# import os
# from os import system, name
# from taiwan import game1_first_decision
# from poland import game2_first_decision
# from helpers import *
import helpers
import taiwan
import poland


# def clear():
#     """
#     Clear function to clean-up the terminal so things don't get messy.
#     """
#     os.system("cls" if os.name == "nt" else "clear")


# def menu_option():
#     """
#     Main menu selection function.
#     Uses while loop to make sure user selects one of the provided options.
#     """
#     selection = ''
#     while selection != 'a' and selection != 'p' and selection != 'q':
#         print('Please select one option')
#         selection = input(
#             'a for about\n'
#             'p for play\n'
#             'q for quit\n').lower()
#     return selection


# def gamemode():
#     """
#     Gamemode selection function.
#     Uses while loop to make sure user selects one of the provided options.
#     """
#     gamechoice = ''
#     while gamechoice != '1' and gamechoice != '2' and gamechoice != '3':
#         print('Please select one option')
#         gamechoice = input(
#             '1 for Taiwan scenario\n'
#             '2 for Poland scenario\n'
#             '3 for Mongolia scenario\n'
#         )
#     return gamechoice


# def main_menu():
#     """
#     Main menu function.
#     Brings up the main menu or opening screen
#     that lets the player select from a range of options
#     """
#     clear()
#     print(
#         'Welcome to GeoPolitik, the text based Geo-political game!\n'
#         'Navigate through the world of geography & politics\n'
#         'to overcome your regions geo-political challenges\n'
#         'Select an option below to start:\n'
#         'About >> a\n'
#         'Play >> p\n'
#         'Quit >> q\n'
#     )
#     option = menu_option()
#     if option == 'p':
#         clear()
#         print(
#             "Please select which scenario you'd like to play:\n"
#             '1 >> Taiwan\n'
#             '2 >> Poland\n'
#             '3 >> Mongolia\n'
#         )
#         gameselect = gamemode()
#         if gameselect == '1':
#             taiwan.game1_first_decision()
#         elif gameselect == '2':
#             poland.game2_first_decision()
#         elif gameselect == '3':
#             game3_first_decision()
#     # elif option == 'a':
#     #     about_page()
#     # else:
#     #     quit()


# def make_decision():
#     """
#     Input validation. Checks for a y n or d input.
#     Keeps user in while loop until correct input is used.
#     """
#     decision = ''
#     while decision != 'y' and decision != 'n' and decision != 'd':
#         print('Please make a valid decision\n')
#         decision = input(
#             'What is your decision?\n'
#             'y for yes\n'
#             'n for no\n'
#             'd for deliberate\n').lower()
#     return decision


# def repeat_game():
#     # play_again = 'yes'
#     """
#     Play again loop to keep user within the game.
#     """
#     while True:
#         play_again = input('Do you want to play again? (y or n): ').lower()
#         if play_again == 'y':
#             main_menu()
#             break
#         else:
#             print('Invalid option, please try again.')

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



if __name__ == '__main__':
    helpers.main_menu()
