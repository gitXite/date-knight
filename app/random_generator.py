import random
from date_content import activities


film_activities = [
    "Movie",
    "Cinema",
    "Theatre"
]
food_activities = [
    "Restaurant",
    "Homemade dinner"
]

def get_random_activities(activities, n, activities_list=None, is_film=False, is_food=False):
    if activities_list is None:
        activities_list = []
    if n == 0:
        return activities_list

    keys = list(activities.keys())
    random_key = random.choice(keys)
    value = activities[random_key]
    if is_film and (random_key in film_activities):
        get_random_activities(activities, n, activities_list, is_film, is_food)
    if is_food and (random_key in food_activities):
        get_random_activities(activities, n, activities_list, is_film, is_food)

    if value is None:
        is_film = True if random_key in film_activities
        if random_key in activities_list:
            get_random_activities(activities, n, activities_list, is_film, is_food)
        else:
            activities_list.append(random_key)
    elif isinstance(value, list):
        is_food = True if random_key in food_activities
        result = random.choice(value)
        if result in activities_list:
            get_random_activities(activities, n, activities_list, is_film, is_food)
        else:
            activities_list.append(activity)
    elif isinstance(value, dict):
        is_film = True if random_key in film_activities
        nested_activity = get_random_activities(value, 1, activities_list, is_film, is_food)
        if nested_activity[0] not in activities_list:
            activities_list.append(nested_activity[0])
    return get_random_activities(activities, n-1, activities_list, is_film, is_food)
    
def get_number_activities(user_input):
    if not 0 < user_input < 5:
        raise ValueError("The number of activities must be between 1 and 4")
    return user_input

user_input = int(input("Enter number of activities between 1 and 4"))
n = get_number_activities(user_input)
