import pandas

# dictionaries to hold menu details
all_names = ["diego", "flynn", "beng", "kelly", "cancelled"]
all_pizza = ["cheese", "pepperoni", "cheese", "hawaiian", "cancelled"]
all_pizza_costs = [7.5, 10.5, 7.5, 6.5, 0]
all_size_scale = ["S", "L", "M", "S", "-"]
all_extra = [2.5, 2.5, 1.5, 0, 0]

# dictionary used to create data frame ie column_name:list
pizza_order_dict = {
    "Name": all_names,
    "Pizza": all_pizza,
    "Price": all_pizza_costs,
    "Size": all_size_scale,
    "Extra": all_extra
}

pizza_order_menu = pandas.DataFrame(pizza_order_dict)

print(pizza_order_menu)
