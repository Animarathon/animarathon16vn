# Animarathon XVI: Operation Ohio Tutorial
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
#  _____      _             _       _ 
# |_   _|   _| |_ ___  _ __(_) __ _| |
#   | || | | | __/ _ \| '__| |/ _` | |
#   | || |_| | || (_) | |  | | (_| | |
#   |_| \__,_|\__\___/|_|  |_|\__,_|_|

#  ____        _           _
# / ___| _ __ | | __ _ ___| |__  ___  ___ _ __ ___  ___ _ __  
# \___ \| '_ \| |/ _` / __| '_ \/ __|/ __| '__/ _ \/ _ \ '_ \ 
#  ___) | |_) | | (_| \__ \ | | \__ \ (__| | |  __/  __/ | | |
# |____/| .__/|_|\__,_|___/_| |_|___/\___|_|  \___|\___|_| |_|
#       |_|

label pre_game:

    scene pink

    if renpy.ios:

        "Error Code {b}Lemon Waffle Doughnut{/b}: Please report this error only to animarathon@bgsu.edu"

        # No way this is getting accepted with the GPL. Some shenanigans have occurred.

        $ renpy.quit()

    system "There are portrayals of Laws and Animarathon rules being broken in game. You must follow the Law. Follow Animarathon rules at Animarathon or face punishment."

    system "This game contains depictions of bad behavior, violence, alcohol, drugs, gambling, and gratuitous romance scenes not suitable for everyone."

    system "This game has flashing imagery that could cause dangerous seizures. Exit the game now if you or anyone watching is at risk for a seizure."

    menu:

        system "{b}Those with epilepsy must exit this game now{/b}. This game is for responsible players 18 years or older."

        "Begin tutorial.":

            jump tutorial

        "Skip tutorial to character setup":

            hide 3D tutorial
            with dissolve

            stop music fadeout 1

            jump setup

        "Skip tutorial and setup and play the game with presets":

            hide 3D tutorial
            with dissolve

            stop music fadeout 1

            jump intro

        "Exit the game.":

            $ renpy.quit()

label tutorial:

    scene white

    queue music this_reminds_me_of_something_p1

    show 3D Tutorial at truecenter

    python:
        tutorial = True
        achievement.grant("RTFM")

    label tutorial_menu:

        menu:

            system "To select a menu option, click or tap on it."

            "Game Controls":

                call tutorial_controls

            "Game Background":

                call tutorial_background

            "Recommended Requirements":

                call tutorial_requirements

            "Begin character setup":

                hide 3D tutorial
                with dissolve

                stop music fadeout 1

                jump setup

            "Skip setup and play the game with presets":

                hide 3D tutorial
                with dissolve

                stop music fadeout 1

                jump intro

        jump tutorial_menu

label tutorial_background:

    system "At Animarathon you play as [a]."

    show ann normal with easeinleft

    a "Nice to meet ya!"

    system "Please take care of [a], she's a great mascot!"

    hide ann normal with easeoutleft

    system "Grabbing a burger at the food court, some hot coffee, or some nuttin dojinshi at artists alley takes {b}no time{/b}."

    system "However going to a panel or event {b}will take the time listed in the schedule{/b}."

    system "[a] has a PANDA (Personal Area Network Digital Assistant). Use PANDA programs like {b}schedule{/b} with the {b}esc{/b} key!"

    system "If [a] is hungry or sleepy {b}yelling like an anime character{/b} becomes harder."

    system "Running out of money will prevent [a] from {b}buying things{/b}."

    return

label tutorial_visual_novel:

    # Honestly not sure if I should include this part in the game or not.

    system "A visual novel is a game that plays much like a book. The player interacts with the game by making choices at critical points."

    system "This game in particular is an Original English Language Visual Novel or OELVN. It was written in English, and not created by a Japanese studio."

    system "This game does a few things differently then a typical OELVN. It should not be considered representative of the genre."

    return

label tutorial_controls:

    system "To progress use the {b}spacebar{/b} or {b}left mouse button.{/b}"

    system "Great Job! If your computer has a touchscreen or pointing joystick it may be compatible! Use what you like best!"

    system "Regret a decision? Scroll the mouse wheel back to undo {b}recent{/b} choices. This doesn't go back forever, so you should create a new save often."

    # The player would just save scum otherwise. This is disabled only when it might break the game.

    system "See something that you like? Use the {b}S key{/b} to take a screenshot."

    system "Press the {b}V key{/b} to use text to speech mode. On GNU/Linux you need the espeak package to use this mode."

    # Self voicing with Ren'Py is only available on Windows, MacOS, and GNU/Linux.

    system "You must restart while in 3D for the FOV slider to have an effect."

    # A-Frame does not read from the source html file dynamicly. Once it's loaded that's it.

    return

label tutorial_requirements:

    # FIXME do full profiling and testing

    system "It is recommended that your system have at least 256MB of RAM and a processor with enough megahertz to go Doki Doki."

    system "Hardware such as VR Headsets and 3D Printers are more disgusting than their 2D counterparts, but all may be useful."

    system "It is recommended that you have a foxy and fast web browser installed if you have a VR headset. Motion controls are not used in this version."

    system "During some portions of this game, having long cords to your headphones or speakers may help make certain special effects possible!"

    return
