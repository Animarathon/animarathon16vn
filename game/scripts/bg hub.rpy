# Animarathon XVI: Operation Ohio Bowling Green Hub
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

label bg_hub:

    play music breathe_short fadeout 1

    call display_time
    # Show the time to the player

    scene sky blue
    with dissolve
    show bg tile yellow
    with dissolve
    # Create a tiled background

    show union3d at left
    # Show the union map.

    show side_schedule at right
    # Show a schedule to help the player make decisions.

    window hide None
    # This hides the textbox to make room for the GUI.

    pause(1.0)

    call screen hub_buttons
    # Create the button interface

    window show None
    # This returns the textbox.

    # __        __               _
    # \ \      / /_ _ _ __ _ __ (_)_ __   __ _ 
    #  \ \ /\ / / _` | '__| '_ \| | '_ \ / _` |
    #   \ V  V / (_| | |  | | | | | | | | (_| |
    #    \_/\_/ \__,_|_|  |_| |_|_|_| |_|\__, |
    #                                    |___/ 
    # returned strings must be exactly the same!
    # If "food" is returned and you check for "Food" you'll fail!

    # Enabled Rooms

    if _return == "large panel room":

        hide union3d with dissolve

        hide side_schedule with dissolve

        call large_panel_room

    if _return == "small panel room":

        hide union3d with dissolve

        hide side_schedule with dissolve

        call small_panel_room

    if _return == "artist":

        hide union3d with dissolve

        hide side_schedule with dissolve

        call artist

    if _return == "food":

        hide union3d with dissolve

        hide side_schedule with dissolve

        call food

    if _return == "coffee":

        hide union3d with dissolve

        hide side_schedule with dissolve

        call coffee

    if _return == "fourth floor":

        hide union3d with dissolve

        hide side_schedule with dissolve

        call fourth_floor

    if _return == "kawaii":

        hide union3d with dissolve

        hide side_schedule with dissolve

        call kawaii_kafe

        $ time_factor = 2
        call advance_time

    # Disabled Rooms

    #if _return == "game":
    #
    #    call gaming

    #if _return == "pub":
    #
    #    call pub

    # Return to the main loop
    return

#  _   _ _   _ ____     ____ _   _ ___ 
# | | | | | | | __ )   / ___| | | |_ _|
# | |_| | | | |  _ \  | |  _| | | || | 
# |  _  | |_| | |_) | | |_| | |_| || | 
# |_| |_|\___/|____/   \____|\___/|___|
screen hub_buttons:

    # First Floor

    if False:
        textbutton ("{image=pub icon}"):

            xpos 120

            xanchor 0.5

            ypos 780

            yanchor 0.5

            action Return("pub")

    if True:
        textbutton ("{image=coffee icon}"):

            xpos 250

            xanchor 0.5

            ypos 850

            yanchor 0.5

            action Return("coffee")

    if True:
        textbutton ("{image=food icon}"):

            xpos 350

            xanchor 0.5

            ypos 750

            yanchor 0.5

            action Return("food")

    # Second Floor

    if True:
        textbutton ("{image=aa icon}"):

            xpos 350

            xanchor 0.5

            ypos 580

            yanchor 0.5

            action Return("artist")

    if (time >= 10) and (time < 12):
        textbutton ("{image=kawaii icon}"):

            xpos 500

            xanchor 0.5

            ypos 620

            yanchor 0.5

            action Return("kawaii")

    if True:
        textbutton ("{image=large icon}"):

            xpos 700

            xanchor 0.5

            ypos 530

            yanchor 0.5

            action Return("large panel room")

    # Third Floor

    if True:
        textbutton ("{image=small icon}"):

            xpos 640

            xanchor 0.5

            ypos 400

            yanchor 0.5

            action Return("small panel room")

    if False:
        textbutton ("{image=game icon}"):

            xpos 300

            xanchor 0.5

            ypos 450

            yanchor 0.5

            action Return("game")

    # Fourth Floor

    if True:
        textbutton ("{image=4 unselected icon}"):

            xpos 450

            xanchor 0.5

            ypos 230

            yanchor 0.5

            action Return("fourth floor")
