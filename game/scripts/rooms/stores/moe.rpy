# Animarathon XVI: Operation Ohio Artist Alley: Moe
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

label artist_moe:

    show moe
    with easeinright

    mo "Welcome to [mo]'s anime shop!"

    hide moe
    with easeoutright

label artist_moe_buy:

    menu:

        ann_thoughts "I have $[money] to buy merchandise."

        "Buy anime":

            show moe
            with easeinright

            mo "What anime would you like to buy?"

            hide moe
            with easeoutright

            call buy_anime

        "Buy manga":

            show moe
            with easeinright

            mo "Our manga section isn't the greatest... But I do have some..."

            hide moe
            with easeoutright

            call buy_manga

        "Buy dakimakura":

            show moe
            with easeinright

            mo "Our custom dakimakura printer... Right..."

            hide moe
            with easeoutright

            call buy_dakimakura

        "Ask for life story" if (mo_story == False):

            show moe
            with easeinright

            mo "Eh? You really wanna know? I'm researching the niche market of custom anime goods."

            hide moe
            with easeoutright

            show ann normal
            with easeinleft

            a "Why bother? You don't have a lot of competition here."

            hide ann
            with easeoutleft

            show moe
            with easeinright

            mo "Well [fs]'s antics haven't been good for business. Put an end to it, and there's $10,000 with your name on it."

            hide moe
            with easeoutright

            menu:

                ann_thoughts "$10,000 for taking down [fs] is a lot."

                "Deal":
    
                    python:
                        mo_story = True
                        mo_mission = True

                    show moe
                    with easeinright

                    mo "Good! Come back when he's been stopped."

                    hide moe
                    with easeoutright

                "Negotiate":

                    python:
                        mo_story = True
                        mo_mission = True    
                        mo_gold = True

                    show moe
                    with easeinright

                    mo "I will use my gold marker to literally write your name on the cash. Come back when he's been stopped."

                    hide moe
                    with easeoutright

                "No Deal":

                    $ mo_story = True

                    show moe
                    with easeinright

                    mo "Your call sister. If you manage to get payback, my offer stands."

                    hide moe
                    with easeoutright

        "It's time to leave":

            show moe
            with easeinright

            mo "Come back soon!"

            hide moe
            with easeoutright

            return

    jump artist_moe_buy

label buy_anime:

    menu:

        ann_thoughts "I have $[money] to buy anime."

        "[favorite_anime] Box Set ($[favorite_anime_price])" if ((money >= favorite_anime_price) and (favorite_anime_get == False)):

            python:
                money -= favorite_anime_price
                favorite_anime_get = True

            show moe
            with easeinright

            mo "Thank you for your business!"

            hide moe
            with easeoutright

        "{s}[favorite_anime] Box Set ($[favorite_anime_price]){/s}" if ((money < favorite_anime_price) and (favorite_anime_get == False)):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Don't buy anime":

            return

    jump buy_anime

label buy_manga:

    menu:

        ann_thoughts "I have $[money] to buy manga."

        "Tadpole Sensei: Adventures of Young [fs] ($[tadpole_sensei_price])" if (tadpole_sensei_manga == False):

            show moe
            with easeinright

            mo "This? You want {b}this{/b}? Take it. [fs] gave all 4000 copies to the merchants here. I'm the only official merchant."

            hide moe
            with easeoutright

            $ tadpole_sensei_manga = True

            show manga frog sensei at truecenter
            with easeinbottom

            ann_thoughts "Is this... Hand drawn?"

            hide manga frog sensei
            with easeoutbottom

            show ann happy
            with easeinleft

            a "Thank you!"

            hide ann
            with easeoutleft

            show moe
            with easeinright

            mo "No, thank you. Getting rid of these is gonna be hard."

            hide moe
            with easeoutright

        "Kawaii Calcium Kun ($[kawaii_calcium_price])" if (kawaii_calcium_manga == False):

            show moe
            with easeinright

            mo "You want {b}that{/b}? I ordered it by mistake, and it's been collecting dust for years. Take it."

            hide moe
            with easeoutright

            $ kawaii_calcium_manga = True

            show ann happy
            with easeinleft

            a "Thank you!"

            hide ann
            with easeoutleft

        "Don't buy manga":

            return

    jump buy_manga

label buy_dakimakura:

    menu:

        ann_thoughts "I have $[money] to buy dakimakuras. Who should I make a dakimakura of?"

        "[a] ($[dakimakura_price])" if ((dakimakura_ann == False) and (money >= dakimakura_price)):

            show dakimakura ann
            with easeinright

            $ dakimakura_ann = True

            menu:

                mo "Believe it or not, you're not the first person to ask for that."

                "Someone asked for a dakimakura of themselves?":

                    mo "For sure. I won't disclose their name, but they were very excited."

                "Someone asked for a dakimakura of me?":

                    mo "Eh? She was just some girl with black hair."

            hide dakimakura
            with easeoutright

        "{s}[a] ($[dakimakura_price]){/s}" if ((dakimakura_ann == False) and (money < dakimakura_price)):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "[fs] ($[dakimakura_price])" if ((dakimakura_fs == False) and (money >= dakimakura_price)):

                    show dakimakura fs
                    with easeinright

                    $ dakimakura_fs = True

                    mo "I don't wanna know why you want this, but you aren't the first person to ask for this. Here..."

                    hide dakimakura
                    with easeoutright

        "{s}[fs] ($[dakimakura_price]){/s}" if ((dakimakura_fs == False) and (money < dakimakura_price)):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "[mo] ($[dakimakura_price])" if (money >= dakimakura_price):

            show moe
            with easeinright

            mo "Absolutely not."

            hide moe
            with easeoutright

        "{s}[mo] ($[dakimakura_price]){/s}" if (money < dakimakura_price):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.
            # Not that it mattered for this choice.

            pass

        "Don't make a dakimakura.":

            return

    jump buy_dakimakura
