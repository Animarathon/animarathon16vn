# Animarathon XVI: Operation Ohio Python Configuration
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
#  ____        _   _                 
# |  _ \ _   _| |_| |__   ___  _ __  
# | |_) | | | | __| '_ \ / _ \| '_ \ 
# |  __/| |_| | |_| | | | (_) | | | |
# |_|    \__, |\__|_| |_|\___/|_| |_|
#        |___/                       

init python:

    #  __  __       _   _     
    # |  \/  | __ _| |_| |__  
    # | |\/| |/ _` | __| '_ \ 
    # | |  | | (_| | |_| | | |
    # |_|  |_|\__,_|\__|_| |_|
    # The math module is needed for pachinko effects.
    import math
    
    #  ____       _ _ _                _   
    # |  _ \ ___ | | | |__   __ _  ___| | __
    # | |_) / _ \| | | '_ \ / _` |/ __| |/ /
    # |  _ < (_) | | | |_) | (_| | (__|   < 
    # |_| \_\___/|_|_|_.__/ \__,_|\___|_|\_\                                  
    # Keep rollback enabled during most of the game for player convenience.
    # Explicitly disable rollback for pachinko to avoid crashing the game.
    
    config.rollback_enabled = True

    #  ____                 _                         __  __           _
    # |  _ \  _____   _____| | ___  _ __   ___ _ __  |  \/  | ___   __| | ___ 
    # | | | |/ _ \ \ / / _ \ |/ _ \| '_ \ / _ \ '__| | |\/| |/ _ \ / _` |/ _ \
    # | |_| |  __/\ V /  __/ | (_) | |_) |  __/ |    | |  | | (_) | (_| |  __/
    # |____/ \___| \_/ \___|_|\___/| .__/ \___|_|    |_|  |_|\___/ \__,_|\___|
    #                              |_|
    # Set to false when distributing to disable developer mode.

    config.developer = True

    # __        __   _    ____                           
    # \ \      / /__| |__/ ___|  ___ _ ____   _____ _ __ 
    #  \ \ /\ / / _ \ '_ \___ \ / _ \ '__\ \ / / _ \ '__|
    #   \ V  V /  __/ |_) |__) |  __/ |   \ V /  __/ |
    #    \_/\_/ \___|_.__/____/ \___|_|    \_/ \___|_|
    # Deal with CORS or assets will not load! Holy Toledo web devs!
    # Alas! SimpleHTTPServer isn't playing nice with Ren'Py! The Humanity!
    # Who could have forseen that a webserver would not play nice with a VN?
    # Ren'Py uses python 2.x not 3.x. If that changes please use http.server.

label update_fov:
    #  _____    _ _ _     _____ _ _
    # | ____|__| (_) |_  |  ___(_) | ___ 
    # |  _| / _` | | __| | |_  | | |/ _ \
    # | |__| (_| | | |_  |  _| | | |  __/
    # |_____\__,_|_|\__| |_|   |_|_|\___|
    python:
        vrfile = open("deverse ebook.html", "a")
        # TODO: Search for fov="80" and update it with fov="fov"
        vrfile.close()
    return
