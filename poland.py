import time
import helpers


def pol_first_decision():
    """
    First decision function in Poland game.
    Determines outcome of the first decision the user makes.
    """
    helpers.clear()
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
    choice = helpers.make_decision()
    helpers.clear()
    if choice in ['d', 'y']:
        if choice == 'd':
            print(
                'You decide to consult your cabinet about the matter.\n'
            )
            time.sleep(5)
            input('\nPress enter to continue')
            pol_second_decision()
        elif choice == 'y':
            print(
                'You think that mobilizing ASAP to the east is your best\n'
                'option to deter the Russians.\n'
            )
            time.sleep(5)
            input('\nPress enter to continue')
            pol_third_decision()
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
            helpers.repeat_game()


def pol_second_decision():
    """
    Second decision function in Poland game.
    Determines outcome of the second decision the user makes.
    """
    helpers.clear()
    print(
        'Your cabinet advises you to contact Europe and the US for\n'
        'assistance. You then consult the US president and the\n'
        'European parliment on what to do. They both tell you to\n'
        'deploy your army in small numbers and grdually. You are\n'
        'fearful of a Russian response to your deployment.\n'
        'Do you listen to your allies advice?'
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'y':
        print(
            'You listen to the council of your allies and slowly build up\n'
            'troops on your eastern border.\n'
        )
        time.sleep(5)
        input('\nPress enter to continue')
        pol_third_decision()
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
    helpers.repeat_game()


def pol_third_decision():
    """
    Third decision function in Poland game.
    Determines outcome of the third decision the user makes.
    """
    helpers.clear()
    print(
        'You deploy your troops along the eastern border to shore up\n'
        'your defences. In response Russia sends troops into Ukraine\n'
        'and Lithuania. You recieve a private communiqué from the Russian\n'
        'president himself. He tells you to cease your aggressive actions\n'
        'and pull your troops away from the sovreign borders of Ukraine and\n'
        'Lithuania or face dire consequencecs.\n'
        'Do you give into Russian demands?\n'
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice in ['d', 'n']:
        print(
            'You ignore Russia, you know giving into their demands\n'
            'will only weaken your already tenuous postion.\n'
        )
        time.sleep(5)
        input('\nPress enter to continue')
        pol_fourth_decision()
    else:
        print(
            'You retreat with your tail between your legs and withdraw\n'
            'all defence forces on the border. Russia acts with impunity\n'
            'in eastern Europe and sabotages Polish elections, judical\n'
            'system and finally tanks its economy leaving it open for\n'
            'Russian occupation!\n'
        )
        time.sleep(5)
        print('Game Over!')
        helpers.repeat_game()


def pol_fourth_decision():
    """
    Fourth decision function in Poland game.
    Determines outcome of the fourth decision the user makes.
    """
    helpers.clear()
    print(
        'You leak the communiqué to the public. The Polish population is\n'
        'outraged! Your European and American allies rally around you as\n'
        'they begin to move their forces towards Poland. French and\n'
        'German troops start pouring into Poland. The US mobilizes its\n'
        'Atlantic fleet. Feeling the pressure, Russia imposes a no-fly\n'
        'zone over Polands eastern borders. Russian spy planes begin\n'
        'tracking troop movements, followed by Russian fighter jets\n'
        'excursions deep into Polish territory. Your on the ground\n'
        'generals inform you that they can easily down these planes with\n'
        'your permission.\n'
        'Do you give the go ahead to your generals?\n'
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'n':
        print(
            'You infrom your generals that the rules of engagement do not\n'
            'allow you to strike first. Your decision to show restraint pays\n'
            'off as the international community by and large demands Russian\n'
            'withdrawl from the region. Fierce and violent protests flair up\n'
            'in Ukraine and Lithuania and Russian troops have to be summoned\n'
            'to quell the civil unrest. US and Europe impose punative\n'
            'sanctions that soon crush the Russian economy. Russian\n'
            'occupation waivers and soon recedes back to Moscow!\n'
        )
        time.sleep(5)
        print('You Win!')
    elif choice == 'd':
        print(
            'You tell your generals to hold off and wait for the right\n'
            'moment to engage Russia.\n'
        )
        time.sleep(5)
        input('\nPress enter to continue')
        pol_fifth_decision()
    else:
        print(
            'You give the go ahead. As soon as you down a Russian aircraft\n'
            'Russian troops engage in open conflict with you before your\n'
            'your allies can arrive and respond. They do eventually arrive\n'
            'to relieve you and begin to push the Russians back. Russian\n'
            'troops retreat to the Russian border. Fearing an invasion the\n'
            'Russian high command authorizes a nuclear strike! the world\n'
            'lies decimated after the nukes have landed!'
        )
        time.sleep(5)
        print('Game Over!')
        helpers.repeat_game()


def pol_fifth_decision():
    """
    Fifth decision function in Poland game.
    Determines outcome of the fifth decision the user makes.
    """
    helpers.clear()
    print(
        'The right moment never arrives, but nevertheless you stand firm\n'
        'in the face of an occupying force. As French and German troops\n'
        'arrive Russia begins to cool off and wind down the excursions\n'
        'and threats. However, Russia shuts down its natural gas pipelines\n'
        'going into Poland. This source of energy is vital to Polands\n'
        'survival! You want to involve America and request it put boots\n'
        'on the ground in Poland. Your cabinet warns you further\n'
        'intervention by western allies may provoke Russia to retaliate\n'
        'with force.\n'
        'Do you ask for US troops in Poland?\n'
    )
    choice = helpers.make_decision()
    helpers.clear()
    if choice == 'y':
        print(
            'You relay to the US ambassador that military intervention\n'
            'by the US is urgently needed. America honours its NATO\n'
            'allegiance to Poland and moves in battalions to the country\n'
            'The US Atlantic fleet imposes a blockade of all Russian\n'
            'in the Baltic sea. Soon Russian bases and puppets in eastern\n'
            'Europe crumble. Fierce and violent protests flair up\n'
            'in Ukraine and Lithuania, and Russian troops have to be called\n'
            'to quell the civil unrest. US and Europe impose punative\n'
            'sanctions that soon crush the Russian economy. Russian\n'
            'aggression waivers and soon recedes back to Moscow!\n'
        )
        time.sleep(5)
        print('You Win!')
    else:
        print(
            'You fear angering Russia and so you refuse to contact the US\n'
            'as there is no invasion so far. But Russia has already begun\n'
            'its subversion of Polish democracy. Elections are rigged,\n'
            'a terrorist attack occurs in Warsaw with suspected Russian\n'
            'involvement. French and German troops grow restless and soon\n'
            'pull out for fear of Russian retaliation at home. Alone\n'
            'against Russia you sue for peace and sign unfavourable treaty\n'
            'after unfavourable treaty and are soon under the Russian\n'
            'umbrella!\n'
        )
        time.sleep(5)
        print('Game Over!')
        helpers.repeat_game()
