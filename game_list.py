from random import randrange

games = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']

minimum = 3 # Minimum amount of games that must be given back
maximum = 10 # Maximum amount of games that must be given back

def spelProgramma(spelList, minimum, maximum):
    total_game_amount = randrange(minimum, maximum)

    for i in range(total_game_amount):
        num = randrange(0, (len( games) -1))
        random_game = games[num]

        print(random_game)


spelProgramma(games, minimum, maximum)