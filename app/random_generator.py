import random
from date_content import activities


def get_random_activities(activities, n, activities_list=None, is_restaurant=False, is_movie=False):
    if activities_list is None:
        activities_list = []
    if n == 0:
        return activities_list

    keys = list(activities.keys())
    random_key = random.choice(keys)
    value = activities[random_key]
    if is_restaurant and random_key == "Restaurant":
        get_random_activities(activities, n, activities_list, is_restaurant, is_movie)
    if is_movie and random_key == "Movie":
        get_random_activities(activities, n, activities_list, is_restaurant, is_movie)

    if value is None:
        if random_key in activities_list:
            get_random_activities(activities, n, activities_list, is_restaurant, is_movie)
        else:
            activities_list.append(random_key)
    elif isinstance(value, list):
        is_restaurant = True if random_key == "Restaurant"
        result = random.choice(value)
        if result in activities_list:
            get_random_activities(activities, n, activities_list, is_restaurant, is_movie)
        else:
            activities_list.append(activity)
    elif isinstance(value, dict):
        is_movie = True if random_key == "Movie"
        nested_activity = get_random_activities(value, 1, activities_list, is_restaurant, is_movie)
        if nested_activity[0] in activities_list:
            get_random_activities(activities, n, activities_list, is_restaurant, is_movie)
        else:
            activities_list.append(nested_activity[0])
    return get_random_activities(activities, n-1, activities_list, is_restaurant, is_movie)
    
def get_number_activities(user_input):
    if not 0 < user_input < 6:
        raise ValueError("The number of activities must be between 1 and 5")
    return user_input

user_input = int(input("Enter number of activities between 1 and 5"))
n = get_number_activities(user_input)
