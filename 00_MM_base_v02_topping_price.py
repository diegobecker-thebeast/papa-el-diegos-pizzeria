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
def calc_pizza_price(var_pizza):

    # pizza is $7.50 for people under 16
    if var_pizza == 'cheese' or '1':
        price = 7.5

    # pizza is $10.50 for people between 16 and 64
    elif var_pizza == 'pepperoni' or '2':
        price = 10.5

    # pizza is 6.5 for hawaiian
    elif var_pizza == 'hawaiian' or '3':
        price = 6.5

    # pizza price is $6.50 for 65+
    else:
        print('womp womp didnt work')

    return price


# checks that users enter a valid response (eg yes / no
# cash / credit) based on a list of options
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
pizza_list = ["cheese", "pepperoni", "hawaiian"]
topping_list = ["extra cheese", "extra pepperoni", "stuffed crust"]

# dictionaries to hold pizza details
all_pizza = []
all_names = []
all_pizza_costs = []
all_size_scale = []
all_size = []
textra = []

# dictionary used to create data frame ie column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Pizza": all_pizza,
    "Price": all_pizza_costs,
    "Size": all_size_scale,
    "Extra": all_size
}

# ask user if they want instructions
want_instructions = string_checker("Do you want to read the instructions? "
                                   "instructions (y/n): ",
                                   1, yes_no_list)
topping_price = 0
size = 0
extra = size + topping_price

if want_instructions == "yes":
    print()
    print("This is a beautiful Pizza Ordering Site. Order your pizza and select if you "
          "would like small, medium, or large.")
elif want_instructions == "no":
    pass


# loop to sell pizza
while pizzas_sold < MAX_PIZZAS:
    print()
    name = not_blank("Please enter your name or 'xxx' to quit: ")

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
    else:
        print()
        print("You have to input one of the options buddy")
        continue

        # calculate pizza cost
    pizza_cost = calc_pizza_price(pizza)

    # get payment method
    print()
    pay_method = string_checker("Choose a size (small / "
                                "medium(+1.5) / large(+2.5)): ",
                                1, payment_list)
    if pay_method == "small":
        size_scale = 'S'
        size = 0
        print()
        print("you have selected da small {} pizza".format(pizza))
    elif pay_method == "medium":
        size_scale = 'M'
        size = 1.5
        print()

        print("you have selected a medium {} pizza".format(pizza))
    elif pay_method == "large":
        size_scale = 'L'
        size = 2.5
        print()
        print("you have selected da large {} pizza".format(pizza))

    topping_check = string_checker("Do you want any extra toppings?(y/n)", 1, yes_no_list)

    if topping_check == "yes":
        print()
        print("---Toppings List---")
        print(topping_order_menu)
        print()
        extra_topping = string_checker("What topping do you want: ", 15, topping_list)
        if extra_topping == "extra cheese":
            size += 1.5
            topping = "cheese"
            print("you have selected da cheese topping")
        elif extra_topping == "extra pepperoni":
            size += 2.5
            topping = "pepperoni"
            print("you have selected da extra pepperoni topping")
        elif extra_topping == "stuffed crust":
            size += 3.5
            topping = "stuffed"
            print("you have selected da stuffed crust topping")

    pizzas_sold += 1

    # add ticket name, cost and size to lists
    all_names.append(name)
    all_pizza.append(pizza)
    all_pizza_costs.append(pizza_cost)
    all_size.append(size)
    all_size_scale.append(size_scale)



# create data from dictionary to organise info
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

# mini_movie_frame['Extra'] = mini_movie_frame['Size Extra'] + mini_movie_frame['Topping']
# mini_movie_frame['TExtra'] = mini_movie_frame['Topping'] \
#                            + mini_movie_frame['Extra']

# calculate the total pizza cost (pizza + size)
mini_movie_frame['Total'] = mini_movie_frame['Extra'] \
                            + mini_movie_frame['Price']

# calculate the profit for each pizza
mini_movie_frame['Profit'] = mini_movie_frame['Price'] - 5

# calculate pizza and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# currency formatting (uses currency function)
add_dollars = ['Price', 'Extra', 'Total', 'Profit', textra]
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner name i n list
win_index = all_names.index(winner_name)

# look up total amount own ie price + size
total_won = mini_movie_frame.at[win_index, 'Total']

print()
print("---- Order Data ----")
print()

# print tables
print(mini_movie_frame)

print()
print("---- Pizza Cost / Profit ----")

# output total pizza sales and profit
print("Total Pizza Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))

print()
print('---- Pizza Winner ----')
print("Congratulations {}. You have won {} ie: your "
      " pizza is free!!!".format(winner_name, total_won))


# Output number of pizzas sold
if pizzas_sold == MAX_PIZZAS:
    print("Congratulations you have sold all the pizzas")
else:
    print("You have sold {} pizza/s. There is {} pizza/s "
          "remaining".format(pizzas_sold, MAX_PIZZAS - pizzas_sold))








