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
        'Much of the factories and supply chains it promised to build all\n'
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


def mog_fourth_decision():
    """
    Fourth decision function in Mongolia game/mog.
    Determines outcome of the fourth decision the user makes.
    """
    helpers.clear()
    print(
        'As you remain indecisive on the Russian trade deal, tensions\n'
        'between China and Russia flair up! They both compete with each\n'
        'other fiercely. Russia sweetens the deal, offering open borders and\n'
        'and access to natural gas pipelines within Russia! China realising\n'
        'they may lose you to the Russians, threaten to cut all economic\n'
        'ties with you (knowing full well it could destroy your economy)\n'
        'if you accept the Russian offer. Both seek greater influence with\n'
        'you! Your economic branch informs you that China needs the rare\n'
        'minerals from Mongolia, and that cutting economic ties with you is\n'
        'just a bluff to prevent you from becoming closer with Russia.\n'
        'Will you accept the Russians trade agreement?\n'
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'y':
        print(
            "You call China's bluff and progress with the Russian deal\n"
            'Your guess was correct! China expresses disappointment but does\n'
            'not cut economic ties. Russia assists in building up Mongolia!\n'
            "Mongolia is on it's way to becoming a strong regional power!\n"
        )
        time.sleep(2)
        print('You Win!')
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


def mog_fifth_decision():
    """
    Fifth decision function in Mongolia game/mog.
    Determines outcome of the fifth decision the user makes.
    """
    helpers.clear()
    print(
        'China grows frustrated with you as you accept the Russian trade\n'
        'deal. For fear of losing all access to the mines, China lashes out\n'
        'and demands further access to all the rare mineral mines in\n'
        'Mongolia! Your police force inform you that armed Chinese soldiers\n'
        'have now begun to sneak over the border and into the mining areas.\n'
        'You see a crisis on the horizon.\n'
        "Do you grant China's request?\n"
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'n':
        print(
            'You stand firm and order your border patrol and police to \n'
            'arrest any armed personnel in the mining areas. China denies\n'
            'sending armed people into Mongolia, but a UN commission refutes\n'
            "this claim. China is ordered to expel all it's citizens from\n"
            'Ömnögovi. Backed into a corner, China agrees and still agrees\n'
            'to trade for your rare minerals!\n'
        )
        time.sleep(2)
        print('You Win!')
    else:
        print(
            'You fear armed clashes between your people and Chinese\n'
            'insurgents and so you grant China more access. They slowly\n'
            'wither your rare mineral supplies, leaving none for Russia or\n'
            'other prospective countries. You are in financial ruins and are\n'
            'under the influence of the Chinese!\n'
        )
        time.sleep(2)
        print('Game Over!')
        helpers.repeat_game()