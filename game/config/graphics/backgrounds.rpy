# Animarathon XVI: Operation Ohio Background Graphics Definitions
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
#  ____             _                                   _
# | __ )  __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| |___ 
# |  _ \ / _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` / __|
# | |_) | (_| | (__|   < (_| | | | (_) | |_| | | | | (_| \__ \
# |____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|___/
#                       |___/   

image bg artists alley:
    "backgrounds/artists alley.webp"

image bg atrium:
    "backgrounds/atrium.webp"

image bg blossom:
    "backgrounds/blossom.webp"

image bg building old:
    "backgrounds/building old.webp"

image bg cherry:
    "backgrounds/cherry.webp"

image bg clouds:
    "backgrounds/clouds.webp"

image bg coffee shop:
    "backgrounds/coffee shop.webp"

image bg cosplay lab:
    "backgrounds/cosplay lab.webp"

image bg film room:
    "backgrounds/film room.webp"

image bg food court:
    "backgrounds/food court.webp"

image bg garden:
    "backgrounds/garden.webp"

image bg gym:
    "backgrounds/gym.webp"

image bg hallway fancy:
    "backgrounds/hallway fancy.webp"

image bg hallway nice:
    "backgrounds/hallway nice.webp"

image bg kafe:
    "backgrounds/kafe.webp"

image bg machine:
    "backgrounds/machine.webp"

image bg panel room big theater:
    "backgrounds/panel room big theater.webp"

image bg panel room broken:
    "backgrounds/panel room broken.webp"

image bg panel room dark:
    "backgrounds/panel room dark.webp"

image bg panel room japanese:
    "backgrounds/panel room japanese.webp"

image bg panel room large:
    "backgrounds/panel room large.webp"

image bg panel room old:
    "backgrounds/panel room old.webp"

image bg panel room small:
    "backgrounds/panel room small.webp"

image bg panel room small theater:
    "backgrounds/panel room small theater.webp"

image bg panel room wet:
    "backgrounds/panel room wet.webp"

image bg peace:
    "backgrounds/peace.webp"

image bg port:
    "backgrounds/port.webp"

image bg power:
    "backgrounds/power.webp"

image bg stairway:
    "backgrounds/stairway.webp"

image bg tea room:
    "backgrounds/tea room.webp"

image bg bowling green:
    "backgrounds/bowling green.webp"

image bg tunnel:
    "backgrounds/tunnel.webp"

image bg union tower:
    "backgrounds/union tower.webp"

image bg gameover:
    "neural_style/union.webp"

# Complex Images

image bg sky:
    "sky blue"

image fight:
    "backgrounds/fight.webp"
    block:
        linear 1.0 zoom 1.1
        linear 1.0 zoom 1.0
        repeat

image crowd:
    choice:
        "backgrounds/crowd 0.webp"
    choice:
        "backgrounds/crowd 1.webp"
    choice:
        "backgrounds/crowd 2.webp"

image bg tile yellow = LiveTile("tiles/map tile.webp")

image bg rave:
    "pink"
    block:
        "pink" with dissolve
        pause (4.0)
        "orange" with dissolve
        pause (4.0)
        "yellow" with dissolve
        pause (4.0)
        "sky blue" with dissolve
        pause (4.0)
        "red" with dissolve
        pause (4.0)
        repeat

image bg splash adorina:
    "splashes/adorina.webp"

image bg splash ann:
    "splashes/ann.webp"

image bg splash frog:
    "splashes/frog.webp"

image bg splash mobobrious pi:
    "splashes/mobobrious pi.webp"

image bg splash orion:
    "splashes/orion.webp"

image bg splash sezsez:
    "splashes/sezsez.webp"

image bg splash will:
    "splashes/will.webp"

image bg character splash:
    choice:
        "bg splash adorina"
    choice:
        "bg splash ann"
    choice:
        "bg splash frog"
    choice:
        "bg splash mobobrious pi"
    choice:
        "bg splash orion"
    choice:
        "bg splash sezsez"
    choice:
        "bg splash will"

#   ___  ____  __  __ 
#  / _ \/ ___||  \/  |
# | | | \___ \| |\/| |
# | |_| |___) | |  | |
#  \___/|____/|_|  |_|

image osm 1:
    "osm/1.webp"

image osm 2:
    "osm/2.webp"

image osm 3:
    "osm/3.webp"

image osm 4:
    "osm/4.webp"

image osm 5:
    "osm/5.webp"

image osm 6:
    "osm/6.webp"
    pause (1.0)
    "osm/7.webp"
    pause (1.0)
    repeat

image osm 8:
    "osm/8.webp"

image osm 9:
    "osm/9.webp"

image osm 10:
    "osm/10.webp"

image osm 11:
    "osm/11.webp"
    pause (1.0)
    "osm/12.webp"
    pause (1.0)
    "osm/13.webp"
    pause (1.0)
    "osm/14.webp"
    pause (1.0)
    "osm/15.webp"

image osm 16:
    "osm/16.webp"

image osm 17:
    "osm/17.webp"

#  _____ _
# |_   _(_)_ __ ___   ___  ___ 
#   | | | | '_ ` _ \ / _ \/ __|
#   | | | | | | | | |  __/\__ \
#   |_| |_|_| |_| |_|\___||___/

image time 9:
    "times/9.webp"

image time 10:
    "times/10.webp"

image time 10:
    "times/10.webp"

image time 11:
    "times/11.webp"

image time 12 = LiveComposite(
    (1920, 1080),
    (0, 0), "orange",
    (-75, 200),  Text("NOON", size=700))

# I was told this is "Unreadable :p"
#"times/12.webp"

image time 13:
    "times/13.webp"

image time 14:
    "times/14.webp"

image time 15:
    "times/15.webp"

image time 16:
    "times/16.webp"

image time 17:
    "times/17.webp"

image time 18:
    "times/18.webp"

image time 19:
    "times/19.webp"

image time 20:
    "times/20.webp"

image time 21:
    "times/21.webp"

image time 22:
    "times/22.webp"

image time 23:
    "times/23.webp"

image time 24:
    "times/24.webp"
