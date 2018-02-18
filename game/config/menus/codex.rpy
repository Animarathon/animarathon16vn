# Animarathon XVI: Operation Ohio Codex
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
#   ____          _           
#  / ___|___   __| | _____  __
# | |   / _ \ / _` |/ _ \ \/ /
# | |__| (_) | (_| |  __/>  < 
#  \____\___/ \__,_|\___/_/\_\
screen codex():
    
    tag menu
    
    use game_menu(_("Codex"), scroll="viewport"):
    
        style_prefix "codex"

        text _("""{b}Codex{/b}

{b}Subcultures: Anime & Otaku{/b}

{b}Anime{/b} - Japanese term for Animation.

{b}Cosplay{/b} - The art of dressing up as a character.

Although cosplay is associated with Japan, it originated in Cincinnati Ohio.

{b}Subcultures: Bowling Green{/b}

{b}ANWO{/b} - Anime In Northwest Ohio.

""")
