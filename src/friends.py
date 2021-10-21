def get_name(person):
    return person["name"]

def get_favourite_tv_show(person):
    return person["favourites"]["tv_show"]

def likes_to_eat(person, food):
    if food in person["favourites"]["snacks"]:
        return True
    return False

def add_friend(person, friend):
    person["friends"].append(friend)

def remove_friend(person, friend):
    person["friends"].remove(friend)

def total_money(people):
    total = 0
    for person in people:
        total += person["monies"]
    return total

def l_money(lender, lendee, amount):
    lender["monies"] -= amount
    lendee["monies"] += amount

def all_favourite_foods(people):
    favourites = []
    for person in people:
        favourites.extend(person["favourites"]["snacks"])
    return favourites