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


menu()
