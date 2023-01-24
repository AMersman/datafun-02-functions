"""
Ashley Mersman,1/23/23

Use built-in functions and 
functions from the math module.

To illustrate the ability to call functions and 
display useful results to the user. 

Use your textbook and the examples in this repo to get ideas.

"""

import math

# define some functions

def get_area_of_lot(length, width):
    """
    Return area of a lot given the length and width of the lot.

    Could this fail?

    """

    # Use a try / except / finally block when something 
    # could go wrong
    try: 
        area = length * width # fix this
        return area
    except Exception as ex:
        print(f"Error: {ex}")
        return None


# define more functions here (see instuctions)
def wait_time(num_ppl, rate):
    try:
        wait_time = num_ppl/rate
        return wait_time * 60
    except Exception as ex:
        print(f"Error: {ex}")
        return None

def gross_profit(num_tickets, ticket_price):
    try:
        profit = num_tickets * ticket_price
        return profit
    except Exception as ex:
        print(f"Error: {ex}")
        return None

def opening_night(lst):
    try:
        op_night = math.fsum(lst)
        return op_night
    except Exception as ex:
        print(f"Error: {ex}")
        return None




# -------------------------------------------------------------
# Call some functions and execute code!
open_profits = [1.4, 5.6, 6.7, 1.2, 6.7]

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")
    print("Explore some functions in the math module")
    print()
    print(f"math.comb(5,1) = {math.comb(5,1)}")
    print(f"math.perm(5,1) = {math.perm(5,1)}")
    print(f"area of lot(2,3) = {get_area_of_lot(2,3)}")
    print(f"wait_time(35 people, 30 people per hour) = {round(wait_time(35,30),2)} minutes.")
    print(f"gross_profit(1000200,11.95) = {gross_profit(1000200,11.95)}")
    print(f"opening_night([1.4, 5.6, 6.7, 1.2, 6.7]) = {opening_night(open_profits)} million dollars.")