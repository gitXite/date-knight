import random
from date_content import activities_bergen, activities_stavanger, activities_oslo, activities_trondheim


# activity limits
film_activities = [
    "Movie",
    "Cinema",
    "Theatre",
    "Stand up"
]
food_activities = [
    "Restaurant",
    "Homemade dinner"
]


def get_random_activities(activities_city, n, activities_list=None, is_film=False, is_food=False, is_hike=False, attempts=0):
    if activities_list is None:
        activities_list = []
    if n == 0:
        return activities_list
    if attempts > 20:
        return activities_list

    # selects the random activities
    keys = list(activities_city.keys())
    random_key = random.choice(keys)
    value = activities_city[random_key]

    # checks the limit for specific activities and rerolls if limit is reached
    if (is_film and random_key in film_activities) or \
       (is_food and random_key in food_activities) or \
       (is_hike and random_key == "Run/hike"):
        return get_random_activities(activities_city, n, activities_list, is_film, is_food, is_hike, attempts + 1)

    # function body
    if value is None:
        if random_key not in activities_list:
            activities_list.append(random_key)
            print(f"----------\nActivity selected: {random_key}!")
            n -= 1
            if random_key in film_activities:
                is_film = True
            elif random_key in food_activities:
                is_food = True
            elif random_key == "Run/hike":
                is_hike = True
    elif isinstance(value, list):
        activity = random.choice(value)
        if activity not in activities_list:
            activities_list.append(activity)
            print(f"----------\nActivity selected: {random_key}!")
            n -= 1
            if random_key in film_activities:
                is_film = True
            elif random_key in food_activities:
                is_food = True
            elif random_key == "Run/hike":
                is_hike = True
    elif isinstance(value, dict):
        nested_activity = get_random_activities(value, 1, [], is_film, is_food, is_hike)
        if nested_activity and nested_activity[0] not in activities_list:
            activities_list.append(nested_activity[0])
            print(f"----------\nActivity selected: {random_key}!")
            n -= 1
            if random_key in film_activities:
                is_film = True
            elif random_key in food_activities:
                is_food = True
            elif random_key == "Run/hike":
                is_hike = True
    if n > 0:
        return get_random_activities(activities_city, n, activities_list, is_film, is_food, is_hike, attempts + 1)
    return f"----------\nYour date for the evening: {activities_list}"
    
def get_number_activities():
    user_input_num = int(input("Enter number of activities between 1 and 4: "))
    if not 0 < user_input_num < 5:
        raise ValueError("The number of activities must be between 1 and 4")
    return user_input_num

def get_activities_city():
    user_input_city = input("Enter your city: ").lower()
    if user_input_city == "stavanger":
        return activities_stavanger
    elif user_input_city == "bergen":
        return activities_bergen
    elif user_input_city == "oslo":
        return activities_oslo
    elif user_input_city == "trondheim":
        return activities_trondheim
    else:
        raise ValueError("Specified city not available")


city = get_activities_city()
n = get_number_activities()
print(get_random_activities(city, n))
