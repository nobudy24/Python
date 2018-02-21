
player = int(input("Pick a number between 1-20 "))
    if player == 13 or player == 4:
        state="unlucky"
    elif player%2 ==0 :
        state="even"
    else:
        state="odd"
    print(f"{player} is {state} number")
