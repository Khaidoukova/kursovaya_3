import json
from datetime import date

def load_data(path):
    """Загружает данные о трансакциях из словаря .json"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_filtered_data(path):
    """ Фильтрует данные по параметру "EXECUTED" и создает новый список транзакций"""
    raw_data = load_data(path)
    filtered_data = []
    for i in raw_data:
        if i.get("state") == "EXECUTED":
            filtered_data.append(i)
    return filtered_data

def dict_modification(data):
    """Перепаковывает словари в списке, оставляя только требуемые параметры и добавляя параметры,
    которые в словаре отсутствуют"""
    new_list = []
    for item in data:
        new_dict = {}
        try:
            new_dict["date"] = item["date"][:10]
        except KeyError:
            new_dict["date"] = "Not fount"
        try:
            new_dict["description"] = item["description"]
        except KeyError:
            new_dict["description"] = "Not found"
        try:
            new_dict["from"] = item["from"]
        except KeyError:
            new_dict["from"] = "Not found"
        try:
            new_dict["to"] = item["to"]
        except KeyError:
            new_dict["to"] = "Not found"
        try:
            new_dict["amount"] = item["operationAmount"]["amount"]
        except KeyError:
            new_dict["amount"] = "Not found"
        try:
            new_dict["currency"] = item["operationAmount"]["currency"]["name"]
        except KeyError:
            new_dict["currency"] = "Not found"
        new_list.append(new_dict)
    return sorted(new_list, key=lambda x: x["date"], reverse=True)















