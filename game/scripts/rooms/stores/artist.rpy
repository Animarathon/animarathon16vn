# Animarathon XVI: Operation Ohio Artist Alley
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

label artist:

    play music orange_beach fadeout 1

    scene bg artists alley
    with dissolve

    jump artist_menu

label artist_menu:

    menu:

        ann_thoughts "What should I do in Artist's Alley?"

        "Buy pachinko balls":

            call artist_ska

        "Sell pachinko balls":

            call artist_pachinko_jester

        "Buy anime merchandise":

            call artist_moe

        "It's time to leave":

            return

    jump artist_menu
