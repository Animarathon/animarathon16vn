# Animarathon XVI: Operation Ohio Setup
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
#  ____       _
# / ___|  ___| |_ _   _ _ __  
# \___ \ / _ \ __| | | | '_ \ 
#  ___) |  __/ |_| |_| | |_) |
# |____/ \___|\__|\__,_| .__/ 
#                      |_|
label setup:

    queue music this_reminds_me_of_something_p2

    scene purple
    with dissolve

    show ann normal
    with easeinleft

#  ____       _                 __  __
# / ___|  ___| |_ _   _ _ __   |  \/  | ___ _ __  _   _
# \___ \ / _ \ __| | | | '_ \  | |\/| |/ _ \ '_ \| | | |
#  ___) |  __/ |_| |_| | |_) | | |  | |  __/ | | | |_| |
# |____/ \___|\__|\__,_| .__/  |_|  |_|\___|_| |_|\__,_|
#                      |_|

label setup_menu:

    menu:

        a "It's not like I want you to set up my character or anything."

        "Explain character options":

            call explain_setup_options

        "Favorite Anime":

            call set_favorite_anime

        "Online Handle":

            call set_online_handle

        "Power Code" if power_code == False:

            call set_power_code

        "Reset Ann":

            call reset_ann

        #  _____ _       _     _       ____       _
        # |  ___(_)_ __ (_)___| |__   / ___|  ___| |_ _   _ _ __
        # | |_  | | '_ \| / __| '_ \  \___ \ / _ \ __| | | | '_ \
        # |  _| | | | | | \__ \ | | |  ___) |  __/ |_| |_| | |_) |
        # |_|   |_|_| |_|_|___/_| |_| |____/ \___|\__|\__,_| .__/
        #                                                  |_|

        "Finish Setup":

            stop music fadeout 1

            hide ann with easeoutleft

            jump intro

jump setup_menu

#  _____            _       _   
# | ____|_  ___ __ | | __ _(_)_ __  
# |  _| \ \/ / '_ \| |/ _` | | '_ \ 
# | |___ >  <| |_) | | (_| | | | | |
# |_____/_/\_\ .__/|_|\__,_|_|_| |_|
#            |_|

label explain_setup_options:

    a "My favorite anime is the Anime I like the most, and my online handle is the username I use online."

    return

#  _____                     _ _            _          _
# |  ___|_ ___   _____  _ __(_) |_ ___     / \   _ __ (_)_ __ ___   ___
# | |_ / _` \ \ / / _ \| '__| | __/ _ \   / _ \ | '_ \| | '_ ` _ \ / _ \
# |  _| (_| |\ V / (_) | |  | | ||  __/  / ___ \| | | | | | | | | |  __/
# |_|  \__,_| \_/ \___/|_|  |_|\__\___| /_/   \_\_| |_|_|_| |_| |_|\___|

label set_favorite_anime:

    $ favorite_anime = renpy.input("What is your favorite anime?")

    $ favorite_anime = favorite_anime.strip() # Sanitize Player Input

    if favorite_anime == "":

        $ favorite_anime = "Magical Man M'onsieur"

        # In case the player entered nothing as their favorite anime, use a default value.

    show ann smug

    a "[favorite_anime] has to be my favorite anime!"

    show ann normal

    return

#   ___        _ _              _   _                 _ _
#  / _ \ _ __ | (_)_ __   ___  | | | | __ _ _ __   __| | | ___
# | | | | '_ \| | | '_ \ / _ \ | |_| |/ _` | '_ \ / _` | |/ _ \
# | |_| | | | | | | | | |  __/ |  _  | (_| | | | | (_| | |  __/
#  \___/|_| |_|_|_|_| |_|\___| |_| |_|\__,_|_| |_|\__,_|_|\___| 

label set_online_handle:

    $ online_handle = renpy.input("What is your online handle?")

    $ online_handle = online_handle.strip() # Sanitize Player Input

    if online_handle == "":

        $ online_handle = "Ann_i_meme_xXx_BGxTSUN_xXx_1337"

        # In case the player entered nothing as their handle, use a default value.

    show ann normal

    a "In cyberspace people call me [online_handle]."

    return

#  ____                           ____          _
# |  _ \ _____      _____ _ __   / ___|___   __| | ___ 
# | |_) / _ \ \ /\ / / _ \ '__| | |   / _ \ / _` |/ _ \
# |  __/ (_) \ V  V /  __/ |    | |__| (_) | (_| |  __/
# |_|   \___/ \_/\_/ \___|_|     \____\___/ \__,_|\___|

label set_power_code:

    system "Enter the {b}power code{/b} on the front of your {b}power chip{/b}. You may reuse the one you got at Animarathon XV."

    $ power_code_entered = renpy.input("{b}Power Chip{/b} number format: xxx-xxx-xxxx")

    $ power_code_entered = power_code_entered.strip() # Sanitize Player Input

    if power_code_entered == "419-352-8475":

        system "{b}Power Code{/b} successfully entered!"

        $ power_code = True

    if power_code_entered != "419-352-8475":

        system "Sorry that's not a valid {b}Power Code{/b}!"

    return

#  ____                _        _
# |  _ \ ___  ___  ___| |_     / \   _ __  _ __  
# | |_) / _ \/ __|/ _ \ __|   / _ \ | '_ \| '_ \ 
# |  _ <  __/\__ \  __/ |_   / ___ \| | | | | | |
# |_| \_\___||___/\___|\__| /_/   \_\_| |_|_| |_|

label reset_ann:

    python:

        favorite_anime = "Magical Man M'onsieur"

        online_handle = "Ann_i_meme_xXx_BGxTSUN_xXx_1337"

        power_code = False

    return
