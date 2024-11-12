import random
from date_content import activities


def get_random_activities(activities, n, activities_list=None):
    if activities_list is None:
        activities_list = []
    if n == 0:
        return activities_list

    keys = list(activities.keys())
    random_key = random.choice(keys)
    value = activities[random_key]

    if value is None:
        if random_key in activities_list:
            get_random_activities(activities, n, activities_list=None)
        else:
            activities_list.append(random_key)
    elif isinstance(value, list):
        activities_list.append(random.choice(value))
    elif isinstance(value, dict):
        nested_activity = get_random_activities(value, 1, activities_list)
        activities_list.append(nested_activity[0])
    return get_random_activities(activities, n-1, activities_list)
    
def get_number_activities(user_input):
    if not 0 < user_input < 6:
        raise ValueError("The number of activities must be between 1 and 5")
    return user_input

user_input = int(input("Enter number of activities between 1 and 5"))
n = get_number_activities(user_input)
