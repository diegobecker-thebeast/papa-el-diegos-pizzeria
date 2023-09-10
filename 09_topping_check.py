import pandas

all_topping_menu = ["Extra Cheese", "Extra Pepperoni", "Stuffed Crust"]
all_topping_costs_menu = ["$1.5", "$2.5", "$3.5"]

pizza_menu_dict = {
    "Extra": all_topping_menu,
    "Price": all_topping_costs_menu,
}

topping_order_menu = pandas.DataFrame(pizza_menu_dict)


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


yes_no_list = ["yes", "no"]

# main routine starts here
topping_check = string_checker("Do you want any extra topping?(y/n)", 1, yes_no_list)
if topping_check == "yes":
    print()
    print("---Toppings List---")
    print(topping_order_menu)
    print()

