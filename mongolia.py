import time
import helpers


def mog_first_decision():
    """
    First decision function in Mongolia game/mog.
    Determines outcome of the first decision the user makes.
    """
    helpers.clear()
    print(
        'In the steppes of central Asia the Mongolian economy stagnates.\n'
        'The only thing keeping your economy above water is your trade\n'
        'agreements with your northern neighbour Russia. These agreements\n'
        'are merely a remnant of a Cold War era trade deal between 2\n'
        'previously communist nations. In todays modern world it will not\n'
        'sustain you for long! The Mongolian economy is slowly shrinking,\n'
        'and the only bargaining chip you have is your gold and copper mines\n'
        'in the Ömnögovi Province in southern Mongolia. With all of this in\n'
        'mind you turn to your other powerful southern neighbour China for\n'
        'financial assistance. Your government cautions you on any dealings\n'
        'China as they come with unforseen consequences. Additionally you\n'
        'are aware that both countries are competing for regional supremacy.\n'
        'Do you reach out to China for financial assitance?\n'
        )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'y':
        print(
            'You reach out to China, and they seem happy to do business\n'
            'Russia takes note of your request and the Kremlin speaks with\n'
            'your ambassador in Moscow, suggesting a rework of your trade\n'
            'agreements may be in order.\n'
        )
        time.sleep(1)
        input('\nPress enter to continue')
        mog_second_decision()
    else:
        print(
            'Your stubbornness to reach out for financial assistance is your\n'
            'undoing! Your economy begins to plummet and the population\n'
            'revolts. Seizing the moment, China swiftly invades the southern\n'
            'province of Ömnögovi, taking control of the rare mineral mines.\n'
            'China gains the upperhand over Russia, at the expense of the\n'
            'dissolution of Mongolia!'
        )
        time.sleep(2)
        print('Game Over!')
        helpers.repeat_game()


def mog_second_decision():
    """
    Second decision function in Mongolia game/mog.
    Determines outcome of the second decision the user makes.
    """
    helpers.clear()
    print(
        'You begin to fear the loss of ties with Russia as you come to the\n'
        'negotiating table with the Chinese. But the reality remains, you\n'
        'need strong economic ties with both nations to survive. China\n'
        'promisies a strong boost to the Mongolian economy by way of\n'
        'relocating factories and supply chains into and through Mongolia.\n'
        'the only catch is that you must allow Chinese mining companies\n'
        'access to your rare mineral mines in Ömnögovi. You need those\n'
        'minerals for trading, and Chinese access may drive prices down for\n'
        'rare minerals hurting your economy.\n'
        'Do you sign this trade deal with China?'
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'y':
        print(
            'You sign off on the trade agreement. China swiftly moves into\n'
            'Mongolia, building much of the promised infrastructure near\n'
            'near the mines. This deal may not go so well!\n'
        )
        time.sleep(2)
        input('\nPress enter to continue')
        mog_third_decision()
    elif choice == 'd':
        print(
            'You hesitate fearing the wrath of Russia! You are not sure\n'
            'about the ramifacations this may have with your relationship\n'
            'with Russia. You consult with your advisors\n'
        )
        time.sleep(2)
        input('\nPress enter to continue')
        mog_fifth_decision()
    else:
        print(
            'At the last second you back out of the trade agreement\n'
            'China are not too pleased with you! Your economy then spins\n'
            'into freefall. You turn to Russia and any other neighbour for\n'
            'for assistance, but it is too late. Unable to sustain you\n'
            'economy, your government collapses and Mongolia slips into\n'
            'disaster. Russia and China divide the ruins of Mongolia\n'
            'amoungst themselves.\n'
        )
        time.sleep(2)
        print('Game Over!')
        helpers.repeat_game()


def mog_third_decision():
    """
    Third decision function in Mongolia game/mog.
    Determines outcome of the third decision the user makes.
    """
    helpers.clear()
    print(
        'You soon realise that this trade agreement mostly benefits China.\n'
        'Much of the infrastructure that China promised it would build all\n'
        'all over Mongolia is only being built near the mines. This gives\n'
        'Mongolia only a short, temporary economic boost. Rare mineral\n'
        'plummet and as a result you economy slows its growth. Seeing their\n'
        'chance, Russia sends an envoy to Ulaanbaatar to discuss a new trade\n'
        'deal. Russia promises infrastructure country-wide and in return\n'
        'wants closer diplomatic ties along with special access your\n'
        'minerals and agricultural produce.\n'
        'Will you accept the Russians trade agreement?\n'
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'y':
        print(
            'China takes note of this counter offer by Russia, things may\n'
            'get complicated!\n'
        )
        time.sleep(2)
        input('\nPress enter to continue')
        mog_fifth_decision()
    if choice == 'd':
        print(
            'While you are greatful for the Russians counter offer, you\n'
            'remain cautious. You worry about coming between 2 superpowers!\n'
        )
        time.sleep(2)
        input('\nPress enter to continue')
        mog_fourth_decision()
    else:
        print(
            'Fearing Chinese retaliation and a possible trade war with\n'
            'Beijing you refuse the offer. But China only continues to\n'
            'take advantage of your mines. Soon you lose control of all\n'
            'your mining operations. China now dominates Mongolia through\n'
            'its economic ties with you!\n'
        )
        time.sleep(2)
        print('Game Over!')
        helpers.repeat_game()
