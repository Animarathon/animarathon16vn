# Animarathon XVI: Operation Ohio Kawaii Kafe Date: Frog Sensei
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

label kawaii_kafe_date_frog_sensei:

    show frog sensei
    with easeinright

    fs "Kero Ribbit!"

    hide frog sensei
    with easeoutright

    menu:

        ann_thoughts "This is awkward."

        "Threaten":

            show ann disgust
            with easeinleft

            a "You're gonna pay for what you've done!"

            hide ann
            with easeoutleft

            show frog sensei
            with easeinright

            fs "Ribbit?"

            hide frog sensei
            with easeoutright

            show ann disgust
            with easeinleft

            a "You're a huge pain!"

            hide ann
            with easeoutleft

            show frog sensei
            with easeinright

            fs "Truce ribbit?"

            hide frog sensei
            with easeoutright

            ann_thoughts "This is getting nowhere."

        "Give [fs] the dakimakura" if (dakimakura_fs == True):

            show frog sensei
            with easeinright

            fs "Ribbit! Thank you tadpole! I'll pay you $1000 bucks for this!"

            hide frog sensei
            with easeoutright

            python:
                money += 1000
                dakimakura_fs = False

        "Leave immediately.":

            show frog sensei
            with easeinright

            fs "Ribbit?"

            hide frog sensei
            with easeoutright

    $ hunger -= 20

    return
