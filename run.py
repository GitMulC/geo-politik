import os
from os import system, name
import time


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


# def menu():
#     """
#     Runs opening menu screen on startup.
#     """
#     while True:
#         print('Welcome to GeoPolitik, the geo-political adventure game!')
#         print('Face geo-political challenges to survive as a nation.\n')
#         print('About - a')
#         print('Play - p')
#         print('Quit - q\n')

#         selection = input('Select an option: \n')

#         if selection == 'a':
#             print('About')
#             return False
#         elif selection == 'p':
#             print('Play')
#             return False
#         elif selection == 'q':
#             print('Quit')
#             return False
#         else:
#             print('Please select a viable option.')
#             return True
#     return selection

#     #     if menu_validate(selection):
#     #         print(f'You have chosen {selection}')
#     #         break
#     # return selection


# # def menu_validate(values):
# #     """
# #     Check if selection in menu is correct.
# #     """
# #     # if len(values) == 1:
# #     #     print('Correct text!')
# #     #     return True
# #     # elif len(values) != 1:
# #     #     print('Wrong text!')
# #     #     return False
# #     # elif values.isalpha():
# #     #     return True
# #     if
# #     else:
# #         return False


# # menu()

# current_scenario = 0


# def main_game():
#     """
#     """
#     scenario_texts = [
#         'China flyovers. Defence misniter urges retaliation.',
#         'Something else bad happens.\nWhat do?',
#         'blah'
#     ]
#     while True:
#         print(scenario_texts[current_scenario])
#         selection = input('\nWhat will you do?\n')
#         decision()


# def decision(current_scenario,selection):
#     if selection == 'y':
#         print('You retaliate, China responds')
#         game_over()
#     elif selection == 'n':
#         print('You do nothing')
#         current_scenario += 1
#     elif selection == 'd':
#         print('You deliberate with you cabinet')
#         current_scenario += 1


def make_decision():
    """
    Input validation. Checks for a y n or d input.
    Keeps user in while loop until correct input is used.
    """
    decision = ''
    while decision != 'y' and decision != 'n' and decision != 'd':
        print('Please make a valid decision\n')
        decision = input(
            'What is your decision?\n'
            'y for yes\n'
            'n for no\n'
            'd for deliberate\n').lower()
    return decision


def first_decision():
    """
    First decision function in Taiwan game.
    Determines outcome of the first decision the user makes.
    """
    clear()
    print('China flys fighter jets over Taipei regularly')
    print('Your defence minister urges you to retaliate.')
    print('Will you follow this advice?\n')
    choice = make_decision()
    if choice in ['d', 'n']:
        print('Correct!')
        time.sleep(2)
        second_decision()
    else:
        time.sleep(2)
        print('Game Over!')
        # Game over function here
    # check_decision1(choice)


def second_decision():
    """
    Second decision function in Taiwan game.
    Determines outcome of the second decision the user makes.
    """
    clear()
    print('You do nothing')
    print('China intensifies its flyovers and invades Kinmen Island')
    print('Your foreign minister suggests you let China have the island')
    print('What will you do?\n')
    choice = make_decision()
    # check_decision2(choice)
    if choice in ['d', 'n']:
        print('Correct!')
        time.sleep(2)
        if choice == 'n':
            fourth_decision()
        else:
            third_decision()
    else:
        time.sleep(2)
        print('Game Over!')
        # Game over function here


def third_decision():
    """
    Third decision function in Taiwan game.
    Determines outcome of the third decision the user makes.
    """
    clear()
    print('You are reluctant to fight and hesitate')
    print('Japan and Korea then join the fight on your side')
    print('You lose the island but gain allies')
    print('Your defence minister asks you to appeal to the USA')
    print('Do you appeal to the USA?\n')
    choice = make_decision()
    # check_decision3(choice)
    if choice in ['y', 'd']:
        print('You contact the US')
        time.sleep(2)
        if choice == 'y':
            fifth_decision()
        else:
            fourth_decision()
    else:
        time.sleep(2)
        print('Game Over!')
        # Game over function here


def fourth_decision():
    """
    Fourth decision function in Taiwan game.
    Determines outcome of the fourth decision the user makes.
    """
    clear()
    print('You fight China')
    print("But the odds aren't in your favour")
    print('PLA takes Kinmen Island')
    print('Your vice president urges you to send for assitance from the USA')
    print('Do you send a special envoy to the US?\n')
    choice = make_decision()
    # check_decision4(choice)
    if choice == 'y':
        fifth_decision()
    else:
        time.sleep(2)
        print('Game Over!')
        # Game over function here


def fifth_decision():
    """
    Fifth decision function in Taiwan game.
    Determines outcome of the fifth decision the user makes.
    """
    clear()
    print('US responds and promises to come to your defence')
    print('But this will take time.')
    print('Your defence minister says they have a plan to strike')
    print('Bejing with a lethal airstrike to take out the Chairman')
    print('Do you carry out this strike?\n')
    choice = make_decision()
    # check_decision5(choice)
    if choice in ['d', 'n']:
        time.sleep(2)
        print('You Win!')
    else:
        time.sleep(2)
        print('Game Over!')
        # Game over function here

"""
Play again loop to keep user within the game.
"""
play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    first_decision()
    play_again = input('Do you want to play again? (yes or y to play again): ')
