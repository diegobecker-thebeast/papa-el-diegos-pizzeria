import pandas


# checks that users enter a valid response (eg yes / no
# based on a list of options
def string_checker(question, num_letters, valid_responses):

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

price = 7.5
name = "beng"
pizza = "cheese"
extra = 3
size_scale = "M"


print()
print("Thanks for ordering with us {}, you're final pizza is:".format(name))
print("A ${} size {} {} pizza including any toppings you selected".format(price, size_scale, pizza))
confirmed_order = string_checker("Do you want to confirm your final order (no will reset order): ", 1, yes_no_list)
if confirmed_order == "no":
    print("Ok your order has been cancelled")
    name = "cancelled"
    pizza = "-"
    price = 0
    extra = 0
    size_scale = "-"

print("name= {}  "
      "pizza= {}  "
      "price= ${}  "
      "extra= ${}  "
      "size= {}  ".format(name, pizza, price, extra, size_scale))

