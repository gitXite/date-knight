import random
from date_content import activities


def get_random_date_suggestion(n):
    if not 0 < n < 6:
        raise ValueError("The number of activities must be between 1 and 5")
    
    
def get_number_activities(user_input):
    n = int(input("Enter number of activities between 1-5"))
    if not 0 < n < 6:
        raise ValueError("The number of activities must be between 1 and 5")
    return n
