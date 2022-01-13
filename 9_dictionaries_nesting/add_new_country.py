travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(name, visit_amount, cities):
    new_country = {
        "country": name,
        "visits": visit_amount,
        "cities": cities,
    }
    travel_log.append(new_country)


add_new_country(name="Russia", visit_amount=2, cities=["Moscow", "Saint Petersburg"])
print(travel_log)
