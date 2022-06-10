from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from crop.values import values, crops, predresult, leafs
import pickle
from PIL import Image
from io import BytesIO
import numpy as np
import tensorflow

leafmodel = tensorflow.keras.models.load_model("crop/models/model")


def index(request):
    return render(request, "index.html", {"oplist": values.keys()})


def fertresult(request):
    n = int(request.GET.get("n", 0))
    p = int(request.GET.get("p", 0))
    k = int(request.GET.get("k", 0))
    c = request.GET.get("c", 0)
    result = check([c, n, p, k])
    k = result[0]
    ver = ""
    if result[1] == "+":
        k += "High"
        ver = " IS HIGH"
    else:
        k += "low"
        ver = " IS LOW"
    return JsonResponse({"result": result[0], "desc": predresult[k], "ver": ver})


def check(a):
    global values
    imp = ["N", "P", "K"]
    v = values[a[0]]
    diff = [i-j for i, j in zip(list(v.values()), a[1:])]
    if diff[0] == 0 and diff[1] == 0 and diff[2] == 0:
        return ["all", "="]
    else:
        ma = max(diff)
        mi = min(diff)
        comp = imp[[abs(i) for i in diff].index(max(abs(ma), abs(mi)))]
        am = "+" if abs(ma) < abs(mi) else "-"
        return [comp, am]


class crop:
    def __init__(self, n, p, k, temp, humidity, ph, rain):
        self.n = n
        self.p = p
        self.k = k
        self.temp = temp
        self.humidity = humidity
        self.ph = ph
        self.rain = rain

    def predict(self):
        filename = "crop/models/croprecomndation_model.pkl"
        loaded_model1 = pickle.load(open(filename, 'rb'))
        return (loaded_model1.predict([[self.n, self.p, self.k, self.temp, self.humidity, self.ph, self.rain]]))


def croprecomnder(request):
        result = {"name":"","img":""}
        print(request.GET)
        n = float(request.GET.get('ni'))
        p = float(request.GET.get('p'))
        k = float(request.GET.get('k'))
        temp = float(request.GET.get('temp'))
        humidity = float(request.GET.get('h'))
        ph = float(request.GET.get('phvalue'))
        rain = float(request.GET.get('rainfall'))
        c = crop(n, p, k, temp, humidity, ph, rain)
        name = c.predict()[0]
        result = {}
        for i in crops:
            if i["name"].lower() == name.lower():
                result = i
        return JsonResponse({'result': result["name"].upper(), "img": result["img"]})


def convert(img):
    return np.array(Image.open(BytesIO(img)))


def leafpred(req):
    if req.method == "POST":
        file = req.FILES.get("leaf")
        img = convert(file.read())
        img = np.expand_dims(img/255, 0)
        pred = leafmodel.predict(img)
        fv = np.argmax(pred[0])
        name = leafs[fv]
    return JsonResponse({"name": name})
