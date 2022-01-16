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
