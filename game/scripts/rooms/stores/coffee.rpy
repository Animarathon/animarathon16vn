# Animarathon XVI: Operation Ohio Kopi Tiam
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

label coffee:

    play music water fadeout 1

    scene bg coffee shop
    with dissolve

    if kopi_first == False:

        show karen kopi happy
        with easeinright

        kk "Ayo, bodoh! Haven't seen you since finals last semester lah."

        hide karen kopi
        with easeoutright

        $ kopi_first = True

        show ann normal
        with easeinleft

        a "Hey K. No more all nighters for me in lah lah land. That said, can I get a kopi?"

        hide ann
        with easeoutleft

        show karen kopi happy
        with easeinright

        kk "Can lah!"

        hide karen kopi
        with easeoutright

    if kopi_first == True:

        show karen kopi happy
        with easeinright

        kk "Can get you a kopi boss?"

        hide karen kopi
        with easeoutright

    jump coffee_menu

label coffee_menu:

    menu:

        ann_thoughts "I have $[money]."

        "Kopi-o ($[coffee_price])" if (money >= coffee_price):

            python:
                energy += 50
                money -= coffee_price

            show karen kopi pour
            with easeinright

            kk "Kopi-o lah!~"

            hide karen kopi
            with easeoutright

        "{s}Kopi-o{/s} ($[coffee_price])" if (money < coffee_price):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Teh ($[teh_price])" if (money >= teh_price):

            python:
                energy += 50
                money -= teh_price

            show karen kopi pour
            with easeinright

            kk "Teh lah!~"

            hide karen kopi
            with easeoutright

        "{s}Teh{/s} ($[teh_price])" if (money < teh_price):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Kaya Waffle ($[waffle_price])" if (money >= waffle_price):

            python:
                energy += 50
                hunger -= 50
                money -= waffle_price

            show karen kopi pour
            with easeinright

            kk "Kapster songkok pours waffle batter too lah!~"

            hide karen kopi
            with easeoutright

        "{s}Kaya Waffle{/s} ($[waffle_price])" if (money < waffle_price):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass


        "It's time to leave":

            show karen kopi normal
            with easeinright

            kk "Ayo bodoh, come back soon lah!~"

            hide karen kopi
            with easeoutright

            return

    jump coffee_menu
