import random
from lists import restaurants, activities, movies


date_details = {
    "restaurant": random.choice(restaurants),
    "activity": random.choice(activities),
    "film": random.choice(movies)
}

def get_date_suggestion(date_details):
    restaurant = date_details["restaurant"]
    activity = date_details["activity"]
    movie = date_details["film"]
    if activity == "film":
        return f"----------\nYour selected date:\nRestaurant: {restaurant}\nActivity: {activity}\nFilm suggestion: {movie}\n----------"
    else:
        return f"----------\nYour selected date:\nRestaurant: {restaurant}\nActivity: {activity}\n----------"
