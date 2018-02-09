# Animarathon XVI: Operation Ohio Artist Alley: Pachinko Jester
# 
# Copyright (C) 2018  Anime In Northwest Ohio
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author :      Maxwell Paul Brickner
# Maintainer :  Maxwell Paul Brickner

label artist_pachinko_jester:

    #  ____            _     _       _               _           _            
    # |  _ \ __ _  ___| |__ (_)_ __ | | _____       | | ___  ___| |_ ___ _ __
    # | |_) / _` |/ __| '_ \| | '_ \| |/ / _ \   _  | |/ _ \/ __| __/ _ \ '__|
    # |  __/ (_| | (__| | | | | | | |   < (_) | | |_| |  __/\__ \ ||  __/ |   
    # |_|   \__,_|\___|_| |_|_|_| |_|_|\_\___/   \___/ \___||___/\__\___|_|   

    show pachinko jester
    with easeinright

    if pachinko_jester_known == False:

        pj "{b}Du~Fu~Hu{/b} they call me the [pj] I suppose?"

        $ pachinko_jester_known = False

    if pachinko_jester_known == True:

        pj "{b}Du;Fu;Hu{/b} What can I do for you?"

    hide pachinko jester
    with easeoutright

    jump sell_balls_menu

label sell_balls_menu:

    # The reason Ann can't sell all her pachinko balls (Unlike spending money)
    # Is because she would be kicked out for doing so.

    menu:

        ann_thoughts "I have $[money] and [pachinko_balls] Pachinko balls."

        "Sell 1000 pachinko balls for $10 {b}$0.010 a ball!{/b}" if (pachinko_balls > 1000):

            python:
                pachinko_balls -= 1000
                money += 10

            show pachinko jester
            with easeinright

            pj "{b}Du.Fu?Hu!{/b} Thank you! Pachi Get!"

            hide pachinko jester
            with easeoutright

        "{s}Sell 1000 pachinko balls for $10 {b}$0.010 a ball!{/b}{/s}" if (pachinko_balls <= 1000):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Sell 2000 pachinko balls for $20 {b}$0.010 a ball!{/b}" if (pachinko_balls > 2000):

            python:
                pachinko_balls -= 2000
                money += 20

            show pachinko jester
            with easeinright

            pj "{b}Du!Fu?Hu!{/b} Thank you! Pachi Boom!"

            hide pachinko jester
            with easeoutright

        "{s}Sell 2000 pachinko balls for $20 {b}$0.010 a ball!{/b}{/s}" if (pachinko_balls <= 2000):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Sell 9001 pachinko balls for $100 {b}$0.011 a ball!{/b}" if (pachinko_balls > 9001):

            python:
                pachinko_balls -= 9001
                money += 100

            show pachinko jester
            with easeinright

            pj "{b}Du!Fu!Hu!{/b} Thank you! Pachi Blossom!"

            hide pachinko jester
            with easeoutright

        "{s}Sell 9001 pachinko balls for $100 {b}$0.011 a ball!{/b}{/s}" if (pachinko_balls <= 9001):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass


        "It's time to leave":

            show pachinko jester
            with easeinright

            pj "{b}Du&Fu&Hu{/b} I'll see you!"

            hide pachinko jester
            with easeoutright

            return

    jump sell_balls_menu
