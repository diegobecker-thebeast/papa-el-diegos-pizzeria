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

pizza = "cheese"
payment_list = ["small", "medium", "large"]

while True:
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

    print("this size option will add a bonus fee of ${} to the pizza".format(extra))