import json

def load_data(path):
    """Загружает данные о трансакциях из словаря .json"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

def get_filtered_data(path):
    raw_data = load_data(path)
    data = []
    for i in raw_data:
        if i["state"] == ("EXECUTED"):
            data.append(i)
    return data


# filtered_data = list(filter(lambda x: x["state"] == "EXECUTED", raw_data))
# print(filtered_data)





