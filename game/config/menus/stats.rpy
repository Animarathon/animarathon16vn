# Animarathon XVI: Operation Ohio Stats Screen
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
#  ____  _        _         ____                           
# / ___|| |_ __ _| |_ ___  / ___|  ___ _ __ ___  ___ _ __  
# \___ \| __/ _` | __/ __| \___ \ / __| '__/ _ \/ _ \ '_ \ 
#  ___) | || (_| | |_\__ \  ___) | (__| | |  __/  __/ | | |
# |____/ \__\__,_|\__|___/ |____/ \___|_|  \___|\___|_| |_|
screen stats():
    
    tag menu
    
    use game_menu(_("stats"), scroll="viewport"):
    
        style_prefix "stats"

        text _("{b}Quick Stats!{/b}\n")

        if time < 12:
    
            text _("The time is [time] AM")
    
        if time == 12:
    
            text _("The time is high noon")
    
        # Ren'Py acts up if you use [time-12]. Do calculations outside output.

        if time > 12 and time < 24:

            $ temp_time = time - 12

            text _("The time is [temp_time] PM")
    
        if time == 24:
    
            text _("{b}Time: {/b} [Midnight]")
    
        if (time > 24) and (time <= 36):

            $ temp_time = time - 24

            text _("The time is [temp_time] AM")
    
        if (time > 36):
    
            text _(" Time System Error.")

        if (time < 9):
    
            text _(" Time System Error.")

        text _("{b}Money: {/b}$[money]")

        if pachinko_discovered:

            text _("{b}Pachinko Balls: {/b}[pachinko_balls]")

        text _("\n\n{b}Physiological/Psychological Profile.{/b}\n")

        text _("{b}Name: {/b}Ann Ferrone.\n")

        text _("{b}Age: {/b}21\n")

        text _("{b}Height: {/b}1.87 Meters\n")

        text _("{b}Weight: {/b}72 kg\n")

        text _("{b}Blood Type: {/b}A+\n")


        if hunger <= 0:
            text _("{b}Hunger: {/b}Not Hungry ")
            
        if ((hunger <= 50) & (hunger > 0)):
            text _("{b}Hunger: {/b}A Little Hungry ")
            
        if ((hunger > 50)):
            text _("{b}Hunger: {/b}Hungry ")


        if energy >= 75:
            text _("{b}Energy: {/b}Perky ")
            
        if ((energy <= 75) & (energy > 50)):
            text _("{b}Energy: {/b}Alert ")
            
        if ((energy <= 50) & (energy > 25)):
            text _("{b}Energy: {/b}Fatigued ")
            
        if ((energy < 25)):
            text _("{b}Energy: {/b}Sleepy ")

            
        if drunkenness <= 0:
            text _("{b}Sobriety: {/b}Sober ")
            
        if ((drunkenness <= 50) & (drunkenness > 0)):
            text _("{b}Sobriety: {/b} Buzzed ")
            
        if ((drunkenness > 50)):
            text _("{b}Sobriety: {/b} Drunk ")

            
        if calcium_discovered:
            text _("{b}Calciums: {/b} [calcium]")

        if buff:
            text _("{b}Buff: {/b}Temporarily Buff.\n") 
