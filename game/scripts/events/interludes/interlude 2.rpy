# Animarathon XVI: Operation Ohio Interlude 2
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

label interlude_2:

    play music yo_p0 fadeout 1

    show frog sensei
    with easeinright

    fs "Konnichiwa Ribbit. Do you know what a convention is?"

    hide frog sensei
    with easeoutright

    show ann disgust
    with easeinleft

    a "Glitch please [fs]! Of course I know! What do you want with [o]?" with vpunch

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "A convention is more then a filthy mammal pack. It is a pact ribbit!"

    hide frog sensei
    with easeoutright

    show ann disgust
    with easeinleft

    a "Are you out of your fscking mind? What are you going on about pacts for?" with vpunch
    # $ man fsck

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "When you both signed on to this you entered a pact with us ribbit! [o] has been useful."

    if magical_girl:

        fs "Don't forget your magical girl pact with [aa] either ribbit!" with vpunch

    hide frog sensei
    with easeoutright

    show ann smug
    with easeinleft

    a "You should call your garbage collector, there's a big leak of trash coming out of your mouth! I don't give a fsck about your pacts!"
    # $ man fsck (This is to re enforce to normals that there's no typo here.)

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "Maybe one day you will understand ribbit! Sayonara tadpole!"

    hide frog sensei
    with easeoutright

    return
