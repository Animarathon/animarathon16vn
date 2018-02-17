# Animarathon XVI: Operation Ohio Time System
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
#  _____ _                  ____            _                 
# |_   _(_)_ __ ___   ___  / ___| _   _ ___| |_ ___ _ __ ___  
#   | | | | '_ ` _ \ / _ \ \___ \| | | / __| __/ _ \ '_ ` _ \ 
#   | | | | | | | | |  __/  ___) | |_| \__ \ ||  __/ | | | | |
#   |_| |_|_| |_| |_|\___| |____/ \__, |___/\__\___|_| |_| |_|
#                                 |___/
# When the player visits a panel or event, the in game time progresses.
# Time does not pass when shopping or doing side quests.

#     _       _                             _____ _                
#    / \   __| |_   ____ _ _ __   ___ ___  |_   _(_)_ __ ___   ___ 
#   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \   | | | | '_ ` _ \ / _ \
#  / ___ \ (_| |\ V / (_| | | | | (_|  __/   | | | | | | | | |  __/
# /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|   |_| |_|_| |_| |_|\___|
# This function is VERY IMPORTANT.
# This not only governs game time, but game difficulty as well.
# Only change it if you are sure what you're doing.


label advance_time:
    python:
        time += (time_factor)
        hunger += (difficulty_factor*time_factor)
        energy -= (difficulty_factor*time_factor)
    
    # Reset the time factor to a sane value.
    $ time_factor = 1
    return

#  ____  _           _               _____ _                
# |  _ \(_)___ _ __ | | __ _ _   _  |_   _(_)_ __ ___   ___ 
# | | | | / __| '_ \| |/ _` | | | |   | | | | '_ ` _ \ / _ \
# | |_| | \__ \ |_) | | (_| | |_| |   | | | | | | | | |  __/
# |____/|_|___/ .__/|_|\__,_|\__, |   |_| |_|_| |_| |_|\___|
#             |_|            |___/                          
# I do not intend to use anything other then full units of hours.
# However should this change, the extra conditionals should help.
# As a purely decorative function this is not critical to the game.

label display_time:

    window hide

    # Hide the dialogue box from the player.

    if (time >= 9 and time < 10):

        show time 9
        with dissolve

        pause 3.0

    if (time >= 10 and time < 11):

        show time 10
        with dissolve

        pause 3.0

    if (time >= 11 and time < 12):

        show time 11
        with dissolve

        pause 3.0

    if (time >= 12 and time < 13):

        show time 12
        with dissolve

        pause 3.0

    if (time >= 13 and time < 14):

        show time 13
        with dissolve

        pause 3.0

    if (time >= 14 and time < 15):

        show time 14
        with dissolve

        pause 3.0

    if (time >= 15 and time < 16):

        show time 15
        with dissolve

        pause 3.0

    if (time >= 16 and time < 17):

        show time 16
        with dissolve

        pause 3.0

    if (time >= 17 and time < 18):

        show time 17
        with dissolve

        pause 3.0

    if (time >= 18 and time < 19):

        show time 18
        with dissolve

        pause 3.0

    if (time >= 19 and time < 20):

        show time 19
        with dissolve

        pause 3.0

    if (time >= 20 and time < 21):

        show time 20
        with dissolve

        pause 3.0

    if (time >= 21 and time < 22):

        show time 21
        with dissolve

        pause 3.0

    if (time >= 22 and time < 23):

        show time 22
        with dissolve

        pause 3.0

    if (time >= 23 and time < 24):

        show time 23
        with dissolve

        pause 3.0

    if (time >= 24 and time < 25):

        show time 24
        with dissolve

        pause 3.0

    window show

    # Show the dialogue box.

    return 
