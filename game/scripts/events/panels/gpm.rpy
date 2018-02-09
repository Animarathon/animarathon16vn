# Animarathon XVI: Operation Ohio GPM Panel
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
#   ____ ____  __  __   ____                  _ 
#  / ___|  _ \|  \/  | |  _ \ __ _ _ __   ___| |
# | |  _| |_) | |\/| | | |_) / _` | '_ \ / _ \ |
# | |_| |  __/| |  | | |  __/ (_| | | | |  __/ |
#  \____|_|   |_|  |_| |_|   \__,_|_| |_|\___|_|
#
# By the end of the panel the player should experience the following outcomes.
#
# ! Positive Outcome (Player doesn't nap.)
# 💭 (Potential) Learn how to let go.
# 💭 (Potential) Learn about Van Eck Phreaking.
# 💭 Learn about scams involving scientific terms.
# $ Gain a in game reward for learning.
# Ψ Feel that this learning was done of their own free will.
#
# ! Negative Outcomes (The player took a nap.)
# 💭 Experience some minor wordplay.
# $ Gain a in game reward to encourage better sleeping habits.
# Ψ Feel that this choice was made of their own free will.

# Note:
# Schumann Resonance actually does affect the brain, simply say these words,
# And shmucks brains shut down!

label gpm:

    scene gym
    with dissolve

    play music yo_p0 fadeout 1

    show text "{size=70}Chapter 2: Dëstroy Dëvoid!{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard='True')
    
    hide text
    with dissolve

    show crowd
    with easeinbottom

    jump gpm_menu

label gpm_menu:

    menu:

        ann_thoughts "Looks like the Dë-Vërsë is Hell panel is about to start. What should I do?"

        "Stay awake for the panel":

            call gpm_awake

        "Consider the Panel":

            call gpm_considerations

            jump gpm_menu

        "Take a nap outside the panel":

            call gpm_asleep

    stop music fadeout 1

    return

label gpm_awake:

    show first streaming text
    show second streaming text
    show third streaming text

    # Begin Ebook conversation

    if haunted_radio:
        play music tone
        if haunted_ebook:
            $ print("Please tune in!")

    show gpm normal
    with easeinright

    gpm "Hey, It's me GPM. It's high noon so let's get started! The Dë-Vërsë has been Dëcomissionëd but that won't stop us from going there."

    hide gpm
    with easeoutright

    if haunted_ebook:
        $ print("It's about time, glad you're here friend!")

    show guest gamer
    with easeinright

    guest_gamer "1m40 d00d! d3v3r53 15 d33d!"
    # I'm laughing my butt off dude! the Dë-Vërsë is dead (No longer functioning).

    hide guest
    with easeoutright

    queue music yo_p1

    show gpm normal
    with easeinright

    gpm "The Dë-Vërsë was never anything more then a product of the Noosphere. If you know where to look it's alive and well."

    hide gpm
    with easeoutright

    if haunted_ebook:
        $ print("Could you please return me to my mortal flesh coil? its worth the effort.")

    show guest gamer
    with easeinright

    guest_gamer "y34 r1gh7."
    # Yeah right.

    hide guest
    with easeoutright

    show gpm normal
    with easeinright

    gpm "Using Schumann Resonance I can manifest aspects of the Noosphere here. There we can dëconstruct the Dë-Vërsë."

    hide gpm
    with easeoutright

    queue music yo_p2

    if haunted_ebook:
        $ print("My friend, the best panel is the friends we make 5 minutes from my body!")

    show guest gamer
    with easeinright

    guest_gamer "pr00v3 17 d00d."
    # Proove it dude.

    hide guest
    with easeoutright

    queue music yo_p3

    if haunted_ebook:
        $ print("This is awesome! Just print out ebook.stl and bring it to my mortal flesh coil!")

    show gpm normal
    with easeinright

    gpm "You can see the stream of livestream chat behind me right? This is a weak manifestation of what I'm talking about."

    hide gpm
    with easeoutright

    if haunted_ebook:
        $ print("Thanks friend! don't forget the ritual make my dream come true! :D")

    queue music yo_p4

    show guest cyber
    with easeinright

    guest_cyber "Yeah! Trash the Dë-Vërsë! Hack the world!"

    hide guest
    with easeoutright

    if haunted_radio:
        stop music

    queue music yo_p5

    show gpm normal
    with easeinright

    gpm "Is everyone in AR? Cool! Let's jack in! Dë-Vërsë is GO!"

    hide gpm
    with easeoutright

    hide first streaming text
    hide second streaming text
    hide third streaming text

    stop music fadeout 1

    show black
    with dissolve

    $ renpy.run(OpenURL("https://animarathon.com/animarathon16vn/vr/gpm.html"))

    # When testing from the Ren'Py launcher, be advised that it will look for the document in the Ren'Py launcher directory
    # Not in the game directory as you would expect.
    # This is location is fine for shipping.

    menu:

        ann_thoughts "I can pull öut at any timë, but dö I want tö dö that prëmaturëly?"

        "Dëcëivë nöösphërë":

            pass

        "Divorcë nöösphërë":

            pass

        "Dëvolvë nöösphërë":

            pass

        "Dësërt nöösphërë":

            pass

    hide black
    with dissolve

    play music breathe_short fadeout 1

    show gpm normal
    with easeinright

    gpm "Dëja-vu! What were we doing here again?"

    hide gpm
    with easeoutright

    ann_thoughts "A burden has been lifted from us all."

    show ann normal
    with easeinleft

    a "I beleive you were talking about how Schumann Resonance can link all our brains together or something?"

    hide ann
    with easeoutleft

    show gpm normal
    with easeinright

    gpm "Oh yeah. Whatever I was doing must have used something else, because Schumann Resonance definately can't do that. Panel's over."

    hide gpm
    with easeoutright

    $ energy += 5

    return

#     _        _
#    / \   ___| | ___  ___ _ __  
#   / _ \ / __| |/ _ \/ _ \ '_ \ 
#  / ___ \\__ \ |  __/  __/ |_) |
# /_/   \_\___/_|\___|\___| .__/ 
#                         |_|
label gpm_asleep:

    play music this_reminds_me_of_something_p4 fadeout 1

    show black
    with irisin

    a "Sleep is good. mmmm..."

    show orange
    with dissolve

    hide black
    with dissolve

    ann_thoughts "Buffer then the rest of them... Time to flex my guns..."

    show red
    with dissolve

    hide orange
    with dissolve

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "The buffiest buffer... I need a bigger cache..."

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

label gpm_considerations:

    menu:
    
        ann_thoughts "Was there anything I wanted to consider before the panel starts?"

        "Who is [gpm]?":

            ann_thoughts "GPM is a superstar streamer on the world wide web!"

            ann_thoughts "He also does some web development!"

            ann_thoughts "I wonder what he'll have to say?"

        "That's all":

            return

    jump gpm_considerations
