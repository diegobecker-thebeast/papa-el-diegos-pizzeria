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

pizza_list = ["cheese", "pepperoni", "hawaiian", "meatlovers", "tuna"]

# main routine goes here
while True:
    pizza = string_checker("what pizza do you want(input the pizza name): ",
                           1, pizza_list)
    if pizza == 'cheese':
        print()
        print("You have purchased a cheese pizza")
        pass
    elif pizza == 'pepperoni':
        print()
        print("You have purchased a pepperoni pizza")
        pass
    elif pizza == 'hawaiian':
        print()
        print("You have purchased a pineapple pizza")
        pass
    elif pizza == 'meatlovers':
        print()
        print("You have purchased a meatlovers pizza")
        pass
    elif pizza == 'tuna':
        print()
        print("You have purchased a tuna pizza")
        pass