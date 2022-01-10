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
    input validation
    """
    decision = ''
    while decision != 'y' and decision != 'n' and decision != 'd':
        decision = input('What is your decision? (y/n/d): ')
    return decision


def check_decision1(make_decision):
    correct_decision1 = 'n'
    correct_decision2 = 'd'
    if make_decision == correct_decision1:
        print('Correct!')
        second_decision()
    elif make_decision == correct_decision2:
        print('Correct!')
        second_decision()
    else:
        print('Game Over')


def check_decision2(make_decision):
    correct_decision1 = 'n'
    correct_decision2 = 'd'
    if make_decision == correct_decision1:
        print('Correct!')
        fourth_decision()
    elif make_decision == correct_decision2:
        print('Correct!')
        third_decision()
    else:
        print('Game Over')


def check_decision3(make_decision):
    correct_decision1 = 'y'
    correct_decision2 = 'd'
    if make_decision == correct_decision1:
        print('You contact the US')
        print('Correct!')
        fifth_decision()
    elif make_decision == correct_decision2:
        print('You contact the US')
        print('but China gets wind of this and blocks communications')
        print('Correct!')
        fourth_decision()
    else:
        print('Game Over')


def check_decision4(make_decision):
    correct_decision = 'y'
    if make_decision == correct_decision:
        print('Correct!')
        fifth_decision()
    else:
        print('Game Over')


def check_decision5(make_decision):
    correct_decision1 = 'n'
    correct_decision2 = 'd'
    if make_decision == correct_decision1:
        print('Correct!')
        print('You Win!')
    elif make_decision == correct_decision2:
        print('Correct!')
        print('You Win!')
    else:
        print('Game Over')


def first_decision():
    print('China flys fighter jets over Taipei regularly')
    print('Your defence minister urges you to retaliate.')
    print('Will you follow this advice?\n')
    choice = make_decision()
    check_decision1(choice)


def second_decision():
    print('You do nothing')
    print('China intensifies its flyovers and invades Kinmen Island')
    print('Your foreign minister suggests you let China have the island')
    print('What will you do?\n')
    choice = make_decision()
    check_decision2(choice)


def third_decision():
    print('You are reluctant to fight and hesitate')
    print('Japan and Korea then join the fight on your side')
    print('You lose the island but gain allies')
    print('Your defence minister asks you to appeal to the USA')
    print('Do you appeal to the USA?\n')
    choice = make_decision()
    check_decision3(choice)


def fourth_decision():
    print('You fight China')
    print("But the odds aren't in your favour")
    print('PLA takes Kinmen Island')
    print('Your vice president urges you to send for assitance from the USA')
    print('Do you send a special envoy to the US?\n')
    choice = make_decision()
    check_decision4(choice)


def fifth_decision():
    print('US responds and promises to come to your defence')
    print('But this will take time.')
    print('Your defence minister says they have a plan to strike')
    print('Bejing with a lethal airstrike to take out the Chairman')
    print('Do you carry out this strike?\n')
    choice = make_decision()
    check_decision5(choice)


play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    first_decision()
    # second_decision()
    # third_decision()
    play_again = input('Do you want to play again? (yes or y to play again): ')
