import random
from date_content import activities


def get_random_date_suggestion(n):
    result = []
    if n == 0:
        return
    
    
def get_number_activities():
    user_input = int(input("Enter number of activities between 1 and 5"))
    if not 0 < user_input < 6:
        raise ValueError("The number of activities must be between 1 and 5")
    return user_input