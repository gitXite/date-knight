from random import random
from lists import restaurants, activities, movies


dates = {
    "restaurant": choice.restaurants,
    "activity": choice.activities,
    "movie": choice.movies
}

def get_date(dates):
    restaurant = dates["restaurant"]
    activity = dates["activity"]
    movie = None
    if activity == "movie":
        movie = dates["movie"]
        return f"----------\nYour selected date:\nRestaurant: {restaurant}\nMovie: {movie}\n----------"
    return f"----------\nYour selected date:\nRestaurant: {restaurant}\nActivity: {activity}\n----------"
