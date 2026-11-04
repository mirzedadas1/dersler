#json -  JavaScript Object Notation, dumps(),loads(),indent = 4, ensure_ascii=False,


import json


telebe4 = {
    "ad": "Mirzə",
    "soyad": "Dadaşov",
    "fakulte": "riyaziyyat",
    "yas": 20
}

telebe5 = {
    "ad": "Nicat",
    "soyad": "Hüseynov",
    "fakulte": "riyaziyyat"}


#json yeni melumatlar yazmaq
with open("telebe4.json", "w", encoding="utf-8") as f: #write
    telebe4["fakulte"] = "biologiya"
    json.dump(telebe4, f, indent=4,ensure_ascii=False) 
     # dumps() - string formatina cevirir, dump() - fayla yazir
    print("melumatlar yenilendi")

    #json faylindan oxumaq
with open("telebe4.json", "r", encoding="utf-8") as f : #read
    telebe4 = json.load(f)  # loads() - string formatindan dict formatina cevirir, load() - fayldan oxuyur
    print(telebe4)