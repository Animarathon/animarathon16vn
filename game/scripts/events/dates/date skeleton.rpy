# Animarathon XVI: Operation Ohio Kawaii Kafe Date: Skeleton
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

label kawaii_kafe_date_skeleton:

    show ann genki
    with easeinleft

    a "Yay! A Skeleton!"

    hide ann
    with easeinleft

    show skeleton
    with easeinright

    sk "EEEEEEEEEEE"

    hide skeleton
    with easeoutright

    show ann genki
    with easeinleft

    a "This is just like my Japanese manga, Kawaii Calcium Kun!"

    hide ann
    with easeinleft

    show skeleton
    with easeinright

    sk "EEEEEEEEEEE"

    hide skeleton
    with easeoutright

    system "[a] lost: Skin, Muscles, Internal Organs"

    system "[a] has joined Skeleton's party!"

    $ calcium_discovered = True

    ann_thoughts "The skeleton uses sign language to tell me that more anime is needed to raise the OG skeleton army."

    ann_thoughts "I also motion back in sign language that there is anime in artist's alley."

    show bg artists alley
    with dissolve

    show skeleton
    with easeinright

    sk "EEEEEEEEEEE"

    hide skeleton
    with easeoutleft

    show moe
    with easeinright

    mo "Get back here!"

    hide moe
    with easeoutright

    scene bg kafe
    with dissolve

    system "Skeleton Wins!"

    ann_thoughts "Wait! None of this is right! I'm more then my skeleton!"

    $ calcium_discovered = False

    ann_thoughts "A delusion? Did I grab the wrong bottle this morning? Get it together [a]!"

    return
