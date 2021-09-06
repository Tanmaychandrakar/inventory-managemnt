products = {
    1001 : {"name":"Pepsi Can",               "price":153,  "quan":50,  "expiry":"20 oct 2023",  "brand":"Pepsi"},
    1002 : {"name":"Tata Salt",               "price":20,   "quan":130, "expiry":"12 jan 2022",  "brand":"Tata"},
    1003 : {"name":"Tata Tea Gold",           "price":48,   "quan":145, "expiry":"10 mar 2023",  "brand":"Tata"},
    1004 : {"name":"Turmeric Powder",         "price":52,   "quan":122, "expiry":"23 jun 2023",  "brand":"Tata"},
    1005 : {"name":"Quaker Oats",             "price":285,  "quan":30,  "expiry":"30 oct 2022",  "brand":"Quaker"},
    1006 : {"name":"Saffola Active",          "price":207,  "quan":58,  "expiry":"29 jan 2022",  "brand":"Saffola"},
    1007 : {"name":"Kitkat Desert",           "price":55,   "quan":59,  "expiry":"31 aug 2022",  "brand":"Nestle"},
    1008 : {"name":"Dark Fantasy Choco Fills","price":90,   "quan":90,  "expiry":"21 feb 2022",  "brand":"Dark Fantasy"},
    1009 : {"name":"Candyman Fantasy",        "price":80,   "quan":95,  "expiry":"28 dec 2021",  "brand":"Candyman Fantastik"},
    1010 : {"name":"Lotte Choco Pie",         "price":110,  "quan":95,  "expiry":"01 jun 2022",  "brand":"Lotte"},
    1011 : {"name":"Britania Chocolate cake", "price":120,  "quan":100, "expiry":"15 jul 2022",  "brand":"Britania"},
    1012 : {"name":"Pillsbury cookes cake",   "price":90,   "quan":200, "expiry":"02 dec 2021",  "brand":"Pillsbury"},
    1013 : {"name":"Kraft Oreo Soft Cake",    "price":249,  "quan":120, "expiry":"30 dec 2021",  "brand":"Ore0"},
    1014 : {"name":"Mom's Magic Cashew",      "price":80,   "quan":180, "expiry":"19 mar 2022",  "brand":"Sunfeast"},
    1015 : {"name":"Cadbury Oreo chacolate",  "price":60,   "quan":185, "expiry":"19 feb 2022",  "brand":"Cadbury"},
    1016 : {"name":"Betty Croker Pancake",    "price":346,  "quan":190, "expiry":"15 jan 2022",  "brand":"Betty Croker"},
    1017 : {"name":"Parle G Original",        "price":67,   "quan":140, "expiry":"13 dec 2011",  "brand":"Parle"},
    1018 : {"name":"Lays Potato Chips",       "price":30,   "quan":450, "expiry":"14 feb 2023",  "brand":"Lay's"},
    1019 : {"name":"Bingo! Mad Angle",        "price":25,   "quan":440, "expiry":"20 dec 2023",  "brand":"Bingo!"},
    1020 : {"name":"Kellogg's pringles",      "price":85,   "quan":400, "expiry":"25 jan 2024",  "brand":"Kellog's"},
    1021 : {"name":"Dorito's Nacho Chips",    "price":90,   "quan":360, "expiry":"22 jan 2023",  "brand":"Dorito's"},
    1022 : {"name":"Thums Up Soft Drink",     "price":40,   "quan":60,  "expiry":"20 dec 2024",  "brand":"Thums Up"},
    1023 : {"name":"Svami Soda Water",        "price":55,   "quan":70,  "expiry":"20 jun 2023",  "brand":"Svami"},
    1024 : {"name":"Coca-Cola",               "price":65,   "quan":60,  "expiry":"22 jul 2023",  "brand":"Coca Cola"},
    1025 : {"name":"Sprite Lime Flavor",      "price":89,   "quan":40,  "expiry":"20 nov 2023",  "brand":"Sprite"},
    1026 : {"name":"Colgate Maxfresh",        "price":215,  "quan":55,  "expiry":"20 jun 2024",  "brand":"Colgate"},
    1027 : {"name":"Pepsodent Gum Care",      "price":300,  "quan":150, "expiry":"15 jul 2022",  "brand":"Pepsodent"},
    1028 : {"name":"Dabur Amla Hair Oil",     "price":247,  "quan":100, "expiry":"10 aug 2024",  "brand":"DABUR"},
    1029 : {"name":"Nivea Men Face Wash",     "price":149,  "quan":98,  "expiry":"31 jul 2022",  "brand":"Nivea"},
    1030 : {"name":"Himalaya Herbal Face wash","price":104, "quan":200, "expiry":"22 may 2022",  "brand":"Himalaya"},
    1031 : {"name":"Himalaya Baby Powder",    "price":243,  "quan":150, "expiry":"31 may 2024",  "brand":"Himalaya"},
    1032 : {"name":"Nivea Talcum Powder",     "price":199,  "quan":120, "expiry":"31 may 2024",  "brand":"Nivea"},
    1033 : {"name":"Fogg Xtremo Scent",       "price":299,  "quan":155, "expiry":"01 jan 2024",  "brand":"FOGG"},
    1034 : {"name":"Villain Perfume men",     "price":555,  "quan":230, "expiry":"31 may 2024",  "brand":"Villian"},
    1035 : {"name":"Dairy Milk Silk",         "price":475,  "quan":50,  "expiry":"31 jan 2022",  "brand":"Cadbury"}
}

import json

js = json.dumps(products)
fd = open("products.json","w")
fd.write(js)
fd.close()

fd = open("products.json",'r')

r = fd.read()

fd.close()
products = json.loads(r)


prod_id = input("Enter the Product ID: ")
name = input("Enter the Name of the Product: ")
price = int(input("Enter the price per Item: "))
quan = int(input("Enter The Quantity of the Product you want to add: "))
expiry = input("Enter the expiry date of the Product: ")
brand = input("Enter the Brand of the product: ")

products[prod_id] = {"name":name,"price":price,"quan":quan,"expiry":expiry,"brand":brand}

js = json.dumps(products)

fd = open("products.json","w")
fd.write(js)
fd.close()