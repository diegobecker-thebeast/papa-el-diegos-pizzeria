# function goes here

# checks the user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("sorry bucko, his cant be left blank, try again kid.")
        else:
            return response


# main routine goes here
while True:
    name = not_blank("enter your name (or 'xxx' to quit)")
    if name == "xxx":
        break

print("We are done")