# check if user has played the game before
# if they have continue with game if they have not played show instructions
# also check if input is valid
# yes_no_checkerv1

# yes/no checking function
show_instructions = ""


def yes_no(show_instructions):
    while True:

        # Ask the user if they have played before
        show_instructions = input("Have you played this game before?: ")
        # If they say yes, output 'Program Continues
        if show_instructions == "yes" or show_instructions == "y":
            print("Program continues")

        # If they say no, output 'display instructions'
        elif show_instructions == "no" or show_instructions == "n":
            print("Display instructions")

        # Otherwise - show error
        else:
            print("Please answer 'yes' or 'no'")