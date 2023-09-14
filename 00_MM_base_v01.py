import pandas
import random

# PIZZA MENU
# ----------------------------------------------------------------------------
# dictionaries to hold menu details
all_pizza_menu = ["Cheese", "Pepperoni", "Hawaiian", "Meatlovers", "Tuna"]
all_pizza_costs_menu = ["$7.5", "$10.5", "$6.5", "$11.5", "$5.5"]


pizza_menu_dict = {
    "Pizza": all_pizza_menu,
    "Price": all_pizza_costs_menu,
}

pizza_order_menu = pandas.DataFrame(pizza_menu_dict)


# ----------------------------------------------------------------------------

# TOPPING MENU
# ----------------------------------------------------------------------------
all_topping_menu = ["Extra Cheese", "Extra Pepperoni", "Stuffed Crust"]
all_topping_costs_menu = ["$1.5", "$2.5", "$3.5"]


pizza_menu_dict = {
    "Extra": all_topping_menu,
    "Price": all_topping_costs_menu,
}

topping_order_menu = pandas.DataFrame(pizza_menu_dict)
# ----------------------------------------------------------------------------

# checks the user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("sorry bucko, his cant be left blank, try again kid.")
        else:
            return response


# checks users enter an integer to a given question
def num_check(question):

    while True:

        try:
            response = (input(question))
            return response

        except ValueError:
            print("please enter something")


# calculate pizza price based on the pizza
def calc_pizza_price(pizza):

    # pizza is $7.50
    if pizza == 'cheese':
        price = 7.5

    # pizza is $10.50
    elif pizza == 'pepperoni':
        price = 10.5

    # pizza is 6.5 for hawaiian
    elif pizza == 'hawaiian':
        price = 6.5

        # pizza is 11.5 for hawaiian
    elif pizza == 'meatlovers':
        price = 11.5

        # pizza is 5.5 for hawaiian
    elif pizza == 'tuna':
        price = 5.5

    else:
        print('womp womp didnt work')

    return price


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


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# main routine starts here
# set maximum number of pizzas below
MAX_PIZZAS = 5
pizzas_sold = 0

yes_no_list = ["yes", "no"]
payment_list = ["small", "medium", "large"]
pizza_list = ["cheese", "pepperoni", "hawaiian", "meatlovers", "tuna"]
topping_list = ["extra cheese", "extra pepperoni", "stuffed crust", "xxx"]

# dictionaries to hold pizza details
all_pizza = []
all_names = []
all_pizza_costs = []
all_size_scale = []
all_extra = []

# dictionary used to create data frame ie column_name:list
pizza_order_dict = {
    "Name": all_names,
    "Pizza": all_pizza,
    "Price": all_pizza_costs,
    "Size": all_size_scale,
    "Extra": all_extra
}

# ask user if they want instructions
want_instructions = string_checker("Do you want to read the instructions? "
                                   "instructions (y/n): ",
                                   1, yes_no_list)

if want_instructions == "yes":
    print()
    print("This is a beautiful Pizza Ordering Site. Order your pizza and select if you "
          "would like small, medium, or large.")
elif want_instructions == "no":
    pass

# MAX_PIZZAS = num_check("how many pizzas do you want?")

# loop to sell pizza
while pizzas_sold < MAX_PIZZAS:
    print()
    name = not_blank("Please enter your name to start an order 'xxx' to end: ")

    if name == 'xxx':
        break

    menu_check = string_checker("Do you want to see the menu? "
                                   " (y/n): ",
                                   1, yes_no_list)

    if menu_check == "yes":
        print()
        print("---- The Menu ----")
        print()

        # print tables
        print(pizza_order_menu)

        print()
        pass

    pizza = string_checker("what pizza do you want(input the pizza name): ",
                           1, pizza_list)
    if pizza == 'cheese':
        print()
        print("You have purchased a cheese pizza!!!")
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

    # calculate pizza cost
    pizza_cost = calc_pizza_price(pizza)

    # get payment method
    print()
    size_check = string_checker("Choose a size (small / "
                                "medium(+1.5) / large(+2.5)): ",
                                1, payment_list)
    if size_check == "small":
        size_scale = 'S'
        extra = 0
        print()
        print("you have selected a small {} pizza".format(pizza))
    elif size_check == "medium":
        size_scale = 'M'
        extra = 1.5
        print()

        print("you have selected a medium {} pizza".format(pizza))
    elif size_check == "large":
        size_scale = 'L'
        extra = 2.5
        print()
        print("you have selected a large {} pizza".format(pizza))

    topping_check = string_checker("Do you want any extra topping?(y/n)", 1, yes_no_list)
    if topping_check == "yes":
        print()
        print("---Toppings List---")
        print(topping_order_menu)
        print()
        extra_topping = ""
        while extra_topping != "xxx":
            extra_topping = string_checker("What toppings do you want (xxx to end): ", 15, topping_list)
            if extra_topping == "extra cheese":
                extra += 1.5
                topping = "cheese"
                print("you have selected the extra cheese topping")
                print()
            elif extra_topping == "extra pepperoni":
                extra += 2.5
                topping = "pepperoni"
                print("you have selected the extra pepperoni topping")
                print()
            elif extra_topping == "stuffed crust":
                extra += 3.5
                topping = "stuffed"
                print("you have selected the stuffed crust topping")
                print()
            elif extra_topping == "xxx":
                print("you have finished selecting your toppings")

    pizzas_sold += 1

    # add ticket name, cost and size to lists
    all_names.append(name)
    all_pizza.append(pizza)
    all_pizza_costs.append(pizza_cost)
    all_extra.append(extra)
    all_size_scale.append(size_scale)


# create data from dictionary to organise info
pizza_order_frame = pandas.DataFrame(pizza_order_dict)

# calculate the total pizza cost (pizza + size)
pizza_order_frame['Total'] = pizza_order_frame['Extra'] \
                            + pizza_order_frame['Price']

# calculate the profit for each pizza
pizza_order_frame['Profit'] = pizza_order_frame['Price'] - 5

# calculate pizza and profit totals
total = pizza_order_frame['Total'].sum()
profit = pizza_order_frame['Profit'].sum()

# currency formatting (uses currency function)
add_dollars = ['Price', 'Extra', 'Total', 'Profit']
for var_item in add_dollars:
    pizza_order_frame[var_item] = pizza_order_frame[var_item].apply(currency)

print()
print("---- Order Data ----")
print()

# print tables
print(pizza_order_frame)

print()
print("---- Pizza Cost / Profit ----")

# output total pizza sales and profit
print("Total Pizza Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))

print()

# Output number of pizzas sold
if pizzas_sold == MAX_PIZZAS:
    print("Congratulations you have sold all the pizzas")
else:
    print("You have sold {} pizza/s. There is {} pizza/s "
          "remaining".format(pizzas_sold, MAX_PIZZAS - pizzas_sold))