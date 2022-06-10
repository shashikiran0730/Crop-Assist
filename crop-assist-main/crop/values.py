values = {
    'rice': {'N': 80, 'P': 40, 'K': 40},
    'maize': {'N': 80, 'P': 40, 'K': 20},
    'chickpea': {'N': 40, 'P': 60, 'K': 80},
    'kidneybeans': {'N': 20, 'P': 60, 'K': 20},
    'pigeonpeas': {'N': 20, 'P': 60, 'K': 20},
    'mothbeans': {'N': 20, 'P': 40, 'K': 20},
    'mungbean': {'N': 20, 'P': 40, 'K': 20},
    'blackgram': {'N': 40, 'P': 60, 'K': 20},
    'lentil': {'N': 20, 'P': 60, 'K': 20},
    'pomegranate': {'N': 20, 'P': 10, 'K': 40},
    'banana': {'N': 100, 'P': 75, 'K': 50},
    'mango': {'N': 20, 'P': 20, 'K': 30},
    'grapes': {'N': 20, 'P': 125, 'K': 200},
    'watermelon': {'N': 100, 'P': 10, 'K': 50},
    'muskmelon': {'N': 100, 'P': 10, 'K': 50},
    'apple': {'N': 20, 'P': 125, 'K': 200},
    'orange': {'N': 20, 'P': 10, 'K': 10},
    'papaya': {'N': 50, 'P': 50, 'K': 50},
    'coconut': {'N': 20, 'P': 10, 'K': 30},
    'cotton': {'N': 120, 'P': 40, 'K': 20},
    'jute': {'N': 80, 'P': 40, 'K': 40},
    'coffee': {'N': 100, 'P': 20, 'K': 30}
}

crops = [
    {"name": "pomegranate", "img": "https://www.washingtonpost.com/rf/image_1484w/2010-2019/WashingtonPost/2014/01/10/Production/Health/Images/bigstock-Half-of-pomegranate-on-a-white-12359999.jpg?t=20170517"},
    {"name": "banana","img": "https://cdn.vox-cdn.com/thumbor/O3bgH4_QEuaBXQFpEAxr2HUeWVY=/0x0:5472x3648/1200x800/filters:focal(2299x1387:3173x2261)/cdn.vox-cdn.com/uploads/chorus_image/image/66982287/AdobeStock_245734346.0.0.jpeg"},
    {"name": "mango", "img": "https://c0.wallpaperflare.com/preview/459/506/545/mango-tree-green-food.jpg"},
    {"name":"rice","img":"https://thumbs.dreamstime.com/b/paddy-field-11870763.jpg"},
    {"name":'maize',"img": "https://m.economictimes.com/thumb/msid-85019460,width-1200,height-900,resizemode-4,imgsize-463784/maize.jpg"},
    {"name":'chickpea',"img": "https://www.chilternseeds.co.uk/images/products//img_10440_10898.jpg"},
    {"name":'kidneybeans',"img": "https://media.istockphoto.com/photos/kidney-beans-in-a-bowl-picture-id646869882?k=20&m=646869882&s=612x612&w=0&h=0oLauY7e7FBuMjIYDj2ry56GjrI2jrIwPuis2czdsIs="},
    {"name":'pigeonpeas',"img": "https://cdn.croptrust.org/wp/wp-content/uploads/2014/12/9179813643_60290766da_o-1920x1126.jpg"},
    {"name":'mothbeans',"img": "https://grocerondoor.com/wp-content/uploads/2020/10/Moth-bean-seeds.jpg"},
    {"name":'mungbean',"img": "https://ap.fftc.org.tw/sites/default/files/styles/project_slider/public/31.jpg?itok=rT1ffHN4"},
    {"name":'blackgram',"img": "https://assets.thehansindia.com/hansindia-bucket/1587_Black-Gram-Seeds-Urad-Dal-s.jpg"},
    {"name":'lentil',"img": "https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fimg1.cookinglight.timeinc.net%2Fsites%2Fdefault%2Ffiles%2Fstyles%2F4_3_horizontal_-_1200x900%2Fpublic%2F1561576233%2FGettyImages-689997322.jpg%3Fitok%3Dp0XFQUy-"},
    {"name":'grapes',"img": "https://images.newscientist.com/wp-content/uploads/2021/12/21135850/PRI_215974993.jpg"},
    {"name":'watermelon',"img": "https://www.thespruce.com/thmb/EwSnqbAD1rogPrgizEgfOvNSWtk=/4002x2251/smart/filters:no_upscale()/how-to-grow-watermelons-1403491-hero-2d1ce0752fed4ed599db3ba3b231f8b7.jpg"},
    {"name":'muskmelon',"img": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Muskmelon.jpg"},
    {"name":'apple',"img": "https://ychef.files.bbci.co.uk/976x549/p07v2wjn.jpg"},
    {"name":'orange',"img": "https://rurallivingtoday.com/wp-content/uploads/types-of-oranges-1.jpeg"},
    {"name":'papaya',"img": "https://www.gardeningknowhow.com/wp-content/uploads/2020/05/papaya.jpg"},
    {"name":'coconut',"img": "https://www.deccanherald.com/sites/dh/files/articleimages/2021/10/08/clipboard-2021-10-08t165956599-1038642-1633692738.jpg"},
    {"name":'cotton',"img": "https://bettercotton.org/wp-content/uploads/2021/09/Cotton-boll-Tajikistan-scaled.jpg"},
    {"name":'jute',"img": "https://5.imimg.com/data5/XW/AK/MY-27039311/jute-twine-500x500.jpg"},
    {"name":'coffee',"img": "https://images-prod.healthline.com/hlcmsresource/images/AN_images/safe-to-eat-coffee-beans-1296x728-feature.jpg"},
]


predresult = {
    'NHigh': """ Please consider the following suggestions:
<br>1. Manure  – adding manure is one of the simplest ways to amend your soil with nitrogen. Be careful as there are various types of manures with varying degrees of nitrogen.
<br>2.Coffee grinds  – use your morning addiction to feed your gardening habit! Coffee grinds are considered a green compost material which is rich in nitrogen. Once the grounds break down, your soil will be fed with delicious, delicious nitrogen. An added benefit to including coffee grounds to your soil is while it will compost, it will also help provide increased drainage to your soil.
<br>3. Plant nitrogen fixing plants – planting vegetables that are in Fabaceae family like peas, beans and soybeans have the ability to increase nitrogen in your soil
<br>4. Plant ‘green manure’ crops like cabbage, corn and brocolli
<br>5. Use mulch(wet grass) while growing crops - Mulch can also include sawdust and scrap soft woods""",

    'Nlow': """The N value of your soil is low.
Please consider the following suggestions:
<br>1. Add sawdust or fine woodchips to your soil – the carbon in the sawdust/woodchips love nitrogen and will help absorb and soak up and excess nitrogen.
<br>2.Plant heavy nitrogen feeding plants – tomatoes, corn, broccoli, cabbage and spinach are examples of plants that thrive off nitrogen and will suck the nitrogen dry.
<br>3. Water – soaking your soil with water will help leach the nitrogen deeper into your soil, effectively leaving less for your plants to use.
<br>4. Sugar – In limited studies, it was shown that adding sugar to your soil can help potentially reduce the amount of nitrogen is your soil. Sugar is partially composed of carbon, an element which attracts and soaks up the nitrogen in the soil. This is similar concept to adding sawdust/woodchips which are high in carbon content.
<br>5. Add composted manure to the soil.
<br>6. Plant Nitrogen fixing plants like peas or beans.
<br>7. Use NPK fertilizers with high N value.
<br>8. Do nothing – It may seem counter-intuitive, but if you already have plants that are producing lots of foliage, it may be best to let them continue to absorb all the nitrogen to amend the soil for your next crops.""",

    'PHigh': """The P value of your soil is high.
 Please consider the following suggestions:
<br>1. Avoid adding manure – manure contains many key nutrients for your soil but typically including high levels of phosphorous. Limiting the addition of manure will help reduce phosphorus being added.
<br>2.Use only phosphorus-free fertilizer – if you can limit the amount of phosphorous added to your soil, you can let the plants use the existing phosphorus while still providing other key nutrients such as Nitrogen and Potassium. Find a fertilizer with numbers such as 10-0-10, where the zero represents no phosphorous.
<br>3.Water your soil – soaking your soil liberally will aid in driving phosphorous out of the soil. This is recommended as a last ditch effort.
<br>4. Plant nitrogen fixing vegetables to increase nitrogen without increasing phosphorous(like beans and peas).
<br>5. Use crop rotations to decrease high phosphorous levels""",

    'Plow': """The P value of your soil is low.
Please consider the following suggestions:
<br>1. Bone meal – a fast acting source that is made from ground animal bones which is rich in phosphorous.
<br>2. Rock phosphate – a slower acting source where the soil needs to convert the rock phosphate into phosphorous that the plants can use.
<br>3. Phosphorus Fertilizers – applying a fertilizer with a high phosphorous content in the NPK ratio(example: 10-20-10, 20 being phosphorous percentage).
<br>4. Organic compost – adding quality organic compost to your soil will help increase phosphorous content.
<br>5. Manure – as with compost, manure can be an excellent source of phosphorous for your plants.
<br>6. Clay soil – introducing clay particles into your soil can help retain & fix phosphorus deficiencies.
<br>7. Ensure proper soil pH – having a pH in the 6.0 to 7.0 range has been scientifically proven to have the optimal phosphorus uptake in plants.
<br>8. If soil pH is low, add lime or potassium carbonate to the soil as fertilizers. Pure calcium carbonate is very effective in increasing the pH value of the soil.
<br>9. If pH is high, addition of appreciable amount of organic matter will help acidify the soil. Application of acidifying fertilizers, such as ammonium sulfate, can help lower soil pH""",

    'KHigh': """The K value of your soil is high.
 Please consider the following suggestions:
<br>1. Loosen the soil deeply with a shovel, and water thoroughly to dissolve water-soluble potassium. Allow the soil to fully dry, and repeat digging and watering the soil two or three more times.
<br>2. Sift through the soil, and remove as many rocks as possible, using a soil sifter. Minerals occurring in rocks such as mica and feldspar slowly release potassium into the soil slowly through weathering.
<br>3. Stop applying potassium-rich commercial fertilizer. Apply only commercial fertilizer that has a '0' in the final number field. Commercial fertilizers use a three number system for measuring levels of nitrogen, phosphorous and potassium. The last number stands for potassium. Another option is to stop using commercial fertilizers all together and to begin using only organic matter to enrich the soil.
<br>4. Mix crushed eggshells, crushed seashells, wood ash or soft rock phosphate to the soil to add calcium. Mix in up to 10 percent of organic compost to help amend and balance the soil.
<br>5. Use NPK fertilizers with low K levels and organic fertilizers since they have low NPK values.
<br>6. Grow a cover crop of legumes that will fix nitrogen in the soil. This practice will meet the soil’s needs for nitrogen without increasing phosphorus or potassium.
""",

    'Klow': """The K value of your soil is low.
Please consider the following suggestions:
<br>1. Mix in muricate of potash or sulphate of potash
<br>2. Try kelp meal or seaweed
<br>3. Try Sul-Po-Mag
<br>4. Bury banana peels an inch below the soils surface
<br>5. Use Potash fertilizers since they contain high values potassium
"""
}

leafs = ['Tomato_Bacterial_spot',
         'Tomato_Early_blight',
         'Tomato_Late_blight',
         'Tomato_Leaf_Mold',
         'Tomato_Septoria_leaf_spot',
         'Tomato_Spider_mites_Two_spotted_spider_mite',
         'Tomato__Target_Spot',
         'Tomato__Tomato_YellowLeaf__Curl_Virus',
         'Tomato__Tomato_mosaic_virus',
         'Tomato_healthy']
