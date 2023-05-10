import json


def load_data(path):
    """Загружает данные о трансакциях из словаря .json"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_filtered_data(data):
    """ Фильтрует данные по параметру "EXECUTED" и создает новый список транзакций"""
    filtered_data = []
    for i in data:
        if i.get("state") == "EXECUTED":
            filtered_data.append(i)
    return filtered_data


def dict_modification(data):
    """Перепаковывает словари в списке, оставляя только требуемые параметры и добавляя параметры,
    которые в словаре отсутствуют, сортирует список по датеgit"""
    new_list = []
    for item in data:
        new_dict = {}
        new_dict["date"] = item["date"][:10]
        new_dict["description"] = item["description"]
        try:
            new_dict["from"] = item["from"]
        except KeyError:
            new_dict["from"] = "Not found"
        new_dict["to"] = item["to"]
        new_dict["amount"] = item["operationAmount"]["amount"]
        new_dict["currency"] = item["operationAmount"]["currency"]["name"]
        new_dict["currency"] = item["operationAmount"]["currency"]["name"]
        new_list.append(new_dict)
    return sorted(new_list, key=lambda x: x["date"], reverse=True)

def date_formatted(new_list):
    """Переписывает дату в требуемом формате"""
    for i in new_list:
        year, month, day = i["date"].split("-")
        i["date"] = f"{day}.{month}.{year}"
    return new_list

def masked_from(from_param):
    """Закрывает часть информации в выводе в соответствие с требованиями"""
    if len(from_param) == 25:
        return f"Счет **{from_param[-4:]}"
    elif len(from_param) == 9:
        return from_param
    else:
        return f"{from_param[:-12]} {from_param[-11:-10]}** **** {from_param[-4:]} ->"

def masked_to(to_param):
    """Закрывает часть информации в выводе в соответствие с требованиями"""
    if len(to_param) == 25:
        return f"Счет **{to_param[-4:]}"
    else:
        return f"{to_param[:-12]} {to_param[-11:-10]}** **** {to_param[-4:]}"
















