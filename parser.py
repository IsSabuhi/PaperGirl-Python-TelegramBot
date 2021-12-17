from datetime import datetime
import requests
import json


def pars_json():
    url = "https://pipergirl.devhtw.ru/api/freegames"
    a = requests.get(url)
    data_json = a.json()
    # print(json.dumps(data_json, indent=2))

    with open("discounts_game.json", "w") as file:
        json.dump(data_json, file, indent=2, ensure_ascii=False)
    file.close()


def parser_discounts_game():
    pars_json()
    with open("discounts_game.json", "r") as f:
        b = json.load(f)
    old_json = b
    new_json = []

    for item in old_json:
        sd = item.get("promotions").get("startDate")
        startDate = datetime.fromisoformat((sd[: -1]))
        ed = item.get("promotions").get("endDate")
        endDate = datetime.fromisoformat((ed[: -1]))
        new_json.append({
            "url": item.get("url"),
            "title":  item.get("title"),
            "description": item.get("description"),
            "price": item.get("price").get("originalPrice"),
            "discountPrice": item.get("price").get("discountPrice"),
            "startDate": str(startDate),
            "endDate": str(endDate)
        })

        with open("new_json.json", "w") as file:
            json.dump(new_json, file, indent=2, ensure_ascii=False)
        file.close()


if __name__ == '__main__':
    parser_discounts_game()
