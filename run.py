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
        print('Please select one option')
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
            game1_first_decision()
        elif gameselect == '2':
            game2_first_decision()
        elif gameselect == '3':
            game3_first_decision()
    # elif option == 'a':
    #     about_page()
    # else:
    #     quit()


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


def game1_first_decision():
    """
    First decision function in Taiwan game/game1.
    Determines outcome of the first decision the user makes.
    """
    clear()
    print(
        'On the 100th anniversary of the Chinese Communist Party\n'
        'China announces its intent to regain lost territory.\n'
        "This puts the island nation of Taiwan in the China's crosshairs.\n"
        'China begins intimidating Taiwan by flying military jets\n'
        'over Taiwan, to intimidate and wear Taiwan down militarily.\n'
        'In response your defence minister urges you to respond with force.\n'
        'Will you follow this advice?\n'
        )
    choice = make_decision()
    if choice in ['d', 'n']:
        print(
            'You refuse to use any force to resolve the issue\n'
            'You wait it out and see what China plans to do next.\n'
        )
        time.sleep(5)
        game1_second_decision()
    else:
        print(
            'You retaliate and shoot down a Chinese fighter jet over Taiwan.\n'
            "China has found it's excuse to invade Taiwan and reclaim\n"
            'what they see as their territory!\n'
            'The small Taiwanese military is no match for the sheer size\n'
            'of the Chinese army and Taiwan is quickly overrun!\n'
        )
        time.sleep(2)
        print('Game Over!')
        # Game over function here


def game1_second_decision():
    """
    Second decision function in Taiwan game/game1.
    Determines outcome of the second decision the user makes.
    """
    clear()
    print(
        'China intensifies its flyovers over Taipei. Realizing that Taiwan\n'
        'will not respond with force, the Chinese government decides to\n'
        'amass troops near Kinmen island in preparation for an invasion.\n'
        'As Kinmen island is part of Taiwan, you immediately condemn this\n'
        'act and draw attention to it on the international stage.\n'
        'Your intelligence agency says an invasion is imminent and with\n'
        'little to no military presence in Kinmen island, you know that it\n'
        'be taken swiftly by the Chinese army. You know you cannot win.\n'
        'You assemble your government and ask for options. Aggressive force\n'
        'will only provoke the Chinese, so this is not an option.\n'
        'Your foreign minister suggests you let China have the island to\n'
        'descalate the situation and prevent a full scale war with China.\n'
        'Do you agree with your foreign minister?\n'
        )
    choice = make_decision()
    if choice in ['d', 'n']:
        if choice == 'n':
            print('You decide to meet the Chinese in open war.\n')
            time.sleep(5)
            game1_fourth_decision()
        else:
            print('You weigh out your options and again, you wait it out.\n')
            time.sleep(5)
            game1_third_decision()
    else:
        print(
            'You evacuate the island leaving it open for Chinese occupations\n'
            'Sensing weakness, China invades Taiwan feeling confident\n'
            'that Taiwan will be too slow to respond. With a lack of\n'
            'international will to support it, Taiwan falls to China.\n'
            )
        time.sleep(5)
        print('Game Over!')
        # Game over function here


def game1_third_decision():
    """
    Third decision function in Taiwan game/game1.
    Determines outcome of the third decision the user makes.
    """
    clear()
    print(
        'While deliberating your allies in the region\n'
        'Japan and Korea assure you they will assist you should China invade\n'
        'Kinmen island. However, soon after this declaration, China invades\n'
        'Kinmen. Your local forces offer little resistance and the island is\n'
        'quickly taken by China. Your allies tell you they need time to\n'
        'mobilize and they recommend you ask the USA for assitance.\n'
        'Your defence minister reitarates this and says Taiwan will not last\n'
        'long if China invades the island of Taiwan.\n'
        'Do you appeal to the USA?\n'
        )
    choice = make_decision()
    if choice in ['y', 'd']:
        if choice == 'y':
            print(
                'You reach out to the US and request immediate\n'
                'assitance.\n'
            )
            time.sleep(5)
            game1_fifth_decision()
        else:
            print(
                'You mobilize your troops and begin fighting China.\n'
                "You think that your coalition's willingness to act\n"
                'against China will be enough to deter it from\n'
                'invading Taiwan.\n'
            )
            time.sleep(5)
            game1_fourth_decision()
    else:
        print(
            'You refuse to ask for US assitance and confidently\n'
            'face China on the battlefield. Upon hearing this Japan\n'
            'and Korea abandon you knowing full well without the US,\n'
            'defeat is assured. You quickly surrender and\n'
            'concede to Chinas demands\n'
        )
        time.sleep(5)
        print('Game Over!')
        # Game over function here


def game1_fourth_decision():
    """
    Fourth decision function in Taiwan game.
    Determines outcome of the fourth decision the user makes.
    """
    clear()
    print(
        'Your fight with China is in vain. You know you cannot win\n'
        'short term or long term.\n'
        'Your vice president urges you to ask the US for help.\n'
        'Do you send a special envoy to the US?\n'
    )
    choice = make_decision()
    if choice == 'y':
        print(
            'You contact the US who respond and assure you that they will\n'
            'support Taiwan in this war.\n'
        )
        time.sleep(5)
        game1_fifth_decision()
    else:
        print(
            'You refuse to ask for US assitance and confidently\n'
            'face China on the battlefield. Upon hearing this Japan\n'
            'and Korea abandon you knowing full well without the US,\n'
            'defeat is assured. You quickly surrender and\n'
            'concede to Chinas demands\n'
        )
        time.sleep(5)
        print('Game Over!')
        # Game over function here


def game1_fifth_decision():
    """
    Fifth decision function in Taiwan game.
    Determines outcome of the fifth decision the user makes.
    """
    clear()
    print(
        'The US assembles its Pacific battlegroup and makes its way towards\n'
        'Taiwan. In the meantime China is keeping the pressure on. Daily\n'
        'airstrikes hit Taiwanese citizens and many civilians are killed\n'
        'The international community pivots to defending Taiwan and condemns\n'
        'China for its hostility. But only th US is close enough to prevent\n'
        "a fullscale invasion of Taiwan, but they won't arrive for 2 more\n"
        'weeks. Your defence minister lays out a military response to catch\n'
        'the Chinese off guard and stall them until the US arrives\n'
        'The plan involves stealth jets to strike major militray targets\n'
        'and the costal cities in mainland China. It also involves an\n'
        'airstrike on Bejing itself to take out Chinese military command.\n'
        'Your government is split 50:50 on whether to enact this plan.\n'
        'Do you carry out this strike?\n'
    )
    choice = make_decision()
    if choice in ['d', 'n']:
        print(
            'You refuse to act aggressively. Your defence forces and allies\n'
            'stall the Chinese long enough for the US to arrive and stave\n'
            'and invasion of Taiwan! China capitulates and signs a peace\n'
            'deal mediated by the US.\n'
        )
        time.sleep(5)
        print('You Win!')
    else:
        print(
            'You decide to give China a taste of its own medicine.\n'
            'The plan goes ahead. Only 50% of the targets are hit\n'
            "And you've lost 60% of the men and aircraft you sent.\n"
            'The strike on Bejing fails aswell and rallies the Chinese\n'
            'public against you. They demand Taiwanese blood in return\n'
            "China is outraged that it's leaders were targeted and\n"
            'carries out a nuclear strike in retaliation\n'
        )
        time.sleep(5)
        print('Game Over!')
        # Game over function here


def game2_first_decision():
    """
    First decision function in Poland game.
    Determines outcome of the first decision the user makes.
    """
    clear()
    print(
        'In eastern Europe, Russia is flexing its military muscles\n'
        'A few months ago Ukraine was conquered by Russia and now the\n'
        'the Baltic states have been annexed by Russia. The Iron Curtain\n'
        'seems to be coming down again! As the Polish president you watch\n'
        'these events unfurl from a distance, but with Russian troops\n'
        "knocking at your eastern border, you realize it's time to take\n"
        'action. You think that deploying your army across your eastern\n'
        'border is the best course of action\n'
        'Will you follow through with this?\n'
    )
    choice = make_decision()
    if choice in ['d', 'y']:
        if choice == 'd':
            print(
                'You decide to consult your cabinet about the matter.\n'
            )
            time.sleep(5)
            game2_second_decision()
        elif choice == 'y':
            print(
                'You think that mobilizing ASAP to the east is your best\n'
                'option to deter the Russians.\n'
            )
            time.sleep(5)
            game2_third_decision()
        else:
            print(
                'You decide against deploying any serious force to the east\n'
                'which Russia takes note of! They begin to accuse Poland of\n'
                'incursions into Lithuanian territory. These false\n'
                'accusationsare what Russia use as their excuse to invade.\n'
                'Within a days Warsaw falls and Poland falls under the new\n'
                'Iron Curtain!\n'
            )
            time.sleep(5)
            print('Game Over!')


def game2_second_decision():
    """
    Second decision function in Poland game.
    Determines outcome of the second decision the user makes.
    """
    clear()
    print(
        'Your cabinet advises you to contact Europe and the US for\n'
        'assistance. You then consult the US president and the\n'
        'European parliment on what to do. They both tell you to\n'
        'deploy your army in small numbers and grdually. You are\n'
        'fearful of a Russian response to your deployment.\n'
        'Do you listen to your allies advice?'
    )
    choice = make_decision()
    if choice == 'y':
        print(
            'You listen to the council of your allies and slowly build up\n'
            'troops on your eastern border.\n'
        )
        time.sleep(5)
        game2_third_decision()
    else:
        print(
            'Your inability to act quickly proves to be your downfall.\n'
            'Eventually the Russian presence on the border is too built up\n'
            'and incursions into Polish territory begin to occur. You see\n'
            'the writing on the wall and sign a non-aggression pact with\n'
            'Russia, paving the way for Russian annexation!\n'
        )
    time.sleep(5)
    print('Game Over!')


def game2_third_decision():
    """
    Third decision function in Poland game.
    Determines outcome of the third decision the user makes.
    """
    clear()
    print(
        'You deploy your troops along the eastern border to shore up\n'
        'your defences. In response Russia sends troops into Ukraine\n'
        'and Lithuainia'
    )

play_again = 'yes'
"""
Play again loop to keep user within the game.
"""
while play_again == 'yes' or play_again == 'y':
    main_menu()
    play_again = input('Do you want to play again? (yes or y to play again): ')
