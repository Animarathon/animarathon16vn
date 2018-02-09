# Animarathon XVI: Operation Ohio Small Panel Room
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

label large_panel_room:

    if time < 9:

        $ time = 9
        # Reset time to 9 (Sanity Check)

    if time >= 9 and time < 10:

        call interlude_1

        call cosplay

        call interlude_2

        $ time_factor = 1
        call advance_time

        return

    if time >= 10 and time < 12:

        ann_thoughts "There are no ongoing panels. Better head to the Kawaii Kafe."

        call kawaii_kafe

        $ time_factor = 2
        call advance_time

        return

    if time >= 12 and time < 14:

        call interlude_3
    
        call gpm

        call interlude_4

        $ time_factor = 2
        call advance_time

        return

    if time >= 14 and time < 15:

        ann_thoughts "There are no ongoing panels. Better head to the Group Photo."

        call satellite_group_picture

        $ time_factor = 1
        call advance_time

        return

    if time >= 15 and time < 17:

        call interlude_5
    
        call trash

        call interlude_6

        $ time_factor = 2
        call advance_time

        return

    if time >= 17 and time < 20:

        call interlude_7
    
        call robot

        $ time_factor = 3
        call advance_time

        return

    if time >= 20 and time <= 24:

        ann_thoughts "There aren't any ongoing panels here. Animarathon is wrapping up for the night."

        jump end_time

    if time > 24:

        ann_thoughts "There aren't any ongoing panels here. Animarathon is over for the night."

        jump end_time

    return
