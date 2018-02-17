# Animarathon XVI: Operation Ohio Floor 4
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

label fourth_floor:

    stop music fadeout 1

    scene black
    # This is meant to be jarring. Do not use a transition like "with dissolve"
    # Don't use sound either

    # Use reverse chronological order to avoid logic issues.

    if (sezsez_met == True) and (coupon_entered == True):

        call sezsez_ending

    if (sezsez_met == True) and (coupon_entered == False):

        call sezsez_mission_middle

    if (sezsez_met == False):

        call sezsez_mission_start

    return

label sezsez_mission_start:

    ann_thoughts "It's dark in here. I'm likely to be eaten by a monster!"

    play sound switch37
    # Makes the sound of a light switch.

    scene bg power
    # Do not use a dissolve here.

    show sezsez liberty
    with easeinright

    sl "..."

    hide sezsez liberty
    with easeoutright

    ann_thoughts "The statue of liberty cosplayer slides me a piece of candy."

    show candy at truecenter
    with easeinbottom

    menu:

        ann_thoughts "Should I open the candy?"

        "Open the candy.":

            ann_thoughts "There is a small shard of peppermint inside, along with a note soaked in mouthwash."

            mn "Want a laugh?"

            mn "Want a {b}good{/b} time?"

            mn "Want a laugh?"

            mn "Want some fries?"

            mn "Want a laugh?"

            mn "We have lot's of laughs for you!"

            mn "he. he. he."

            mn "ha. ha. ha."

            mn "It's time for you to give us a laugh!"

            mn "Use this coupon at Ray's Rations and come back with the goods."

            mn "And we will laugh"

            mn "Together!"

            mn "~SEZSEZ"

            $ sezsez_met = True

            ann_thoughts "Oh! There is a coupon on the back."

            mn "Hey students! Feeling parched before finals?"

            mn "Get a free NaN {i}oz.{/i} soda pop from Rays Rations in the union!"

            mn "Coupon code: [coupon_code], Expires June 3rd 2038."

            hide candy
            with easeoutbottom

        "Do not open the candy.":

            ann_thoughts "This is too weird."

    play sound switch37
    scene black
    # Makes the sound of a light switch.

    return

label sezsez_mission_middle:

    ann_thoughts "I better not stick around here!"

    return
