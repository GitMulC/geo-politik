import time
# from run import make_decision, clear, repeat_game
import helpers


def game1_first_decision():
    """
    First decision function in Taiwan game/game1.
    Determines outcome of the first decision the user makes.
    """
    helpers.clear()
    print(
        'On the 100th anniversary of the Chinese Communist Party\n'
        'China announces its intent to regain lost territory.\n'
        "This puts the island nation of Taiwan in the China's crosshairs.\n"
        'China begins intimidating Taiwan by flying military jets\n'
        'over Taiwan, to intimidate and wear Taiwan down militarily.\n'
        'In response your defence minister urges you to respond with force.\n'
        'Will you follow this advice?\n'
        )
    choice = helpers.make_decision()
    helpers.clear()
    if choice in ['d', 'n']:
        print(
            'You refuse to use any force to resolve the issue\n'
            'You wait it out and see what China plans to do next.\n'
        )
        time.sleep(5)
        input('\nPress enter to continue')
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
        helpers.repeat_game()
        # Game over function here


def game1_second_decision():
    """
    Second decision function in Taiwan game/game1.
    Determines outcome of the second decision the user makes.
    """
    helpers.clear()
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
    choice = helpers.make_decision()
    helpers.clear()
    if choice in ['d', 'n']:
        if choice == 'n':
            print('You decide to meet the Chinese in open war.\n')
            time.sleep(5)
            input('\nPress enter to continue')
            game1_fourth_decision()
        else:
            print('You weigh out your options and again, you wait it out.\n')
            time.sleep(5)
            input('\nPress enter to continue')
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
        helpers.repeat_game()
        # Game over function here


def game1_third_decision():
    """
    Third decision function in Taiwan game/game1.
    Determines outcome of the third decision the user makes.
    """
    helpers.clear()
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
    choice = helpers.make_decision()
    helpers.clear()
    if choice in ['y', 'd']:
        if choice == 'y':
            print(
                'You reach out to the US and request immediate\n'
                'assitance.\n'
            )
            time.sleep(5)
            input('\nPress enter to continue')
            game1_fifth_decision()
        else:
            print(
                'You mobilize your troops and begin fighting China.\n'
                "You think that your coalition's willingness to act\n"
                'against China will be enough to deter it from\n'
                'invading Taiwan.\n'
            )
            time.sleep(5)
            input('\nPress enter to continue')
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
        helpers.repeat_game()
        # Game over function here


def game1_fourth_decision():
    """
    Fourth decision function in Taiwan game.
    Determines outcome of the fourth decision the user makes.
    """
    helpers.clear()
    print(
        'Your fight with China is in vain. You know you cannot win\n'
        'short term or long term.\n'
        'Your vice president urges you to ask the US for help.\n'
        'Do you send a special envoy to the US?\n'
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'y':
        print(
            'You contact the US who respond and assure you that they will\n'
            'support Taiwan in this war.\n'
        )
        time.sleep(5)
        input('\nPress enter to continue')
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
        helpers.repeat_game()
        # Game over function here


def game1_fifth_decision():
    """
    Fifth decision function in Taiwan game.
    Determines outcome of the fifth decision the user makes.
    """
    helpers.clear()
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
    choice = helpers.make_decision()
    helpers.clear()
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
        helpers.repeat_game()
        # Game over function here
