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

# main routine goes here

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
