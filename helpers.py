import os
from os import system, name
import time
import taiwan
import poland
import mongolia


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def menu_option():
    """
    Main menu selection function.
    Uses while loop to make sure user selects one of the provided options.
    """
    selection = ''
    while selection != 'a' and selection != 'p' and selection != 'q':
        print('Please select one option')
        selection = input(
            'a for about\n'
            'p for play\n'
            'q for quit\n').lower()
    return selection


def gamemode():
    """
    Gamemode selection function.
    Uses while loop to make sure user selects one of the provided options.
    """
    gamechoice = ''
    while gamechoice != '1' and gamechoice != '2' and gamechoice != '3':
        clear()
        print('Please select one option to play:')
        gamechoice = input(
            '1 for Taiwan scenario\n'
            '2 for Poland scenario\n'
            '3 for Mongolia scenario\n'
        )
    return gamechoice


def main_menu():
    """
    Main menu function.
    Brings up the main menu or opening screen
    that lets the player select from a range of options
    """
    clear()
    print(
        'Welcome to GeoPolitik, the text based Geo-political game!\n'
        'Navigate through the world of geography & politics\n'
        'to overcome your regions geo-political challenges\n'
        'Select an option below to start:\n'
        'About >> a\n'
        'Play >> p\n'
        'Quit >> q\n'
    )
    option = menu_option()
    if option == 'p':
        clear()
        print(
            "Please select which scenario you'd like to play:\n"
            '1 >> Taiwan\n'
            '2 >> Poland\n'
            '3 >> Mongolia\n'
        )
        gameselect = gamemode()
        if gameselect == '1':
            taiwan.tw_first_decision()
        elif gameselect == '2':
            poland.pol_first_decision()
        elif gameselect == '3':
            mongolia.mog_first_decision()
    elif option == 'a':
        clear()
        print(
            'You choose 1 of 3 scenarios to play:\n'
            '1 >> Taiwan struggling with an agressive China\n'
            '2 >> Poland facing down a Soviet style Russia\n'
            '3 >> Mongolia between 2 reginal superpowers; Russia & China\n'
            'Use the keys:\n'
            'y for yes\n'
            'n for no\n'
            'd for deliberate\n'
            'to navigate through your scenarios and survive the\n'
            'geo-political challenges of your region!'
        )
        time.sleep(3)
        input('\nPress enter to return to the Main Menu')
        main_menu()
    else:
        print(
                'Exiting game...'
            )
        time.sleep(3)


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


def repeat_game():
    """
    Play again loop to keep user within the game.
    """
    while True:
        play_again = input('Do you want to play again? (y or n): ').lower()
        if play_again == 'y':
            main_menu()
            break
        elif play_again == 'n':
            print(
                'Exiting game...'
            )
            time.sleep(3)
            exit()
        else:
            print('Invalid option, please try again.')
