from utils import load_data, get_filtered_data, dict_modification, date_formatted, masked_from, masked_to

raw_data = load_data("operations.json")
filtered_data = get_filtered_data(raw_data)
list_of_dicts = dict_modification(filtered_data)
new_list = date_formatted(list_of_dicts)
operation = ""
count = 0

for i in new_list:
    if count == 5:
        break
    else:
        date = i["date"]
        description = i["description"]
        from_param = masked_from(i["from"])
        to_param = masked_to(i["to"])
        amount = i["amount"]
        currency = i["currency"]
        operation = f"{date} {description} \n{from_param} -> {to_param} \n{amount} {currency}\n \n"
        print(operation)
        count += 1