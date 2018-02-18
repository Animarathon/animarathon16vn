# Animarathon XVI: Operation Ohio Item Graphics Definitions
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
#  ___ _                     
# |_ _| |_ ___ _ __ ___  ___ 
#  | || __/ _ \ '_ ` _ \/ __|
#  | || ||  __/ | | | | \__ \
# |___|\__\___|_| |_| |_|___/

#  _____               _ 
# |  ___|__   ___   __| |
# | |_ / _ \ / _ \ / _` |
# |  _| (_) | (_) | (_| |
# |_|  \___/ \___/ \__,_|

image candy:
    "items/candy.webp"
    subpixel True

    block:

        linear 5.0 xzoom 0.7

        linear 5.0 xzoom 1.3

        repeat

#  ____        _       
# |  _ \ _   _| |_ __  
# | |_) | | | | | '_ \ 
# |  __/| |_| | | |_) |
# |_|    \__,_|_| .__/ 
#               |_|    

image sezsez note:
    "items/sezseznote.webp"
    subpixel True
    block:
        linear 5.0 xzoom 0.7
        linear 5.0 xzoom 1.3
        repeat

image manga frog sensei:
    "kirsten_art/manga frog sensei.webp"

#   ____                            _                
#  / ___|___  _ __ ___  _ __  _   _| |_ ___ _ __ ___ 
# | |   / _ \| '_ ` _ \| '_ \| | | | __/ _ \ '__/ __|
# | |__| (_) | | | | | | |_) | |_| | ||  __/ |  \__ \
#  \____\___/|_| |_| |_| .__/ \__,_|\__\___|_|  |___/
#                      |_|                           

image panda:
    "items/panda.webp"

image shooting star off:
    "items/minicomp.webp"

image shooting star on:
    block:

        choice (5.0):
            "items/minicomp 0.webp"
            pause 0.2

        choice (10.0):
            "items/minicomp 1.webp"
            pause 0.2

        choice (1.0):
            "items/minicomp 2.webp"
            pause 0.2

        choice (0.1):
            "items/minicomp.webp"
            pause 0.5

    repeat

#  ____       _           _       
# |  _ \ ___ | |__   ___ | |_ ___ 
# | |_) / _ \| '_ \ / _ \| __/ __|
# |  _ < (_) | |_) | (_) | |_\__ \
# |_| \_\___/|_.__/ \___/ \__|___/

image cleaning robot:
    "items/cleaning robot.webp"

image ball robot:
    "items/robot ball.webp"

image moe mecha:
    "items/moe mecha.webp"
    block:

        linear 0.1 yzoom 0.95

        linear 0.1 yzoom 1.0

        repeat

# __     __   _     _      _           
# \ \   / /__| |__ (_) ___| | ___  ___ 
#  \ \ / / _ \ '_ \| |/ __| |/ _ \/ __|
#   \ V /  __/ | | | | (__| |  __/\__ \
#    \_/ \___|_| |_|_|\___|_|\___||___/

image plane:
    "items/plane.webp"

image plane takeoff:
    "items/plane.webp"
    rotate 15

image plane fly:
    "items/plane fly.webp"
    block:
        rotate 0
        linear 1.0 rotate 15
        linear 1.0 rotate 0
        repeat

image police car:
    "items/police car.webp"

#  ____        _    _                 _
# |  _ \  __ _| | _(_)_ __ ___   __ _| | ___   _ _ __ __ _ 
# | | | |/ _` | |/ / | '_ ` _ \ / _` | |/ / | | | '__/ _` |
# | |_| | (_| |   <| | | | | | | (_| |   <| |_| | | | (_| |
# |____/ \__,_|_|\_\_|_| |_| |_|\__,_|_|\_\\__,_|_|  \__,_|

image dakimakura base:
    "items/dakimakura.webp"

image dakimakura ann scale:
    "ann happy composite"
    xzoom 0.60
    yzoom 0.60

image dakimakura fs scale:
    "characters/frog sensei/frog sensei happy.webp"
    xzoom 0.50
    yzoom 0.50

image dakimakura ann = LiveComposite(
    (1920, 1080),
    (600, 45), "dakimakura base",
    (360, 70), "dakimakura ann scale")

image dakimakura fs = LiveComposite(
    (1920, 1080),
    (600, 45), "dakimakura base",
    (640, 100), "dakimakura fs scale")
