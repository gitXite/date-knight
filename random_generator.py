import random
from lists import restaurants, activities, movies


dates = {
    "restaurant": random.choice(restaurants),
    "activity": random.choice(activities),
    "movie": random.choice(movies)
}

def get_date(dates):
    restaurant = dates["restaurant"]
    activity = dates["activity"]
    movie = None
    if activity == "movie":
        movie = dates["movie"]
        return f"----------\nYour selected date:\nRestaurant: {restaurant}\nActivity: {activity}\nMovie suggestion: {movie}\n----------"
    return f"----------\nYour selected date:\nRestaurant: {restaurant}\nActivity: {activity}\n----------"
