def menu():
    """
    Runs opening menu screen on startup.
    """
    while True:
        print('Welcome to GeoPolitik, the geo-political adventure game!')
        print('Face geo-political challenges to survive as a nation.\n')
        print('About - a')
        print('Play - p')
        print('Quit - q\n')

        selection = input('Select an option: \n')

        if selection == 'a':
            print('About')
            return False
        elif selection == 'p':
            print('Play')
            return False
        elif selection == 'q':
            print('Quit')
            return False
        else:
            print('Please select a viable option.')
            return True
    return selection

    #     if menu_validate(selection):
    #         print(f'You have chosen {selection}')
    #         break
    # return selection


# def menu_validate(values):
#     """
#     Check if selection in menu is correct.
#     """
#     # if len(values) == 1:
#     #     print('Correct text!')
#     #     return True
#     # elif len(values) != 1:
#     #     print('Wrong text!')
#     #     return False
#     # elif values.isalpha():
#     #     return True
#     if
#     else:
#         return False


# menu()

current_scenario = 0

def main_game():
    """
    """
    scenario_texts = [
        'China flyovers. Defence misniter urges retaliation.',
        'Something else bad happens.\nWhat do?',
        'blah'
    ]
    while True:
        print(scenario_texts[current_scenario])
        selection = input('\nWhat will you do?\n')
        decision()


def decision(current_scenario,selection):
    if selection == 'y':
        print('You retaliate, China responds')
        game_over()
    elif selection == 'n':
        print('You do nothing')
        current_scenario += 1
    elif selection == 'd':
        print('You deliberate with you cabinet')
        current_scenario += 1