# Animarathon XVI: Operation Ohio Artist Alley: Ska
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

label artist_ska:

    show ska ecchi
    with easeinright

    if ska_ecchi_story == False:

        se "Name's Ska Ecchi. You want some pachinko balls or what?"

    if ska_ecchi_story == True:

        se "You didn't tell [fs] right?"

    hide ska ecchi
    with easeoutright

    jump buy_balls_menu

label buy_balls_menu:

    menu:

        ann_thoughts "I have $[money] and [pachinko_balls] Pachinko balls."

        "Buy 1000 pachinko balls for $10 {b}$0.010 a ball!{/b}" if (money >= 10):

            python:
                pachinko_balls += 1000
                money -= 10

            show ska ecchi
            with easeinright

            se "I'll see you soon cheapskate!"

            hide ska ecchi
            with easeoutright

        "{s}Buy 1000 pachinko balls for $10 {b}$0.010 a ball!{/b}{/s}" if (money < 10):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Buy 2600 pachinko balls for $20 {b}$0.008 a ball!{/b}" if (money >= 20):

            python:
                pachinko_balls += 2600
                money -= 20

            show ska ecchi
            with easeinright

            se "Pleasure doing business with you!"

            hide ska ecchi
            with easeoutright

        "{s}Buy 2600 pachinko balls for $20 {b}$0.008 a ball!{/b}{/s}" if (money < 20):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Buy 9001 pachinko balls for $50 {b}$0.006 a ball! BEST VALUE{/b}" if (money >= 50):

            python:
                pachinko_balls += 9001
                money -= 50

            show ska ecchi
            with easeinright

            se "Thanks a lot big spender! Whales like you shouldn't be strangers!"

            hide ska ecchi
            with easeoutright

        "{s}Buy 9001 pachinko balls for $50 {b}$0.006 a ball! BEST VALUE{/b}{/s}" if (money < 50):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Ask for life story" if (ska_ecchi_story == False):

            show ska ecchi
            with easeinright

            se "Listen snitch, no questions. I'll give you a deal so shut up!"

            hide ska ecchi
            with easeoutright

            $ ska_ecchi_story = True

        "Ask for freebie ball." if (ska_ecchi_story == True):

            show ska ecchi
            with easeinright

            $ pachinko_balls += 1

            se "No questions, no snitching, and I'll keep the goods coming."

            hide ska ecchi
            with easeoutright

        "It's time to leave":

            show ska ecchi
            with easeinright

            se "Come back with more cash!"

            hide ska ecchi
            with easeoutright

            return

    jump buy_balls_menu
