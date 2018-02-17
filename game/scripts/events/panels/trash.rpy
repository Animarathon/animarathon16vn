# Animarathon XVI: Operation Ohio Trash Panel
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
# __        __   _      _               _     _         _   _             ____      _ _        _____
# \ \      / /__| | ___| |__   ___ _ __| |_  (_)_ __   | |_| |__   ___   / ___|_ __(_) |__ _  |__  /
#  \ \ /\ / / _ \ |/ __| '_ \ / _ \ '__| __| | | '_ \  | __| '_ \ / _ \ | |   | '__| | '_ (_)   / / 
#   \ V  V /  __/ | (__| | | |  __/ |  | |_  | | | | | | |_| | | |  __/ | |___| |  | | |_) |   / /_ 
#    \_/\_/ \___|_|\___|_| |_|\___|_|   \__| |_|_| |_|  \__|_| |_|\___|  \____|_|  |_|_.__(_) /____|
#  ____                  _   ____  _
# |  _ \ __ _ _ __   ___| | |  _ \| | __ _ _ __  
# | |_) / _` | '_ \ / _ \ | | |_) | |/ _` | '_ \ 
# |  __/ (_| | | | |  __/ | |  __/| | (_| | | | |
# |_|   \__,_|_| |_|\___|_| |_|   |_|\__,_|_| |_|
#
# By the end of the panel the player should experience the following outcomes.
#
# ! Positive Outcome (Player doesn't nap.)
# 💭 Understand how poor ettiquite can turn others off of a series.
# 💭 Understand that, despite that, fandom can be a good thing!
# 💭 See that, while many fans have poor social skills, most mean well.
# $ Gain a in game reward for learning.
# Ψ Feel that this learning was done of their own free will.
#
# ! Negative Outcomes (The player took a nap.)
# 💭 Experience some minor entertainment.
# $ Gain a in game reward to encourage better sleeping habits.
# Ψ Feel that this choice was made of their own free will. 

label trash:

    scene bg bathroom
    with dissolve

    play music this_reminds_me_of_something_p0 fadeout 1

    show text "{size=70}Chapter 3: Wacky Welchertaku!{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard='True')
    
    hide text
    with dissolve

    show crowd
    with easeinbottom

    jump trash_menu

label trash_menu:

    menu:

        ann_thoughts "Looks like the Welchert in the Crib: Z panel is about to start. What should I do?"

        "Stay awake for the panel":

            call trash_awake

        "Consider the Panel":

            call trash_considerations

            jump trash_menu

        "Take a nap outside the panel":

            call trash_asleep

    stop music fadeout 1

    return

label trash_awake:

    if favorite_anime == "Welchert in the Crib: Z":

        ann_thoughts "It's so great to have two [favorite_anime] panels!"

    show cody maison
    with easeinright

    cm "Welcome Welchertakus! To get us started, who here has seen Welchert in the Crib: Z?"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Oh! Oh! I have! I'm even cosplaying Welchert's right hand man, Zebulon the Third!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "My omae! {b}WELCHERT OMEGA THANKS!{/b}"

    hide cody maison
    with easeoutright

    queue music this_reminds_me_of_something_p1

    if favorite_anime != "Welchert in the Crib: Z":

        # If Ann is not a fan of Welchert in the Crib: Z, go to the normal section.

        call trash_notfan

    if favorite_anime == "Welchert in the Crib: Z":

        # If Ann is a fan of Welchert in the Crib: Z, go to the fan section.

        call trash_fan
    
    return

label trash_notfan:

    show ann happy
    with easeinleft

    a "Nice cosplay! You clearly put a lot of effort into it!"

    hide ann
    with easeoutleft

    show cody maison
    with easeinright

    cm "I could say the same! You are the splitting image of Welcherta herself! {b}MEGA WELCHERT FAN ALERT!{/b}"

    hide cody maison
    with easeoutright

    stop music fadeout 1
    # Stopping the music for just one line should give it weight.

    show ann normal
    with easeinleft

    a "Actually I've never seen Welchert in the Crib: Z. I like [favorite_anime]."

    hide ann
    with easeoutleft

    play music this_reminds_me_of_something_p2 fadeout 1

    show cody maison
    with easeinright

    cm "{b}YOU MONSTER!{/b} [favorite_anime] is trash! Only a degenerate would watch it!"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "{b}YEAH!{/b} [favorite_anime] is trash!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "Right on brother! [favorite_anime] {i}is{/i} trash! You know what anime isn't a garbage fire?"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "What anime is that brother?"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "{b}Welchert in the Crib: Z!{/b}"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Right on brother!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "[favorite_anime] isn't deep at all but Welchert in the Crib: Z is very deep!"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Yeah brother! [favorite_anime] is shallow because it has no real narrative and bad combat scenes!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "If [favorite_anime] did it it's bad! You can remember that with this equation! [favorite_anime] = Bad!"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "[favorite_anime] has the depth of toiler paper but Welchert in the Crib: Z is as deep as an ocean!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "That's a good point brother, but why is [favorite_anime] as deep as toilet paper?"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Because [favorite_anime] belongs in the toilet!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "You really get me brother! Unlike [favorite_anime]'s lame-o protagonist, Welchert is a hero who shows true depth!"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Welchert grew up in Miami, Florida and gets his power from the sun! It's very original!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "Not only that brother! After being forced to move to San Francisco with his cousin Dito he has to overcome the eternal fog!"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Everyone can relate to his struggle! As Welchert says {b}CLOUDY DAYS MAKE ME FROWN{/b}!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "We've got perfect chemistry brother! Don't forget that [favorite_anime] doesn't really have action, especially compared to Welchert in the Crib: Z"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Who can forget Welchert's {b}Noided Nine Arc{/b}!? Compare that to [favorite_anime]! [favorite_anime] action just means [favorite_anime] bad!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "Give me your number brother! Unlike this faker in the audience, your personality is as beautiful and kawaii as the real Welcherta."

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Welcherta is witty, has hammerspace for days, and is super buff! Who wouldn't want her as a waifu, or even {b}be{/b} her and marry Welchert?"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "I know I would! Panel's over! Let's roleplay it in the stairwell pronto!"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Brother! Let's {b}go down{/b} the stairwell! {b}DOUBLE WELCHERT STYLE{/b}"

    hide guest
    with easeoutright

    # If I hear a peep about stairwell activities IRL, I'll make you regret it.

    queue music this_reminds_me_of_something_p3

    ann_thoughts "That was kind of awkward, but at least they forgot about me."

    show cody maison
    with easeinright

    cm "{b}WAIT{/b}! I forgot to deal with {b}YOU{/b}!"

    hide cody maison
    with easeoutright

    menu:
    
        ann_thoughts "He's looking right at me! What should I do?"

        "Deny":

            show ann embarrassed
            with easeinleft

            a "Leave me out of your weird fun! I'm not going down the stairwell with you two!"

            hide ann
            with easeoutleft

            show cody maison
            with easeinright

            cm "We're on the same page! [favorite_anime] is a turn off!"

            hide cody maison
            with easeoutright

            show guest welchertaku
            with easeinright

            guest_welchertaku "Hurry brother! [favorite_anime] makes me less eager each time I hear it!"

            hide guest
            with easeoutright

        "Help":

            show ann normal
            with easeinleft

            a "Do you need help going down the stairwell? It can be hard to find."

            hide ann
            with easeoutleft

            show cody maison
            with easeinright

            cm "Sorry, but [favorite_anime] is a turn off!"

            hide cody maison
            with easeoutright

            show guest welchertaku
            with easeinright

            guest_welchertaku "This is a personal mission with my brother!"

            hide guest
            with easeoutright

        "Question":

            show ann normal
            with easeinleft

            a "How does one go down the stairwell {b}Double Wlechert Style{/b}?"

            hide ann
            with easeoutleft

            show cody maison
            with easeinright

            cm "It's a secret technique learned only by the most elite field hockey players of San Francisco, like Welchert or Zebulon the Third."

            hide cody maison
            with easeoutright

            show guest welchertaku
            with easeinright

            guest_welchertaku "Looks like you've turned her to our side brother! Another member of Welchert's Sunshine Brigade!"

            hide guest
            with easeoutright

    queue music this_reminds_me_of_something_p4

    show cody maison
    with easeinright

    cm "I used to be a casual like you. I even liked [favorite_anime]! But then I saw Welchert in the Crib: Z. You need this more then I do."

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Brother! Is that a signed copy of Welchert in the Crib: Z?! Those are Triple-Zebulon-Rating Rare!"

    hide guest
    with easeoutright

    show cody maison
    with easeinright

    cm "It is. I give it freely to you stranger. If you give Welchert a chance, you won't regret it. I know I didn't!"

    hide cody maison
    with easeoutright

    show ann normal
    with easeinleft

    a "Thank you."

    $ welchert_anime = True

    hide ann
    with easeoutleft

    show cody maison
    with easeinright

    cm "OK everyone! Before we go let's have a Welchert Stick Up! Stick your hands up!"

    hide cody maison
    with easeoutright

    "All Welchertaku" "Hail the sun! Hail Welchert!"

    show cody maison
    with easeinright

    cm "Now I must go! To the stairwell brother!"

    hide cody maison
    with easeoutright

    ann_thoughts "Holy Toledo!"

    ann_thoughts "Did that just happen? What kind of panel was that?"

    return

label trash_fan:

    show ann genki
    with easeinleft

    a "I love [favorite_anime]!"

    hide ann
    with easeoutleft

    show cody maison
    with easeinright

    cm "Do my eyes deceive me, or are you the splitting image of Welcherta herself!? {b}MEGA WELCHERT ALPHA FAN ALERT!{/b}"

    hide cody maison
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "There's no way that's a cosplay! That's Welcherta herself!"

    hide guest
    with easeoutright

    if magical_girl:

        show guest welchertaku
        with easeinright

        guest_welchertaku "{b}THE WAY YOU DEFEATED NEGA-ZEBULON IN THE ME^2 MONSOON ARC WITH YOUR GIGA HAMMERSPACE PADDLE IS SO COOL!{/b}" with hpunch

        hide guest
        with easeoutright

        show cody maison
        with easeinright

        cm "{b}THAT ARC WAS UNFORGETTABLE! TURNING THE PADDLE SIDEWAYS TO ACTIVATE THE BLADE NANOMACHINES AND SLICE AND DICE TO THE SOUL RNA! SO SUGOI!{/b}" with hpunch

        hide cody maison
        with easeoutright

    queue music this_reminds_me_of_something_p2

    show ann genki
    with easeinleft

    a "I look just like the leading heroine of [favorite_anime] with just some hair dye! It's the ultimate cosplay!"

    hide ann
    with easeoutleft

    ann_thoughts "I'd tell them I recently signed on for the Live Action movie, but I'm under NDA! What a world!"

    show cody maison
    with easeinright

    queue music this_reminds_me_of_something_p3

    cm "M'Welcherta! You are an even bigger fan then I am! Please take my signed copy of [favorite_anime]"

    hide cody maison
    with easeoutright

    show ann genki
    with easeinleft

    a "Woah! These are super rare! I will cherish it always! Diasuki Welchert-Kun!"

    hide ann
    with easeoutleft

    if favorite_anime_get == True:

        show ann genki
        with easeinleft

        $ favorite_anime_get == False

        a "Please take my [favorite_anime] box set in turn! It's the least I can do!"

        hide ann
        with easeoutleft

    queue music this_reminds_me_of_something_p4

    show cody maison
    with easeinright

    cm "OK everyone! Before we go let's have a Welchert Stick Up! Stick your hands up!"

    hide cody maison
    with easeoutright

    "Everyone" "Hail the sun! Hail Welchert!"

    $ welchert_anime = True

    show cody maison
    with easeinright

    cm "See you Welchertakus!"

    hide cody maison
    with easeoutright

    return

#     _        _
#    / \   ___| | ___  ___ _ __  
#   / _ \ / __| |/ _ \/ _ \ '_ \ 
#  / ___ \\__ \ |  __/  __/ |_) |
# /_/   \_\___/_|\___|\___| .__/ 
#                         |_|
label trash_asleep:

    play music this_reminds_me_of_something_p4 fadeout 1

    show black
    with irisin

    a "Sleep is good. mmmm..."

    show orange
    with dissolve

    hide black
    with dissolve

    ann_thoughts "Why is everyone's hair weird..."

    show red
    with dissolve

    hide orange
    with dissolve

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "Like one of my Japanese animes..."

    $ energy += 10

    hide crowd

    hide red
    with irisout

    ann_thoughts "Oh my. Looks like everyone's gone now."

    return

#   ____                _     _                _   _                 
#  / ___|___  _ __  ___(_) __| | ___ _ __ __ _| |_(_) ___  _ __  ___ 
# | |   / _ \| '_ \/ __| |/ _` |/ _ \ '__/ _` | __| |/ _ \| '_ \/ __|
# | |__| (_) | | | \__ \ | (_| |  __/ | | (_| | |_| | (_) | | | \__ \
#  \____\___/|_| |_|___/_|\__,_|\___|_|  \__,_|\__|_|\___/|_| |_|___/

label trash_considerations:

    menu:
    
        ann_thoughts "Was there anything I wanted to consider before the panel starts?"

        "Who is the panelist?":

            if favorite_anime == "Welchert in the Crib: Z":

                ann_thoughts "[cm]'s one of the biggest Welchertaku fanfic writers in the galaxy!"

            if favorite_anime != "Welchert in the Crib: Z":

                ann_thoughts "He's probably a fan or something? I don't know."

            ann_thoughts "I wonder what he'll have to say?"

        "What is Welchert in the Crib: Z?":

            if favorite_anime == "Welchert in the Crib: Z":

                ann_thoughts "It's my favorite anime!."

            if favorite_anime != "Welchert in the Crib: Z":

                ann_thoughts "It's a fairly popular anime!"

        "That's all":

            return

    jump trash_considerations
