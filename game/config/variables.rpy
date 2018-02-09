# Animarathon XVI: Operation Ohio Variable Assignment
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
# __     __         _       _     _           
# \ \   / /_ _ _ __(_) __ _| |__ | | ___  ___ 
#  \ \ / / _` | '__| |/ _` | '_ \| |/ _ \/ __|
#   \ V / (_| | |  | | (_| | |_) | |  __/\__ \
#    \_/ \__,_|_|  |_|\__,_|_.__/|_|\___||___/
# This script assigns variables the game uses.

# "default" is used before a variable name to maintain compatibility with older save files.

#  _____ _                
# |_   _(_)_ __ ___   ___ 
#   | | | | '_ ` _ \ / _ \
#   | | | | | | | | |  __/
#   |_| |_|_| |_| |_|\___|
# The time of the game, in hours.

# WARNING
# Currently game logic only uses whole ints.
# Floats should be ok, but are not tested. Prerendered graphics may need changed in some cases.

# WARNING
# Times are on a 24 hour system for one single day.
# If the game is to extend beyond that, decrement the time back to 9 or rework this system.

# How times work.
# Using integers
# 9 would equate to 9:00AM
# 13 would equate to 1:00PM

# Using floats. (Not Planned)
# 9.5 would equate to 9:30AM
# 9 + half an hour

default time = 9
# Int (May be changed to Float later)

default time_factor = 1
# Int
# The time factor is the amount of time that passes after an event.
# If the time factor is set to 1, 1 hour will pass.

default temp_time = 0
# Float
# For display purposes ONLY!

default panels = 0
# Int
# The number of panels that have taken place.
# Game critical logic should use this number, and not time.

#  ____       _           _                 
# / ___|  ___| | ___  ___| |_ ___  _ __ ___ 
# \___ \ / _ \ |/ _ \/ __| __/ _ \| '__/ __|
#  ___) |  __/ |  __/ (__| || (_) | |  \__ \
# |____/ \___|_|\___|\___|\__\___/|_|  |___/

default difficulty_factor = 5
# The difficulty factor determines how quickly player stats degrade.
# Int

default fov = 80
# Determines the Field of View to be used in A-Frame
# Should have no effect in Ren'Py itself
# Float

#  _____ _                         _____         _   
# |  ___| | __ ___   _____  _ __  |_   _|____  _| |_ 
# | |_  | |/ _` \ \ / / _ \| '__|   | |/ _ \ \/ / __|
# |  _| | | (_| |\ V / (_) | |      | |  __/>  <| |_ 
# |_|   |_|\__,_| \_/ \___/|_|      |_|\___/_/\_\\__|
# The player can set these to something else.

# WARNING:
# These variables do not affect gameplay, but they are still expected!
# Removing them might break the game!

default favorite_anime = "Magical Man M'onsieur"
# String
# Ann's Favorite anime.

default online_handle = "Ann_i_meme_xXx_BGxTSUN_xXx_1337"
# String
# Meant to represent a username on in game "Websites"

# default reset_favorite_anime = "Magical Man M'onsieur"
# String
# Ann's Favorite anime.

default reset_online_handle = "Ann_i_meme_xXx_BGxTSUN_xXx_1337"
# String
# Meant to represent a username on in game "Websites"

# default reset_power_code = "419-352-8475"
# String
# Meant to represent a username on in game "Websites"

#  ____  _        _       
# / ___|| |_ __ _| |_ ___ 
# \___ \| __/ _` | __/ __|
#  ___) | || (_| | |_\__ \
# |____/ \__\__,_|\__|___/

default hunger = 1
# Int
# As Hunger decreases the player is rewarded.
# As Hunger increases the player is punished.

default energy = 100
# Int
# As Energy decreases the player is punished with worse timing windows in pachinko.
# As Energy increases the player is rewarded with better timing windows in pachinko.
    
default drunkenness = 0
# Int
# As drunkenness increases plot elements are triggered.

default money = 42.00
# Float
# The player can spend money to acquire items.

default magical_girl_earnings = 0
# Float
# The money the player has earned from magical girl actions.

default reset_money = money
# Float
# The amount of money the player starts with.

default pachinko_balls = 0
# Int
# The number of pachinko balls a player has.
# When the player reaches 0 pachinko balls, a game over is triggered on encounter with a bouncer.

default calcium = 42
# Int
# Calcium is a vanity stat for a gag.

default cleverness = 0
# Int
# Increased when the player uses cleverness to get out of problems.
# Invisible to player

default negotiation = 0
# Int
# Increased when the player negotiates out of problems.
# Invisible to player

default intimidation = 0
# Int
# Increased when the player confronts problems through intimidation.
# Invisible to player

default aggression = 0
# Int
# Increased when the player confronts problems with violence.
# Invisible to player

default vivid_dreams = False
# Bool
# False for short dreams. True for Vivid ones

default buff = False
# Bool
# Learned from GPM. Can be used to get stronger.

default magical_girl = False
# Bool
# Determines if Ann is a Magical Girl or not. 

#  _____ _                 
# |  ___| | __ _  __ _ ___ 
# | |_  | |/ _` |/ _` / __|
# |  _| | | (_| | (_| \__ \
# |_|   |_|\__,_|\__, |___/
#                |___/     

default power_code = False
# Bool
# If the power code from the power chip has been entered or not.

default tutorial = False
# Bool
# If they player has completed the entire tutorial or not.

default pachinko_discovered = False
# Bool
# If Ann has learned about Pachinko yet.
# Use this to hide interface spoilers.

default twenty_dollars = False
# Bool
# If Ann has made a deal with Adorina to get her twenty dollars back.

default calcium_discovered = False
# Bool
# If Ann has joined the Skeletons Party.

default kopi_first = False
# Bool
# If ann has been to kopi before in this game.

default rays_first = False
# Bool
# If ann has been to rays before in this game.

default pachinko_jester_known = False
# Bool
# If ann has seen the pachinko jester before.

default pachinko_jester_story = False
# Bool
# If the Pachinko Jester has told Ann his Story.

default ska_ecchi_story = False
# Bool
# If Ska Ecchi has told Ann his "Story".
    
default mo_manga_intro = False
# Bool
# If Moe has explained manga to ann.
    
default mo_story = False
# Bool
# If Moe has told Ann her story.
    
default mo_mission = False
# Bool
# If Moe has entrusted ann to take on Frog Sensei.
    
default mo_gold = False
# Bool
# If Moe has used her gold marker.

default cardboard_box = False
# Bool

default geraldo_met = False
# Bool
# If ann has met Geraldo Gonzo.

default sezsez_met = False
# Bool
# If ann has met SEZSEZ.

default coupon_entered = False
# Bool
# If ann has used the coupon.

#  ____                  _   _____ _                 
# |  _ \ __ _ _ __   ___| | |  ___| | __ _  __ _ ___ 
# | |_) / _` | '_ \ / _ \ | | |_  | |/ _` |/ _` / __|
# |  __/ (_| | | | |  __/ | |  _| | | (_| | (_| \__ \
# |_|   \__,_|_| |_|\___|_| |_|   |_|\__,_|\__, |___/
#                                          |___/     

#  ____                  _    ____                _             
# |  _ \ __ _ _ __   ___| |  / ___|___  ___ _ __ | | __ _ _   _ 
# | |_) / _` | '_ \ / _ \ | | |   / _ \/ __| '_ \| |/ _` | | | |
# |  __/ (_| | | | |  __/ | | |__| (_) \__ \ |_) | | (_| | |_| |
# |_|   \__,_|_| |_|\___|_|  \____\___/|___/ .__/|_|\__,_|\__, |
#                                          |_|            |___/ 

default what_is_cosplay = False
# Bool
# Weather or not the player got the first question about cosplay correct.

#  ____                  _   _   _                 _ _      
# |  _ \ __ _ _ __   ___| | | \ | | ___   ___   __| | | ___ 
# | |_) / _` | '_ \ / _ \ | |  \| |/ _ \ / _ \ / _` | |/ _ \
# |  __/ (_| | | | |  __/ | | |\  | (_) | (_) | (_| | |  __/
# |_|   \__,_|_| |_|\___|_| |_| \_|\___/ \___/ \__,_|_|\___|

default custard_job_accept = False
# Bool
# Weather or not the player has taken the job from Mr. Custard.
# True indicates the job has been taken.

default paz_ta_date = False
# Bool
# Whether or not the player has accepted a date with Paz Ta.
# Note that this is different from the custard quest.
# True indicates the date has been accepted.

default paz_ta_nyotaimori = False
# Bool
# Whether or not the player has accepted the nyotaimori job from Mr. Custard.


#  ____                  _    ____ ____  __  __ 
# |  _ \ __ _ _ __   ___| |  / ___|  _ \|  \/  |
# | |_) / _` | '_ \ / _ \ | | |  _| |_) | |\/| |
# |  __/ (_| | | | |  __/ | | |_| |  __/| |  | |
# |_|   \__,_|_| |_|\___|_|  \____|_|   |_|  |_|

default haunted_ebook = True
# BOOl
# Allows GPM's online alter ego to have his time in the spot light

default haunted_radio = False
# BOOl
# Don't enable this. I don't think a successful implementation of this would be safe in some cases.
# Besides I don't think this works well enough, and most players would never notice.
# The idea was to do something like 1970's S100 computers and use EMI to play music.
# Interferes AM radio transmission at 560,000 Hz. The longer the cord leading to the speakers the better.
# Check yourself before you Van Eck yourself!

#  ____                                    
# |  _ \ _ __ ___   __ _ _ __ ___  ___ ___ 
# | |_) | '__/ _ \ / _` | '__/ _ \/ __/ __|
# |  __/| | | (_) | (_| | | |  __/\__ \__ \
# |_|   |_|  \___/ \__, |_|  \___||___/___/
#                  |___/                   

default food_progress = 0
# Int

default frog_progress = 0
# Int

default sezsez_progress = 0
# Bool

#  ____  _        _                 
# / ___|| |_ _ __(_)_ __   __ _ ___ 
# \___ \| __| '__| | '_ \ / _` / __|
#  ___) | |_| |  | | | | | (_| \__ \
# |____/ \__|_|  |_|_| |_|\__, |___/
#                         |___/     

default coupon_code = "0xffbff950"
# String

default last_ordered = "Nothing"
# String

default kawaii_selection = "Nothing"
# String

#  ___                      _                   
# |_ _|_ ____   _____ _ __ | |_ ___  _ __ _   _ 
#  | || '_ \ \ / / _ \ '_ \| __/ _ \| '__| | | |
#  | || | | \ V /  __/ | | | || (_) | |  | |_| |
# |___|_| |_|\_/ \___|_| |_|\__\___/|_|   \__, |
#                                         |___/ 
    
default favorite_anime_price = 94.13
# Float
    
default favorite_anime_get = False # Normal Item system isn't working for some reason and I'm out of time.
# Bool
    
default dirk_manning_anime_price = 74.80
# Float

default dirk_manning_anime_get = False # Normal Item system isn't working for some reason and I'm out of time.
# Bool

default tadpole_sensei_manga = False
# Bool

default tadpole_sensei_price = 0.00
# Float

default kawaii_calcium_manga = False
# Bool

default kawaii_calcium_price = 0.00
# Float

default welchert_anime = False
# Bool

default dakimakura_price = 99.99
# Float

default dakimakura_ann = False
# Bool
# If ann has a dakimakura of herself.

default dakimakura_fs = False
# Bool
# If ann has a dakimakura of Frog Sensei.

default has_robot = False
# Bool

#  ____       _               
# |  _ \ _ __(_) ___ ___  ___ 
# | |_) | '__| |/ __/ _ \/ __|
# |  __/| |  | | (_|  __/\__ \
# |_|   |_|  |_|\___\___||___/
# Price Formats
# (Price) Float
# (Number Consumed) Int

#  _____               _ 
# |  ___|__   ___   __| |
# | |_ / _ \ / _ \ / _` |
# |  _| (_) | (_) | (_| |
# |_|  \___/ \___/ \__,_|

    
default pizza_pie_price = 1.39
default pizza_pie_consumed = 0
    
default ravs_price = 0.49
default ravs_consumed = 0
    
default fries_price = 0.24
default fries_consumed = 0
    
default cheez_price = 0.17
default cheez_consumed = 0
    
default sun_price = 0.11
default sun_consumed = 0
    
default satay_price = 0.99
default satay_consumed = 0
    
default mee_price = 1.00
default mee_consumed = 0
    
default roti_price = 1.00
default roti_consumed = 0
    
default char_price = 1.00
default char_consumed = 0

default malay_burger_price = 1.99
default malay_burger_consumed = 0

default kek_price = 3.99
default kek_consumed = 0
    
default ABC_price = 2.99
default ABC_consumed = 0

default waffle_price = 2.99
default waffle_consumed = 0

#  __  __       _   _    __     ___                 _   ____       _               
# |  \/  | __ _| |_| |_  \ \   / (_)___ _   _  __ _| | |  _ \ _ __(_) ___ ___  ___ 
# | |\/| |/ _` | __| __|  \ \ / /| / __| | | |/ _` | | | |_) | '__| |/ __/ _ \/ __|
# | |  | | (_| | |_| |_    \ V / | \__ \ |_| | (_| | | |  __/| |  | | (_|  __/\__ \
# |_|  |_|\__,_|\__|\__|    \_/  |_|___/\__,_|\__,_|_| |_|   |_|  |_|\___\___||___/

default ginger_ale_price = 0.59
default ginger_ale_consumed = 0
    
#   ____       __  __               _____            ____       _               
#  / ___|___  / _|/ _| ___  ___   _|_   _|__  __ _  |  _ \ _ __(_) ___ ___  ___ 
# | |   / _ \| |_| |_ / _ \/ _ \_| |_| |/ _ \/ _` | | |_) | '__| |/ __/ _ \/ __|
# | |__| (_) |  _|  _|  __/  __/_   _| |  __/ (_| | |  __/| |  | | (_|  __/\__ \
#  \____\___/|_| |_|  \___|\___| |_| |_|\___|\__,_| |_|   |_|  |_|\___\___||___/
 
default coffee_price = 0.99
default coffee_consumed = 0
    
default teh_price = 0.99
default teh_consumed = 0
    
#     _    _           _           _   ____       _               
#    / \  | | ___ ___ | |__   ___ | | |  _ \ _ __(_) ___ ___  ___ 
#   / _ \ | |/ __/ _ \| '_ \ / _ \| | | |_) | '__| |/ __/ _ \/ __|
#  / ___ \| | (_| (_) | | | | (_) | | |  __/| |  | | (_|  __/\__ \
# /_/   \_\_|\___\___/|_| |_|\___/|_| |_|   |_|  |_|\___\___||___/

default beer_price = 3.99
default beer_consumed = 0
    
default cider_price = 3.99
default cider_consumed = 0
    
default wine_price = 6.99
default wine_consumed = 0
    
default sake_price = 7.99
default sake_consumed = 0

default erie_highball_price = 0.25
default erie_highball_consumed = 0
