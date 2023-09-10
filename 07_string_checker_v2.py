# checks that users enter a valid response (eg yes / no
# based on a list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid response"

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item
        else:
            print("You have to input a valid response")

# main routine starts here
yes_no_list = ["yes", "no"]
payment_list = ["small", "medium", "large"]
pizza_list = ["cheese", "pepperoni", "hawaiian", "meatlovers", "tuna"]
topping_list = ["extra cheese", "extra pepperoni", "stuffed crust", "xxx"]