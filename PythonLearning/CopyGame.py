import os

os.system('cls')
userInput=input(f'Terminal: Hello how are you?\nUser    : ')
os.system('cls')
while userInput != 'stop copying me':
    if userInput =='help' or userInput=='stop' or userInput=='quit':
        print(f'Terminal: AH..AH..AH..')
    else:
        print(f'Terminal: {userInput}')
    userInput=input(f'User    : ')
    os.system('cls')
print('CONGRATULATIONS YOU BEAT A COMPUTER!')
input()
