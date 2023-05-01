# check if user has played the game before
# if they have continue with game if they have not played show instructions
# also check if input is valid

played_game_before = input("Have you played this game before?: ").upper()
instructions = "Hallossss"
valorant = "better"

while valorant == "better":
    if played_game_before == "YES" or "Y":
        print("hello")
    elif played_game_before == "NO" or "N":
        print(instructions)
    else:
        print("Please enter either yes or no")





