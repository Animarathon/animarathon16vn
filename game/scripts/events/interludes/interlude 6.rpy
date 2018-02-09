# Animarathon XVI: Operation Ohio Interlude 6
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

label interlude_6:

    play music yo_p0 fadeout 1

    show frog sensei
    with easeinright

    fs "Konnichiwa Ribbit. We run marathons. We marathon anime do we not?"

    hide frog sensei
    with easeoutright

    show ann disgust
    with easeinleft

    a "Shock off [fs]! I've had it with your drek!"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "Good ribbit. Then help me end it ribbit. Even if a frog croaks at the end of a marathon, he has still won it ribbit."

    hide frog sensei
    with easeoutright

    menu:

        ann_thoughts "Help him end it? Dare I ask?"

        "Help him end it.":

            call frog_ending

        "Reject his offer.":

            show ann disgust
            with easeinleft

            a "Shock off [fs]! I've had it with your drek!"

            hide ann
            with easeoutleft

            show frog sensei
            with easeinright

            fs "You'll understand one day ribbit! Sayonara tadpole!"

            hide frog sensei
            with easeoutright

    return
