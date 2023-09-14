import pandas

# functions
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


# main routine starts here
# set maximum number of pizzas below
MAX_PIZZAS = 5
pizzas_sold = 0
price = 0
size_scale = "S"

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

print("Welcome to Papa El Diego's Pizzeria!")

# ask user if they want instructions
want_instructions = string_checker("Do you want to read the instructions on how your order will work? "
                                   "instructions (y/n): ",
                                   1, yes_no_list)

if want_instructions == "yes":
    print()
    print("This is a beautiful Pizza Ordering Program, there are a few simple steps to ordering your pizza:")
    print("1. Give us your Order Name")
    print("2. Select your Pizza Choice (not the number!) ")
    print("3. Select the Size for your Pizza")
    print("4. Select any Extra Toppings (not the number!)")
    print(" Easy Peasy Lemon Squeezy")
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

    pizza = string_checker("Which pizza do you want to order? (input the pizza name): ",
                           1, pizza_list)
    if pizza == 'cheese':
        print()
        price = 7.5
        print("You have selected a ${} cheese pizza".format(price))
        pass
    elif pizza == 'pepperoni':
        print()
        price = 10.5
        print("You have selected a ${} pepperoni pizza".format(price))
        pass
    elif pizza == 'hawaiian':
        print()
        price = 6.5
        print("You have selected a ${} hawaiian pizza".format(price))
        pass
    elif pizza == 'meatlovers':
        print()
        price = 11.5
        print("You have selected a ${} meatlovers pizza".format(price))
        pass
    elif pizza == 'tuna':
        print()
        price = 5.5
        print("You have selected a ${} tuna pizza".format(price))
        pass

    # get size
    print()
    extra = 0
    size_check = string_checker("Choose a size (small(+0) / "
                                "medium(+1.5) / large(+2.5)): ",
                                1, payment_list)
    if size_check == "small":
        size_scale = 'S'
        extra += 0
        print()
        print("You have selected a small {} pizza".format(pizza))
    elif size_check == "medium":
        size_scale = 'M'
        extra += 1.5
        print()

        print("You have selected a medium {} pizza".format(pizza))
    elif size_check == "large":
        size_scale = 'L'
        extra += 2.5
        print()
        print("You have selected a large {} pizza".format(pizza))

    topping_check = string_checker("Do you want any extra topping? (y/n): ", 1, yes_no_list)
    if topping_check == "yes":
        print()
        print("---Toppings List---")
        print(topping_order_menu)
        print()
        extra_topping = ""
        while extra_topping != "xxx":
            extra_topping = string_checker("What toppings do you want? (xxx to end): ", 15, topping_list)
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

    print()
    print("Thanks for ordering with us {}, you're final pizza is:".format(name))
    print("A ${} size {} {} pizza including any toppings you selected".format(price, size_scale, pizza))
    confirmed_order = string_checker("Do you want to confirm your final order (no will reset order): ", 1, yes_no_list)

    if confirmed_order == "yes":
        pizzas_sold += 1
    if confirmed_order == "no":
        print("Ok your order has been cancelled")
        name = "cancelled"
        pizza = "-"
        price = 0
        extra = 0
        size_scale = "-"

# add ticket name, cost and size to lists
    all_names.append(name)
    all_pizza.append(pizza)
    all_pizza_costs.append(price)
    all_extra.append(extra)
    all_size_scale.append(size_scale)


# create data from dictionary to organise info
pizza_order_frame = pandas.DataFrame(pizza_order_dict)

# calculate the total pizza cost (pizza + size)
pizza_order_frame['Total'] = pizza_order_frame['Extra'] \
                            + pizza_order_frame['Price']

# calculate the profit for each pizza
pizza_order_frame['Profit'] = pizza_order_frame['Price'] * .5

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

# to_write = pizza_order_frame

# write_to = "finished order.txt"
# text_file = open(write_to, "w+")

# for item in to_write:

#    text_file.write(item)
#    text_file.write("\n")

# close file
# text_file.close()