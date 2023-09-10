import pandas

all_topping_menu = ["Extra Cheese", "Extra Pepperoni", "Stuffed Crust"]
all_topping_costs_menu = ["$1.5", "$2.5", "$3.5"]


pizza_menu_dict = {
    "Extra": all_topping_menu,
    "Price": all_topping_costs_menu,
}

topping_order_menu = pandas.DataFrame(pizza_menu_dict)




print("---- The Toppings ----")
print()

# print tables
print(topping_order_menu)

print()


