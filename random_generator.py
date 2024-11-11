from random import random


dates = {
    "restaurant": choice.restaurants,
    "activity": choice.activities,
    "movie": choice.movies
}

def get_date(dates):
    restaurant = pairing["restaurant"]
    activity = pairing["activity"]
    movie = None
    if activity == "movie":
        movie = pairing["movie"]
        return f"----------\nYour selected date:\nRestaurant: {restaurant}\nMovie: {movie}\n----------"
    return f"----------\nYour selected date:\nRestaurant: {restaurant}\nActivity: {activity}\n----------"
