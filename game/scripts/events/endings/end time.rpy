# Animarathon XVI: Operation Ohio Ending Time
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

label end_time:

    play music eurobeat fadeout 1

    scene bg hallway fancy
    with dissolve

    show ann happy
    with easeinleft

    a "Gee, the first day of Animarathon sure was weird! I wonder what tomarrow will bring?"

    hide ann
    with easeoutleft

    with vpunch

    show ann happy
    with easeinleft

    a "Huh? The rave sure is loud tonight?"

    hide ann
    with easeoutleft

    with vpunch

    with vpunch

    stop music

    with hpunch

    with vpunch

    with vpunch

    scene black

    a "Huh? The power cut out?" with vpunch

    with hpunch

    with vpunch

    with vpunch

    a "Is this an earthquake?! It's really dusty?!" with vpunch

    with vpunch

    ann_thoughts "The ceiling gave out!" 

    a "{i}!!!{/i}" with vpunch
    
    ann_thoughts "{b}AHHH!{/b} I'm pinned..." with vpunch

    with vpunch

    with vpunch

    stop music

    with hpunch

    with vpunch

    with vpunch

    $ renpy.pause(60.0, hard='True')

    scene red
    with dissolve

    ann_thoughts "ha..."

    ann_thoughts "ha..."

    ann_thoughts "Nobody is coming to help..."

    ann_thoughts "The screams died a few minutes ago..."

    ann_thoughts "The sirens stopped too..."

    ann_thoughts "Even the air has left me..."

    ann_thoughts "Time to log out..."

    jump end_game_over
