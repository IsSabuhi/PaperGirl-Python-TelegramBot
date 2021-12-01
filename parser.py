import json


with open("data.json", "r", encoding='utf8') as file:
    a = json.load(file)

def parser_file():
    old_json = a
    new_json =[]
    for item in old_json:
        discountPrice = item.get("price").get("discountPrice")
        if discountPrice == 0:
            new_json.append({
                "url": item.get("url"),
                "title":  item.get("title"),
                "description": item.get("description"),
                "price": item.get("price").get("originalPrice"),
                "discountPrice": item.get("price").get("discountPrice"),
            })
        with open("new_json.json", "w") as file:
            json.dump(new_json, file, indent=2, ensure_ascii=False)


