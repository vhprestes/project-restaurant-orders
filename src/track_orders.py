class TrackOrders:
    def __init__(self):
        self.__orders = {}

    def __len__(self):
        return len(self.__orders)

    def add_new_order(self, customer, order, day):
        if customer not in self.__orders:
            self.__orders[customer] = {"orders": [], "days_visited": set()}

        self.__orders[customer]["orders"].append(order)
        self.__orders[customer]["days_visited"].add(day)

        return len(self.__orders[customer]["orders"])

    def get_most_ordered_dish_per_customer(self, customer):
        orders = self.__orders.get(customer, {}).get("orders", [])
        if not orders:
            return None
        return max(set(orders), key=orders.count)

    def get_never_ordered_per_customer(self, customer):
        all_orders = set(
            order
            for order in self.__orders.values()
            for order in order["orders"]
        )
        orders = set(self.__orders.get(customer, {}).get("orders", []))
        return all_orders - orders

    def get_days_never_visited_per_customer(self, customer):
        all_days = set(
            day
            for order in self.__orders.values()
            for day in order["days_visited"]
        )
        days = set(self.__orders.get(customer, {}).get("days_visited", []))
        return all_days - days

    def get_busiest_day(self):
        visits_per_day = {}
        for order in self.__orders.values():
            for day in order["days_visited"]:
                visits_per_day[day] = visits_per_day.get(day, 0) + 1
        if not visits_per_day:
            return None
        return max(visits_per_day, key=visits_per_day.get)

    # def get_least_busy_day(self):
    #     visits_per_day = {}
    #     for order in self.__orders.values():
    #         for day in order["days_visited"]:
    #             visits_per_day[day] = visits_per_day.get(day, 0) + 1
    #     if not visits_per_day:
    #         return None
    #     return min(visits_per_day, key=visits_per_day.get)
    def get_least_busy_day(self):
        visits_per_day = {}
        for order in self.__orders.values():
            for day in order["days_visited"]:
                day_index = [
                    "domingo",
                    "segunda-feira",
                    "terça-feira",
                    "quarta-feira",
                    "quinta-feira",
                    "sexta-feira",
                    "sábado"
                ].index(day)
                visits_per_day[day_index] = (
                    visits_per_day.get(day_index, 0) + 1
                )
        if not visits_per_day:
            return None
        least_busy_day_index = min(visits_per_day, key=visits_per_day.get)
        return [
            "segunda-feira",
            "terça-feira",
            "quarta-feira",
            "quinta-feira",
            "sexta-feira",
            "sábado",
            "domingo",
        ][least_busy_day_index]
# MEU DEUS MAS O QUE É ISSO AQUI EM CIMA?!
