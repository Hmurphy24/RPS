import random

rock_paper_scissors_dictionary = {'Wins': 0, 'Losses': 0, 'Ties': 0, 'Games Played': 0}


def rock_paper_scissors_game_rules():

    print()

    print('Welcome to Rock, Paper Scissors! Try your best to beat the computer!')

    print()


def rock_paper_scissors_weapon_picker():

    rock_paper_scissors_weapons = ['ROCK', 'PAPER', 'SCISSORS']

    rock_paper_scissors_computer_weapon = random.choice(rock_paper_scissors_weapons)

    while True:

        rock_paper_scissors_user_weapon = input('Do you want to use Rock, Paper or Scissors? ')

        if rock_paper_scissors_user_weapon.upper() in rock_paper_scissors_weapons:

            break

        else:

            print('Please pick Rock, Paper or Scissors!')

    return rock_paper_scissors_computer_weapon.upper(), rock_paper_scissors_user_weapon.upper()


def rock_paper_scissors_outcome_calc(computer_weapon, user_weapon):

    if computer_weapon == user_weapon:

        print('You and the computer both picked the same thing!')

        rock_paper_scissors_dictionary['Ties'] += 1

    elif computer_weapon == 'ROCK' and user_weapon == 'SCISSORS':

        print('The computer crushed your scissors!')

        rock_paper_scissors_dictionary['Losses'] += 1

    elif computer_weapon == 'PAPER' and user_weapon == 'ROCK':

        print('The computer covered your rock!')

        rock_paper_scissors_dictionary['Losses'] += 1

    elif computer_weapon == 'SCISSORS' and user_weapon == 'PAPER':

        print('The computer cut your paper!')

        rock_paper_scissors_dictionary['Losses'] += 1

    elif user_weapon == 'ROCK' and computer_weapon == 'SCISSORS':

        print('You crushed the computer\'s scissors!')

        rock_paper_scissors_dictionary['Wins'] += 1

    elif user_weapon == 'PAPER' and computer_weapon == 'ROCK':

        print('You covered the computer\'s rock!')

        rock_paper_scissors_dictionary['Wins'] += 1

    elif user_weapon == 'SCISSORS' and computer_weapon == 'PAPER':

        print('You cut the computer\'s paper!')

        rock_paper_scissors_dictionary['Wins'] += 1


def rock_paper_scissors_replay():

    print()

    print('Here\'s the score:')

    print(rock_paper_scissors_dictionary)

    print()

    while True:

        rock_paper_scissors_replay_input = input('Do you want to play again? ')

        if rock_paper_scissors_replay_input.upper() == 'YES':

            print('Okay, here we go again!')

            print()

            break

        elif rock_paper_scissors_replay_input.upper() == 'NO':

            print('Okay, I\'ll see you later!')

            exit()

        else:

            print('Please enter either "Yes" or "No"!')


rock_paper_scissors_game_rules()

while True:

    rock_paper_scissors_computer_user_weapons = rock_paper_scissors_weapon_picker()

    rock_paper_scissors_outcome_calc(rock_paper_scissors_computer_user_weapons[0], rock_paper_scissors_computer_user_weapons[1])

    rock_paper_scissors_dictionary['Games Played'] += 1

    rock_paper_scissors_replay()
