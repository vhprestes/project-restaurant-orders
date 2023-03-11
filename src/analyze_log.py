import csv


def get_data_from_file(path_to_file):
    try:
        with open(path_to_file, encoding="utf-8") as file:
            data = list(csv.reader(file, delimiter=",", quotechar='"'))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    if not data:
        raise ValueError("Arquivo de entrada vazio.")
    return data


def count_items_by_person(data, person):
    items = {}
    for name, food, _ in data:
        if name == person:
            items[food] = items.get(food, 0) + 1
    return items


def get_most_ordered_food(data, person):
    items = count_items_by_person(data, person)
    if not items:
        raise ValueError(f"{person} não fez nenhum pedido.")
    most_ordered_food = max(items, key=items.get)
    return most_ordered_food


def get_foods_not_ordered_by_person(data, person):
    all_foods = {food for _, food, _ in data}
    foods_ordereds = {food for name, food, _ in data if name == person}
    return all_foods - foods_ordereds


def get_days_not_visited_by_person(data, person):
    all_days = {day for _, _, day in data}
    days_visited_by_person = {day for name, _, day in data if name == person}
    return all_days - days_visited_by_person


def write_results_to_file(path_to_file, data):
    with open(path_to_file, mode="w") as file:
        file.write("\n".join(str(item) for item in data))


def check_file_extension(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")


def analyze_log(path_to_file):
    check_file_extension(path_to_file)
    data = get_data_from_file(path_to_file)
    results = [
        get_most_ordered_food(data, "maria"),
        count_items_by_person(data, "arnaldo").get("hamburguer", 0),
        get_foods_not_ordered_by_person(data, "joao"),
        get_days_not_visited_by_person(data, "joao"),
    ]
    write_results_to_file("data/mkt_campaign.txt", results)

# print(analyze_log("data/orders_1.csv"))
