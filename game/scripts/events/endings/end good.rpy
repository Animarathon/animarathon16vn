# Animarathon XVI: Operation Ohio Good Ending
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

label end_good:

    play music promenade_medium fadeout 1

    scene bg gameover
    with dissolve

    ann_thoughts "Animarathon was temporarily shut down during the manhunt."

    ann_thoughts "[fs] went to prison for his crimes, and was later released for good behavior."

    ann_thoughts "[o], [fs], [cm], and [kz] put aside their differences and started a boy band."

    if magical_girl == True:

        ann_thoughts "[aa] paid off ANWO's window breaking debts, then made big money through strategic investments."

    if magical_girl == False:

        ann_thoughts "[aa] paid ANWO's window breaking debts but was later jailed for fraud. The prison grew to fear her."

    ann_thoughts "The SEZSEZ gang feasted on fries, and gave out candy at the annual bird beheading."

    ann_thoughts "As for me?"

    show ann happy
    with easeinleft

    a "Well, that's a story for another day!"

    hide ann
    with easeoutleft

    system "{size=70}The End!{/size}"

    $ renpy.full_restart()
