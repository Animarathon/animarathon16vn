# Animarathon XVI: Operation Ohio Taiko Panel
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
#  _____     _ _           ____                  _
# |_   _|_ _(_) | _____   |  _ \ __ _ _ __   ___| |
#   | |/ _` | | |/ / _ \  | |_) / _` | '_ \ / _ \ |
#   | | (_| | |   < (_) | |  __/ (_| | | | |  __/ |
#   |_|\__,_|_|_|\_\___/  |_|   \__,_|_| |_|\___|_|
#  ____                  _   ____  _
# |  _ \ __ _ _ __   ___| | |  _ \| | __ _ _ __  
# | |_) / _` | '_ \ / _ \ | | |_) | |/ _` | '_ \ 
# |  __/ (_| | | | |  __/ | |  __/| | (_| | | | |
# |_|   \__,_|_| |_|\___|_| |_|   |_|\__,_|_| |_|
#
# By the end of the panel the player should experience the following outcomes.
#
# ! Positive Outcome (Player doesn't nap.)
# 💭 Learn that Taiko is the Japanese art of drumming.
# 💭 Learn that Taiko is deeper then simple drums.
# $ Gain a in game reward for learning.
# Ψ Feel that this learning was done of their own free will.
#
# ! Negative Outcomes (The player took a nap.)
# 💭 Experience some minor wordplay.
# $ Gain a in game reward to encourage better sleeping habits.
# Ψ Feel that this choice was made of their own free will. 

label taiko:

    scene panel room japanese
    with dissolve

    play music yo_p0 fadeout 1

    show text "{size=70}Chapter 1: Taiko Terror!{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard='True')
    
    hide text
    with dissolve

    show crowd
    with easeinbottom

    jump taiko_menu

label taiko_menu:

    menu:

        ann_thoughts "Looks like the taiko panel is about to start. What should I do?"

        "Stay awake for the panel":

            call taiko_awake

        "Consider the Panel":

            call taiko_considerations

            jump taiko_menu

        "Take a nap outside the panel":

            call taiko_asleep

    stop music fadeout 1

    return

label taiko_awake:

    show kaze
    with easeinright
    
    kz "{size=50}BAMF! BAM! BOF!{/size} Welcome to Taiko Today!"

    menu:

        kz "To start out, does anyone know what Taiko is?"

        "Octopus!":

            kz "Sorry, this is {b}Taiko Today{/b}, not {b}Tako Today{/b}. Taiko is a musical instrument. Tako is an octopus."

            hide kaze
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "50 wu7 1z 741k0?"
            # So what is Taiko?

            hide guest
            with easeoutright

            show kaze
            with easeinright

            kz "Taiko are traditional Japanese drums. In Japanese the word Taiko actually refers to any drum."

            hide kaze
            with easeoutright

        "A Musical Instrument":

            kz "Bam! That's right!"

            $ energy += 10

            hide kaze
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "50 wu7 1z 741k0?"
            # So what is Taiko?

            hide guest
            with easeoutright

            show kaze
            with easeinright

            kz "Taiko are traditional Japanese drums. In Japanese the word Taiko actually refers to any drum."

            hide kaze
            with easeoutright

        "A Drifting Technique":

            kz "That's pretty far off. There are some popular racing tankobon, so you may have gotten tankobon confused with taiko, a musical instrument."

            hide kaze
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "50 wu7 1z 741k0?"
            # So what is Taiko?

            hide guest
            with easeoutright

            show kaze
            with easeinright

            kz "Taiko are traditional Japanese drums. In Japanese the word Taiko actually refers to any drum."

            hide kaze
            with easeoutright

        "Stay Quiet":

            hide kaze
            with easeoutright

            show guest welchertaku
            with easeinright

            guest_welchertaku "Oh! Oh! {b}Oh!{/b} I know the answer!"

            hide guest
            with easeoutright

            show kaze
            with easeinright

            kz "Great! Let's hear it!"

            hide kaze
            with easeoutright

            show guest welchertaku
            with easeinright

            guest_welchertaku "Taiko was in my favorite anime, {b}Welchert in the Crib: Z{/b}!"

            hide guest
            with easeoutright

            show kaze
            with easeinright

            kz "That's nice but this is more about Taiko in the real world.{nw}"

            hide kaze
            with easeoutright

            show guest welchertaku
            with easeinright

            guest_welchertaku "In the official reference guide {b}Historia Welchertia{/b}, Taiko plays a key role!{nw}" with vpunch

            guest_welchertaku "Welchert's third cousin, thrice removed, Walton, was a taiko master so powerful, he rivaled the power of Welchert himself.{nw}" with hpunch

            guest_welchertaku "He was able to become a Taiko master because as an immortal welchert family member, he had plenty of time to practice.{nw}" with vpunch

            guest_welchertaku "In the Season 7 Battle of the Bands arc, we see the true musical powers of Taiko, as Walton uses Taiko's signature sonic attack to wipe out the competition literally!{nw}" with hpunch

            hide guest
            with easeoutright

            show kaze
            with easeinright

            kz "Um.{nw}"

            hide kaze
            with easeoutright

            show guest welchertaku
            with easeinright

            guest_welchertaku "After this Welcherta works with Walton to develop a Taiko dance, that makes playing Taiko three times more effective.{nw}" with vpunch

            guest_welchertaku "Ironicly, Walton was shot after leaving his taiko equipment at home and thus powerless in the {b}Cincinnati Strike{/b} arc of 2016.{nw}" with hpunch

            guest_welchertaku "It's also on the Welchert Wiki! Really anyone should know what Taiko is!" with vpunch

            hide guest
            with easeoutright

            show kaze
            with easeinright

            kz "Um. You didn't actually explain what Taiko was."

            hide kaze
            with easeoutright

            show guest welchertaku
            with easeinright

            guest_welchertaku "Nope! I just wanted to talk about {b}Welchert in the Crib: Z{/b}!"

            hide guest
            with easeoutright

            show kaze
            with easeinright

            kz "Taiko is a Japanese drum. I'm glad it's so prominent in your favorite anime. In Japanese Taiko refers to any kind of drum."

            hide kaze
            with easeoutright

    show guest otaku
    with easeinright

    guest_otaku "Like the Nihongo word anime, right taiko senpsei sama san ~uguu~?"
    # Just like the Japanese word for cartoon, right Japanese Drum teacher?

    hide guest
    with easeoutright

    show kaze
    with easeinright

    kz "Indeed? However outside Japan Taiko refers to a specific category of drum."

    hide kaze
    with easeoutright

    show guest otaku
    with easeinright

    guest_otaku "Not all Taiko the same? Sensei what kinds of Taiko are there?"
    # Not all Japanese drums are the same? Teacher, what kinds of Japanese drums are there?

    hide guest
    with easeoutright

    show kaze
    with easeinright

    kz "Well there's O-daiko which are big, and Chudaiko which are wine barrels or logs converted into drums."

    hide kaze
    with easeoutright

    show ann happy
    with easeinleft

    a "So if a tree falls in a forest, and nobody is around to hear it, they might hear it later as a Taiko drum?"

    hide ann
    with easeoutleft

    show kaze
    with easeinright

    kz "Exactly! Moving on Shime-daiko are used to keep the beat like a metronome, and Chanchiki are used to produce higher pitch notes."

    hide kaze
    with easeoutright

    show guest gamer
    with easeinright

    guest_gamer "um 50 wu7 1z 4 741k0 druM571k c4113D?"
    # Um, so what is a Taiko drumstick called?

    hide guest
    with easeoutright

    show kaze
    with easeinright

    kz "Good question! Taiko drum sticks are called bachi sticks!"

    hide kaze
    with easeoutright

    show guest gamer
    with easeinright

    guest_gamer "thx d00d u pwn! 1 w1ll r33k my rhy7m g43m c0mp171710n n40w."
    # Thanks dude! You are awesome! I will be victorious over my rhythm game competition now.

    hide guest
    with easeoutright

    show kaze
    with easeinright

    kz "Bam! That concludes my Taiko panel!"

    hide kaze
    with easeoutright

    return

#     _        _
#    / \   ___| | ___  ___ _ __  
#   / _ \ / __| |/ _ \/ _ \ '_ \ 
#  / ___ \\__ \ |  __/  __/ |_) |
# /_/   \_\___/_|\___|\___| .__/ 
#                         |_|
label taiko_asleep:

    play music this_reminds_me_of_something_p4 fadeout 1

    show black
    with irisin

    a "Sleep is good. mmmm..."

    show orange
    with dissolve

    hide black
    with dissolve

    ann_thoughts "A thousand drumsticks right through my skull..."

    show red
    with dissolve

    hide orange
    with dissolve

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "It hurts..."

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

label taiko_considerations:

    menu:
    
        ann_thoughts "Was there anything I wanted to consider before the panel starts?"

        "Who is the panelist?":

            ann_thoughts "[kz] is the leader of our campus taiko band."

            ann_thoughts "He's lead our college to victory in competitions many times."

            ann_thoughts "I wonder what he'll have to say?"

        "What is taiko?":

            ann_thoughts "Taiko are Japanese drums."

            ann_thoughts "They're pretty loud!"

        "That's all":

            return

    jump taiko_considerations
