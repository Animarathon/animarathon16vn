# Animarathon XVI: Operation Ohio Kawaii Kafe Date: Ann
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

label kawaii_kafe_date_ann:

    menu:

        ann_thoughts "It says my perfect match is... myself?"

        "This isn't weird at all!":

            ann_thoughts "It looks like it allocated me sandwiches for two people by mistake."

            show ann happy
            with easeinleft

            a "A Computer error in my favor! I'll collect that extra sandwich! My actions can't be seen as theft if it was given voluntarily!"
            # Based dao message, even if it's prolly fake

            python:
                energy += 100
                hunger -= 40

        "This is awkward":

            show ann embarrassed
            with easeinleft

            a "What a bitbiter computer! This Animarathon really is a rip off."

            python:
                hunger -= 40

    hide ann
    with easeoutleft

    return
