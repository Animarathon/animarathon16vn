# Animarathon XVI: Operation Ohio In Game Schedule
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
#  ____       _              _       _      
# / ___|  ___| |__   ___  __| |_   _| | ___ 
# \___ \ / __| '_ \ / _ \/ _` | | | | |/ _ \
#  ___) | (__| | | |  __/ (_| | |_| | |  __/
# |____/ \___|_| |_|\___|\__,_|\__,_|_|\___|
screen schedule():
    
    tag menu
    
    use game_menu(_("Animarathon XVI: Schedule"), scroll="viewport"):
    
        style_prefix "schedule"

        text _("{b}Animarathon XVI: Schedule{/b}\n")
