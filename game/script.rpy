# Animarathon XVI: Operation Ohio Setup
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
#
# About script.rpy
#
# "label start" is special.
# Ren'Py uses it to show where the game script starts after initialization.
#
# Text is then printed to the terminal. Users shouldn't see it in game.
# It's purpose is to indicate that init went ok, and the game did start.
# 
# The game then begins the pre game setup process.
# (Player interactions before the main game loop begins.)

label start:

    # Terminal output
    python:
        print('Animarathon XVI has started!')
        print('Enjoy the convention!')
        print('Special Thanks to the Creative Commons Artists!')
        print('Programmer, Artist, and Writer: Maxwell Paul Brickner')
        print('Frog Writer: Alex Danny Kidd')
        print('Skeleton Artist: Kirsten McLaughlin')
    
    jump pre_game
