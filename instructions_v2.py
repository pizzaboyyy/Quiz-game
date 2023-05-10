# instructions to show the user how to play the game if they have not played before
# instructions_v2


# function to display instructions
def instructions():
    print("***** How to play ******")
    print()
    print("You will be asked a Maori number and you have to answer the question in english (eg. Tahi = one)")
    print()
    print("Have fun!")
    print()


played_before = input("have you played this game before?: ")

if played_before == "Yes":
    print(instructions())
else:
    print("program continues ")
