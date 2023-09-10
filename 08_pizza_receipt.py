import pandas

# currency formatting function
def currency(x):
    return "${:.2f}".format(x)

# dictionaries to hold pizza details
all_names = ["a", "b", "c", "d", "e"]
all_pizza_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_extra = [0, 1.5, 2.5, 3, 0]

pizza_order_dict = {
    "Name": all_names,
    "Price": all_pizza_costs,
    "Extra": all_extra
}

pizza_order_frame = pandas.DataFrame(pizza_order_dict)
pizza_order_frame = pizza_order_frame.set_index('Name')

# calculate the total pizza cost (pizza + extra)
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

print("---- Pizza Data ----")
print()

# print tables
print(pizza_order_frame)

print()
print("---- Pizza Cost / Profit ----")

# output total pizza sales and profit
print("Total Pizza Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))

