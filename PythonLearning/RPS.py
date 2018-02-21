import os,random

gamesPlayed = 0
score = 0

os.system('cls')


print('\n Welcome to: \n\n"Rock Paper Scissors!" \n')
playerInputGameMode = int(input('Choose a best of... \n"1:3 Games"\n"2:5 Games"\n"3:9 Games"\n'))
if playerInputGameMode == 1:
    gameMode = 3
elif playerInputGameMode == 2:
    gameMode = 5
else:
    gameMode = 9
os.system('cls')
print(f'You are playing the best of {gameMode}')
input()
os.system('cls')
while score<gameMode:
    os.system('cls')
    print(f'Your have {score} of {gameMode} wins')
    print('\n\n\n"Rock Paper Scissors!" \n')
    playerInput = int(input('Pick a choice \n"1:Rock"\n"2:Paper"\n"3:Scissor"\n'))
    enemyRandom = random.randint(1,3)
    os.system('cls')
    gamesPlayed+=1
    if playerInput == enemyRandom:
        print('Draw!')
    elif (playerInput == 1 and enemyRandom == 3) or (playerInput == 2 and enemyRandom == 1) or (playerInput == 3 and enemyRandom == 2):
        print('You Win!')
        score+=1
    else:
        print('You Lose!')
    print('\npress any key to continue...')
    input()

winrate = score/gamesPlayed
print(f'Your rate was {winrate} %')
