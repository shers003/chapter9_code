#Simple Game
#This demonstrates how to use a module you made

import game, random

again = None
while again != 'n':

    players = []

    num = game.ask_number(question = 'How many player (2-6): ',
                          low = 2, high = 6)
    for i in range(num):
        name = input('Player '+str(i+1)+' name: ')
        score = random.randrange(100) + 1
        player = game.Player(name,score)
        players.append(player)

    print('Here are the game results:\n')
    for player in players:
        print(player)

    again = game.ask_yes_no('Do you wish to play again? ')
