# Animarathon XVI: Operation Ohio Food Court
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

label food:

    play music orange_beach fadeout 1

    scene bg food court
    with dissolve

    # In older builds of the game there were 3 stalls to choose from.
    # Now that there is 1 choice this section is maintained for modularity.

    call rays_rations

    return

label rays_rations:

    if rays_first == False:

            show bellini rigatoni happy
            with easeinright

            cbr "If it ain't [online_handle]! Haven't seen you IRL in a while!"

            hide bellini rigatoni
            with easeoutright

            $ rays_first == True

    if rays_first == True:

            show bellini rigatoni happy
            with easeinright

            cbr "Soup's up [online_handle]."

            hide bellini rigatoni
            with easeoutright

    jump rays_rations_menu

label rays_rations_menu:

    menu:

        ann_thoughts "I have $[money]."

        "Pepperoncini Secret ($[pizza_pie_price])" if (money >=pizza_pie_price):

            show bellini rigatoni happy
            with easeinright

            cbr "Ayy, here's your pizza pie [online_handle]!"

            hide bellini rigatoni
            with easeoutright

            python:
                hunger -= 60
                money -= pizza_pie_price
                last_ordered = "Hot Pepper Pizza"

        "{s}Pepperoncini Secret{/s} ($[pizza_pie_price])" if (money < pizza_pie_price):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Chinese Raviolis ($[ravs_price])" if (money >=ravs_price):

            show bellini rigatoni happy
            with easeinright

            cbr "Ayy, here's your ravs [online_handle]!"

            hide bellini rigatoni
            with easeoutright

            python:
                hunger -= 60
                money -= ravs_price
                last_ordered = "Dumplings"

        "{s}Chinese Raviolis{/s} ($[ravs_price])" if (money < ravs_price):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Cheez Loq ($[cheez_price])" if (money >=cheez_price):

            show bellini rigatoni happy
            with easeinright

            cbr "Ayy, here's your cheez loq [online_handle]!"

            hide bellini rigatoni
            with easeoutright

            python:
                hunger -= 60
                money -= cheez_price
                last_ordered = "Cheese"

        "{s}Cheez Loq{/s} ($[cheez_price])" if (money < cheez_price):

            # If the player does not have enough money.
            # Display the option as striked out, but do nothing on click.

            pass

        "Give Coupon" if ((sezsez_met == True) and (coupon_entered == False)):

            show bellini rigatoni sad
            with easeinright

            cbr "You running an errand SEZSEZ [online_handle]? Man this order is sketch."

            hide bellini rigatoni
            with easeoutright

            show ann normal
            with easeinleft

            a "That's right. Really, did they order off the special menu?"

            hide ann
            with easeoutleft

            show bellini rigatoni sad
            with easeinright

            cbr "You bet! You're transporting dangerous drek so my usual confidentiality stuff is out."

            hide bellini rigatoni
            with easeoutright

            show ann normal
            with easeinleft

            a "What's in the takeout box?"

            hide ann
            with easeoutleft

            show bellini rigatoni sad
            with easeinright

            cbr "One extra large DMSO drink with EDTA flavoring, and some fries soaked in high potency syrup of ipecac."

            hide bellini rigatoni
            with easeoutright

            show ann disgust
            with easeinleft

            a "DSMO?! That's an industrial solvent! You shouldn't drink that!"

            hide ann
            with easeoutleft

            show bellini rigatoni sad
            with easeinright

            cbr "Forget that, if you touch it DSMO carries any other drugs to the bloodstream. EDTA lets it penetrate through clothes."

            hide bellini rigatoni
            with easeoutright

            ann_thoughts "That's right. Very rarely medical professionals will use DSMO if an injection isn't appropriate."

            show ann normal
            with easeinleft

            a "Why syrup of ipecac fries? That syrup induces vomiting! It's not even used as medicine anymore!"

            hide ann
            with easeoutleft

            show bellini rigatoni happy
            with easeinright

            cbr "Put two and two together. Normally you take syrup orally. DSMO lets it work on touch. The food is clearly a cover."

            hide bellini rigatoni
            with easeoutright

            show ann normal
            with easeinleft

            a "Do you know why they want this stuff? Are they targeting someone?"

            hide ann
            with easeoutleft

            show bellini rigatoni sad
            with easeinright

            cbr "Yeah, but that's none of your business. I'm taking a early vacation later today, and so should you."

            hide bellini rigatoni
            with easeoutright

            show ann normal
            with easeinleft

            a "Thanks for giving me what info you could."

            hide ann
            with easeoutleft

            show bellini rigatoni happy
            with easeinright

            cbr "Null sweat. Watch your back [online_handle]."

            hide bellini rigatoni
            with easeoutright

            $ coupon_entered = True

        "It's time to leave":

            show bellini rigatoni happy
            with easeinright

            cbr "Ayy, I'll see you online [online_handle]."

            hide bellini rigatoni
            with easeoutright

            return

jump rays_rations_menu

