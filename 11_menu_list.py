import pandas

# dictionaries to hold ticket details
all_pizza_menu = ["Cheese", "Pepperoni", "Hawaiian", "Meatlovers", "Tuna"]
all_pizza_costs_menu = ["$7.5", "$10.5", "$6.5", "$11.5", "$5.5"]


pizza_order_dict = {
    "Pizza": all_pizza_menu,
    "Price": all_pizza_costs_menu,
}

pizza_order_menu = pandas.DataFrame(pizza_order_dict)




print("---- The Menu ----")
print()

# print tables
print(pizza_order_menu)

print()


