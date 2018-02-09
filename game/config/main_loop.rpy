 # Animarathon XVI: Operation Ohio Bowling Green Main Game Loop
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
#  __  __       _         _                      
# |  \/  | __ _(_)_ __   | |    ___   ___  _ __  
# | |\/| |/ _` | | '_ \  | |   / _ \ / _ \| '_ \ 
# | |  | | (_| | | | | | | |__| (_) | (_) | |_) |
# |_|  |_|\__,_|_|_| |_| |_____\___/ \___/| .__/ 
#                                         |_|    
# bg_ prefix indicates a portion of the game that occurs in Bowling Green, Ohio. 
# ã@Á£@çåÉ@å¢€@Õ¥@Š¢@€@š@k@Ô§@Â@@@K@×¢@}£@£@£@£@¢€¢šK@È¥@€Z%

label bg_main_loop:

    # Check to see if the game time has run out.
    if (time > 24):

        call end_time
    
    call bg_hub
    
    jump bg_main_loop
