# Animarathon XVI: Operation Ohio Game Over Ending
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

label end_game_over:

    play music promenade_medium fadeout 1

    scene orange
    with dissolve

    system "[a] died!"

    system "{size=70}End(Game);{/size}"

    show ann disgust
    with easeinbottom

    a "What the fuck?"

    hide ann disgust
    with easeoutbottom

    $ renpy.full_restart()
