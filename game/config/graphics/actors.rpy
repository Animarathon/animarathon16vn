# Animarathon XVI: Operation Ohio Character Graphics Definitions
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
#   ____ _                          _                
#  / ___| |__   __ _ _ __ __ _  ___| |_ ___ _ __ ___ 
# | |   | '_ \ / _` | '__/ _` |/ __| __/ _ \ '__/ __|
# | |___| | | | (_| | | | (_| | (__| ||  __/ |  \__ \
#  \____|_| |_|\__,_|_|  \__,_|\___|\__\___|_|  |___/
# Note:
# Left and right here refer to the side of the screen the characters are shown.
# NOT what direction they are facing.
# Character graphics should enter stage right facing left.
# The Player Character (Ann) should always enter stage left facing right.
#
# There is a lot of boiler plate code in here due to some choices I've made.
# You probably shouldn't structure a typical visual novel like this.

#  ____       _
# |  _ \ _ __(_)_ __ ___   __ _ _ __ _   _ 
# | |_) | '__| | '_ ` _ \ / _` | '__| | | |
# |  __/| |  | | | | | | | (_| | |  | |_| |
# |_|   |_|  |_|_| |_| |_|\__,_|_|   \__, |
#                                    |___/ 

#     _                
#    / \   _ __  _ __  
#   / _ \ | '_ \| '_ \ 
#  / ___ \| | | | | | |
# /_/   \_\_| |_|_| |_|
# Artist: Maxwell Paul Brickner
# Based on the traditional ANO mascot

# As the main character, Ann images are special.
# They should always appear on the left.
# Other characters should always appear on the right.
# This creates a clear structure for the player, you and them.

# Body Parts

# Always use lossless webp for ann for crisp details.
# The player will spend more time looking at her.
# Over other characters, especially minor ones.

# Common

image ann face happy:
    "characters/ann/ann face happy.webp"
    xzoom -1.0
    subpixel True

image ann torso:
    "characters/ann/ann torso.webp"
    xzoom -1.0
    subpixel True

image ann head:
    "characters/ann/ann head.webp"
    xzoom -1.0
    subpixel True

image ann head embarrassed raw = im.MatrixColor(
    "characters/ann/ann head.webp",
    im.matrix.tint(1.0, 0.5, 0.5))
# Changes color to red.

image ann head embarrassed:
    "ann head embarrassed raw"
    xzoom -1.0
    subpixel True

image ann arm left:
    "characters/ann/ann arm left.webp"
    xzoom -1.0
    subpixel True

image ann arm right:
    "characters/ann/ann arm right.webp"
    xzoom -1.0
    subpixel True

image ann hair bg:
    "characters/ann/ann hair bg.webp"
    xzoom -1.0
    subpixel True

image ann hair fg:
    "characters/ann/ann hair fg.webp"
    xzoom -1.0
    subpixel True

image ann eyebrow right:
    "characters/ann/ann eyebrow right.webp"
    xzoom -1.0
    subpixel True

image ann eyebrow left:
    "characters/ann/ann eyebrow left.webp"
    xzoom -1.0
    subpixel True

# Smug Parts

image ann face smug:
    "characters/ann/ann face smug.webp"
    xzoom -1.0
    rotate -20.0
    subpixel True

image ann head smug:
    "characters/ann/ann head.webp"
    xzoom -1.0
    rotate -20.0
    subpixel True

image ann hair bg smug:
    "characters/ann/ann hair bg.webp"
    xzoom -1.0
    rotate -20.0
    subpixel True

image ann hair fg smug:
    "characters/ann/ann hair fg.webp"
    xzoom -1.0
    rotate -20.0
    subpixel True

image ann eyebrow right smug:
    "characters/ann/ann eyebrow right.webp"
    xzoom -1.0
    rotate -20.0
    subpixel True

image ann eyebrow left smug:
    "characters/ann/ann eyebrow left.webp"
    xzoom -1.0
    rotate -20.0
    subpixel True

# Faces

image ann face normal:
    "characters/ann/ann face normal.webp"
    xzoom -1.0
    subpixel True

image ann face disgust:
    "characters/ann/ann face disgust.webp"
    xzoom -1.0
    subpixel True

image ann face genki:
    "characters/ann/ann face genki.webp"
    xzoom -1.0
    subpixel True

image ann face toast:
    "characters/ann/ann face toast.webp"
    xzoom -1.0
    subpixel True

# Composition

# image ann = "ann normal"

image ann normal composite = LiveComposite(
    (1920, 1080),
    (640, 20), "ann hair bg",
    (521, 799), "ann arm left",
    (990, 800), "ann arm right",
    (640, 550), "ann torso",
    (745, 100), "ann head",
    (780, 230), "ann face normal",
    (800, 175), "ann eyebrow left",
    (1050, 200), "ann eyebrow right",
    (677, 69), "ann hair fg")

image ann normal:
    "ann normal composite"
    yalign 0.5
    subpixel True
    block:
        easeout 60.0 rotate 1.0
        easeout 60.0 rotate -1.0
        repeat

image ann happy composite = LiveComposite(
    (1920, 1080),
    (640, 20), "ann hair bg",
    (521, 799), "ann arm left",
    (990, 800), "ann arm right",
    (640, 550), "ann torso",
    (745, 100), "ann head",
    (780, 230), "ann face happy",
    (800, 175), "ann eyebrow left",
    (1050, 200), "ann eyebrow right",
    (677, 69), "ann hair fg")

image ann happy:
    "ann happy composite"
    yalign 0.5
    subpixel True
    block:
        easeout 60.0 rotate 4.0
        easeout 60.0 rotate -4.0
        repeat

image ann smug composite = LiveComposite(
    (1920, 1080),
    (420, -130), "ann hair bg smug",
    (521, 799), "ann arm left",
    (990, 800), "ann arm right",
    (640, 550), "ann torso",
    (530, 0), "ann head smug",
    (650, 120), "ann face smug",
    (650, 155), "ann eyebrow left smug",
    (910, 90), "ann eyebrow right smug",
    (470, -50), "ann hair fg smug")

image ann smug:
    "ann smug composite"
    subpixel True
    xzoom -1.0
    yalign -0.1
    block:
        choice:
            easein 0.4 xzoom -1.0
            time 1.0
        choice:
            easein 0.4 xzoom 1.0
            time 1.0
        choice:
            ease 0.3 ypos 0.0
            ease 0.3 ypos -0.1
        repeat

image ann ultra smug composite = LiveComposite(
    (1920, 1080),
    (420, -130), "ann hair bg smug",
    (521, 799), "ann arm left",
    (990, 800), "ann arm right",
    (640, 550), "ann torso",
    (540, 0), "ann head smug",
    (600, 50), "ann face smug",
    (470, -50), "ann hair fg smug")

image ann ultra smug:
    "ann ultra smug composite"
    subpixel True
    xzoom -1.0
    yalign -0.1
    block:
        choice:
            easein 0.4 xzoom -1.0
            time 1.0
        choice:
            easein 0.4 xzoom 1.0
            time 1.0
        choice:
            ease 0.3 ypos 0.0
            ease 0.3 ypos -0.1
        repeat

image ann genki composite = LiveComposite(
    (1920, 1080),
    (640, 20), "ann hair bg",
    (521, 799), "ann arm left",
    (990, 800), "ann arm right",
    (640, 550), "ann torso",
    (745, 100), "ann head",
    (780, 230), "ann face genki",
    (800, 175), "ann eyebrow left",
    (1050, 200), "ann eyebrow right",
    (677, 69), "ann hair fg")

image ann genki:
    "ann genki composite"
    subpixel True
    xzoom -1.0
    yalign 0.25
    block:
        parallel:
            choice:
                ease 0.1 ypos -80
                ease 0.1 ypos 80
            choice:
                ease 0.1 ypos 80
                ease 0.1 ypos -80
            repeat
        parallel:
            ease 1.0 rotate 15.0
            ease 1.0 rotate -15.0
            repeat

image ann toast composite = LiveComposite(
    (1920, 1080),
    (640, 20), "ann hair bg",
    (521, 799), "ann arm left",
    (990, 800), "ann arm right",
    (640, 550), "ann torso",
    (745, 100), "ann head",
    (780, 230), "ann face toast",
    (800, 175), "ann eyebrow left",
    (1050, 200), "ann eyebrow right",
    (677, 69), "ann hair fg")

image ann toast:
    "ann toast composite"
    subpixel True
    xzoom -1.0
    yalign 0.25
    block:
        parallel:
            ease 0.25 ypos -80
            ease 0.25 ypos 80
            repeat
        parallel:
            ease 1.0 rotate 15.0
            ease 1.0 rotate -15.0
            repeat


image ann embarrassed composite = LiveComposite(
    (1920, 1080),
    (640, 20), "ann hair bg",
    (521, 799), "ann arm left",
    (990, 800), "ann arm right",
    (640, 550), "ann torso",
    (745, 100), "ann head embarrassed",
    (780, 230), "ann face disgust",
    (800, 175), "ann eyebrow left",
    (1050, 200), "ann eyebrow right",
    (677, 69), "ann hair fg")

image ann embarrassed:
    "ann embarrassed composite"
    subpixel True
    yalign 0.25
    block:
        parallel:
            linear 0.15 yzoom 1.0  
            linear 0.15 yzoom 0.75
        parallel:
            linear 0.15 xzoom 1.0  
            linear 0.15 xzoom 0.75
        repeat

image ann disgust composite = LiveComposite(
    (1920, 1080),
    (640, 20), "ann hair bg",
    (521, 799), "ann arm left",
    (990, 800), "ann arm right",
    (640, 550), "ann torso",
    (745, 100), "ann head",
    (780, 230), "ann face disgust",
    (800, 175), "ann eyebrow left",
    (1050, 200), "ann eyebrow right",
    (677, 69), "ann hair fg")

image ann disgust:
    "ann disgust composite"
    subpixel True
    yalign 0.25
    block:
        linear 0.01 xpos 920
        linear 0.01 xpos 929
        repeat

image ann rei ya normal:
    "characters/rei ya/rei ya normal.webp"
    xzoom -1.0
    yalign -0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#   ___       _             
#  / _ \ _ __(_) ___  _ __  
# | | | | '__| |/ _ \| '_ \ 
# | |_| | |  | | (_) | | | |
#  \___/|_|  |_|\___/|_| |_|
# Artist: Maxwell Paul Brickner
# Based on the traditional ANO mascot

image orion = "orion normal"


image orion normal:
    "characters/orion/orion normal.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 10.0 rotate -1.0
        repeat

image orion happy:
    "characters/orion/orion happy.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 3.0 rotate 1.0
        easeout 3.0 rotate -1.0
        repeat

image orion sad:
    "characters/orion/orion sad.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 3.0 rotate 1.0
        easeout 3.0 rotate -1.0
        repeat

image orion smug:
    "characters/orion/orion smug.webp"
    subpixel True
    block:
        choice:
            easein 0.8 xzoom -1.0
            time 1.0
        choice:
            easein 0.8 xzoom 1.0
            time 1.0
        repeat

image orion derp:
    "characters/orion/orion derp.webp"
    subpixel True
    block:
        parallel:
            linear 0.1 ypos 50
            linear 0.1 ypos -50
            repeat
        parallel:
            linear 1.0 rotate 15.0
            linear 1.0 rotate -15.0
            repeat

#  _____                  ____                      _ 
# |  ___| __ ___   __ _  / ___|  ___ _ __  ___  ___(_)
# | |_ | '__/ _ \ / _` | \___ \ / _ \ '_ \/ __|/ _ \ |
# |  _|| | | (_) | (_| |  ___) |  __/ | | \__ \  __/ |
# |_|  |_|  \___/ \__, | |____/ \___|_| |_|___/\___|_|
#                 |___/                               
# Artist: Maxwell Paul Brickner
# Concept: Alex Kidd
# Artist: Maxwell Paul Brickner

image frog sensei = "frog sensei happy"


image frog sensei happy:
    im.FactorScale("characters/frog sensei/frog sensei happy.webp",0.75,0.75)
    subpixel True
    yalign -0.1
    block:
        parallel:
            linear 0.1 yalign 0.1
            linear 0.1 yalign 0.0
            repeat
        parallel:
            linear 1.0 rotate 30.0
            linear 1.0 rotate -30.0
            repeat


image frog sensei angry:
    im.FactorScale("characters/frog sensei/frog sensei angry.webp",0.75,0.75)
    subpixel True
    yalign -0.1
    block:
        parallel:
            choice:
                linear 0.025 xalign 0.51
                linear 0.025 xalign 0.5
            choice:
                linear 0.025 xalign 0.49
                linear 0.025 xalign 0.5
        parallel:
            choice:
                linear 0.01 yalign 0.1
                linear 0.01 yalign 0.0
            choice:
                linear 0.01 yalign -0.1
                linear 0.01 yalign 0.0
        repeat

image frog sensei kidnap:
    im.FactorScale("characters/frog sensei/frog sensei kidnap.webp",0.75,0.75)
    subpixel True
    yalign -0.1
    block:
        parallel:
            linear 0.1 yalign 0.1
            linear 0.1 yalign 0.0
            repeat
        parallel:
            linear 1.0 rotate 30.0
            linear 1.0 rotate -30.0
            repeat

#     _       _            _              __        __     
#    / \   __| | ___  _ __(_)_ __   __ _  \ \      / /   _ 
#   / _ \ / _` |/ _ \| '__| | '_ \ / _` |  \ \ /\ / / | | |
#  / ___ \ (_| | (_) | |  | | | | | (_| |   \ V  V /| |_| |
# /_/   \_\__,_|\___/|_|  |_|_| |_|\__,_|    \_/\_/  \__,_|
# Artist: Maxwell Paul Brickner
# The wicked smart treasurer.

image adorina = "adorina normal"

# Body Parts

image adorina body normal:
    "characters/adorina/adorina body normal.webp"

image adorina body maid:
    "characters/adorina/adorina body maid normal.webp"

# Heads

image adorina head normal:
    "characters/adorina/adorina head normal.webp"

image adorina head normal smug:
    "characters/adorina/adorina head normal smug.webp"

image adorina head maid normal:
    "characters/adorina/adorina head maid normal.webp"

image adorina head maid smug:
    "characters/adorina/adorina head maid smug.webp"

# Composites

image adorina normal composite = LiveComposite(
    (1920, 1080),
    (620, 20), "adorina head normal",
    (600, 700), "adorina body normal")

image adorina smug composite = LiveComposite(
    (1920, 1080),
    (620, 20), "adorina head normal smug",
    (600, 700), "adorina body normal")

image adorina maid normal composite = LiveComposite(
    (1920, 1080),
    (640, -100), "adorina head maid normal",
    (625, 805), "adorina body maid")

image adorina maid smug composite = LiveComposite(
    (1920, 1080),
    (640, -100), "adorina head maid smug",
    (625, 805), "adorina body maid")

image adorina normal:
    "adorina normal composite"
    yalign 0.5
    subpixel True
    block:
        ease 7 rotate 5.0
        ease 14 rotate -10.0
        ease 7 rotate 5.0
        repeat

image adorina genki:
    "adorina normal composite"
    yalign 0.25
    subpixel True
    block:
        parallel:
            linear 0.08 ypos 80
            linear 0.08 ypos -80
            repeat
        parallel:
            linear 1.0 rotate 45.0
            linear 1.0 rotate -45.0
            repeat

image adorina smug:
    "adorina smug composite"
    yalign 0.25
    subpixel True
    parallel:
        linear 2 rotate 5.0
        linear 4 rotate -10.0
        linear 2 rotate 5.0
        repeat
    parallel:
        ease 0.1 ypos 20
        ease 0.1 ypos -20
        choice:
            time 1.0
        choice:
            time 4.20
        repeat

image adorina maid:
    "adorina maid normal composite"
    yalign 0.5
    subpixel True
    block:
        ease 7 rotate 5.0
        ease 14 rotate -10.0
        ease 7 rotate 5.0
        repeat

image adorina maid smug:
    "adorina maid smug composite"
    yalign 0.25
    subpixel True
    parallel:
        ease 2 rotate 5.0
        ease 4 rotate -10.0
        ease 2 rotate 5.0
        repeat
    parallel:
        ease 0.1 ypos 20
        ease 0.1 ypos -20
        choice:
            time 1.0
        choice:
            time 4.20
        repeat

image adorina maid genki:
    "adorina maid normal composite"
    yalign 0.25
    subpixel True
    block:
        parallel:
            linear 0.08 ypos 80
            linear 0.08 ypos -80
            repeat
        parallel:
            linear 1.0 rotate 45.0
            linear 1.0 rotate -45.0
            repeat

# __        ___ _     _  __        __                     _             
# \ \      / (_) | __| | \ \      / /   _  ___  _ __ ___ (_)_ __   __ _  __        ___ _ _ 
#  \ \ /\ / /| | |/ _` |  \ \ /\ / / | | |/ _ \| '_ ` _ \| | '_ \ / _` | \ \      / (_) | |
#   \ V  V / | | | (_| |   \ V  V /| |_| | (_) | | | | | | | | | | (_| |  \ \ /\ / /| | | |
#    \_/\_/  |_|_|\__,_|    \_/\_/  \__, |\___/|_| |_| |_|_|_| |_|\__, |   \ V  V / | | | |
#                                   |___/                         |___/     \_/\_/  |_|_|_|
# Artist: Maxwell Paul Brickner

image will = "will normal"


image will normal:
    "characters/will/will.webp"
    yalign 0.4
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  __  __               _                 _       
# |  \/  | ___ _ __ ___| |__   __ _ _ __ | |_ ___ 
# | |\/| |/ _ \ '__/ __| '_ \ / _` | '_ \| __/ __|
# | |  | |  __/ | | (__| | | | (_| | | | | |_\__ \
# |_|  |_|\___|_|  \___|_| |_|\__,_|_| |_|\__|___/

#  __  __            _               ___  _     _ _            
# |  \/  | __ ___  _(_)_ __   ___   / _ \| |__ | (_) __ _  ___ 
# | |\/| |/ _` \ \/ / | '_ \ / _ \ | | | | '_ \| | |/ _` |/ _ \
# | |  | | (_| |>  <| | | | |  __/ | |_| | |_) | | | (_| |  __/
# |_|  |_|\__,_/_/\_\_|_| |_|\___|  \___/|_.__/|_|_|\__, |\___|
#                                                   |___/
# Artist: Maxwell Paul Brickner
# Nouveau riche.

image moe oblige = "moe normal"


image moe oblige normal:
    "characters/moe/moe.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  _  __                      _  __           _ 
# | |/ /__ _ _ __ ___ _ __   | |/ /___  _ __ (_)
# | ' // _` | '__/ _ \ '_ \  | ' // _ \| '_ \| |
# | . \ (_| | | |  __/ | | | | . \ (_) | |_) | |
# |_|\_\__,_|_|  \___|_| |_| |_|\_\___/| .__/|_|
#                                      |_|      
# Artist: Maxwell Paul Brickner
# I REALLY miss Malaysian food, even the overly sweet coffee.

image karen kopi = "karen kopi happy"


image karen kopi happy:
    "characters/karen kopi/karen kopi happy.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image karen kopi pour:
    "characters/karen kopi/karen kopi pour.webp"
    yalign 0.2
    subpixel True
    block:
        easeout 2.5 rotate 1.0
        easeout 5.0 rotate -2.0
        easeout 2.5 rotate 1.0
        repeat

#  ____       _ _ _       _   ____  _             _              _ 
# | __ )  ___| | (_)_ __ (_) |  _ \(_) __ _  __ _| |_ ___  _ __ (_)
# |  _ \ / _ \ | | | '_ \| | | |_) | |/ _` |/ _` | __/ _ \| '_ \| |
# | |_) |  __/ | | | | | | | |  _ <| | (_| | (_| | || (_) | | | | |
# |____/ \___|_|_|_|_| |_|_| |_| \_\_|\__, |\__,_|\__\___/|_| |_|_|
#                                     |___/                        
# Artist: Maxwell Paul Brickner

image bellini rigatoni = "bellini rigatoni happy"

image bellini rigatoni body:
    "characters/bellini rigatoni/bellini rigatoni.webp"

image bellini rigatoni smile:
    "characters/bellini rigatoni/bellini rigatoni mouth.webp"

image bellini rigatoni frown:
    "characters/bellini rigatoni/bellini rigatoni mouth.webp"
    yzoom -1.0
    subpixel True

image bellini rigatoni happy composite = LiveComposite(
    (1920, 1080),
    (600, 20), "bellini rigatoni body",
    (930, 420), "bellini rigatoni smile")

image bellini rigatoni happy:
    "bellini rigatoni happy composite"
    subpixel True
    yalign 0.5
    block:
        easeout 2.5 rotate 1.0
        easeout 5.0 rotate -2.0
        easeout 2.5 rotate 1.0
        repeat

image bellini rigatoni sad composite= LiveComposite(
    (1920, 1080),
    (600, 20), "bellini rigatoni body",
    (930, 420), "bellini rigatoni frown")

image bellini rigatoni sad:
    "bellini rigatoni sad composite"
    subpixel True
    yalign 0.25
    block:
        linear 0.01 xpos 920
        linear 0.01 xpos 929
        repeat

#  ____  _           _____         _     _ 
# / ___|| | ____ _  | ____|___ ___| |__ (_)
# \___ \| |/ / _` | |  _| / __/ __| '_ \| |
#  ___) |   < (_| | | |__| (_| (__| | | | |
# |____/|_|\_\__,_| |_____\___\___|_| |_|_|
# Artist: Maxwell Paul Brickner
# Based on a joke that I believe was suggested by Kirsten McLaughlin to have a sketchy character.
# The pun is all mine.

image ska ecchi:
    "characters/ska/ska ecchi.webp"
    subpixel True

#  ____            _     _       _               _           _            
# |  _ \ __ _  ___| |__ (_)_ __ | | _____       | | ___  ___| |_ ___ _ __ 
# | |_) / _` |/ __| '_ \| | '_ \| |/ / _ \   _  | |/ _ \/ __| __/ _ \ '__|
# |  __/ (_| | (__| | | | | | | |   < (_) | | |_| |  __/\__ \ ||  __/ |   
# |_|   \__,_|\___|_| |_|_|_| |_|_|\_\___/   \___/ \___||___/\__\___|_|   
# Artist: Maxwell Paul Brickner
# An addict who has completely given in.

image pachinko jester:
    "characters/pachinko jester/pachinko jester.webp"
    yalign 0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  ____  _____ _________  _____ _____
# / ___|| ____|__  / ___|| ____|__  /
# \___ \|  _|   / /\___ \|  _|   / / 
#  ___) | |___ / /_ ___) | |___ / /_ 
# |____/|_____/____|____/|_____/____|
# Thank you for the candy.

image sezsez liberty:
    "characters/sezsez/sezsez liberty.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image sezsez amadeus:
    "characters/sezsez/sezsez amadeus.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  ____                  _ _     _       
# |  _ \ __ _ _ __   ___| (_)___| |_ ___ 
# | |_) / _` | '_ \ / _ \ | / __| __/ __|
# |  __/ (_| | | | |  __/ | \__ \ |_\__ \
# |_|   \__,_|_| |_|\___|_|_|___/\__|___/

#   ____           ____  __  __ 
#  / ___| ___  ___|  _ \|  \/  |
# | |  _ / _ \/ _ \ |_) | |\/| |
# | |_| |  __/  __/  __/| |  | |
#  \____|\___|\___|_|   |_|  |_|
# Artist: Maxwell Paul Brickner
# Based on GPM with permission. buff boi

image gpm = "gpm normal"

image gpm normal:
    "characters/geepm/geepm.webp"
    yalign 0.5
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  ____      _  __   __    
# |  _ \ ___(_) \ \ / /_ _ 
# | |_) / _ \ |  \ V / _` |
# |  _ <  __/ |   | | (_| |
# |_| \_\___|_|   |_|\__,_|
# Artist: Maxwell Paul Brickner

image rei ya normal:
    "characters/rei ya/rei ya normal.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image rei ya silver:
    "characters/rei ya/rei ya silver.webp"

image rei ya ann smug:
    "ann smug"
    subpixel True
    xzoom -1.0
    yalign -0.1

image rei ya ann ultra smug:
    "ann ultra smug"
    subpixel True
    xzoom -1.0
    yalign -0.1

#  _  __          _   _        ____                 _               
# | |/ /__ _ _ __| |_| |__    / ___|_ __ __ _ _ __ | |__   ___ _ __ 
# | ' // _` | '__| __| '_ \  | |  _| '__/ _` | '_ \| '_ \ / _ \ '__|
# | . \ (_| | |  | |_| | | | | |_| | | | (_| | |_) | | | |  __/ |   
# |_|\_\__,_|_|   \__|_| |_|  \____|_|  \__,_| .__/|_| |_|\___|_|   
#                                            |_|                    
# Artist: Maxwell Paul Brickner
# Loves to survey pubs.

image karth grapher:
    "characters/karth grapher/karth grapher.webp"
    yalign 0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  _  __             
# | |/ /__ _ _______ 
# | ' // _` |_  / _ \
# | . \ (_| |/ /  __/
# |_|\_\__,_/___\___|
# Artist: Maxwell Paul Brickner

image kaze:
    "characters/kaze/kaze.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#   ____          _         __  __       _                 
#  / ___|___   __| |_   _  |  \/  | __ _(_)___  ___  _ __  
# | |   / _ \ / _` | | | | | |\/| |/ _` | / __|/ _ \| '_ \ 
# | |__| (_) | (_| | |_| | | |  | | (_| | \__ \ (_) | | | |
#  \____\___/ \__,_|\__, | |_|  |_|\__,_|_|___/\___/|_| |_|
#                   |___/                                  
# Artist: Maxwell Paul Brickner

image cody maison = "cody maison happy"

# Body Parts

image cody maison body:
    "characters/cody maison/cody maison.webp"

image cody maison smile:
    "characters/cody maison/cody maison smile.webp"

image cody maison frown:
    "characters/cody maison/cody maison smile.webp"
    yzoom -1.0
    subpixel True

# Compositions

image cody maison happy composition = LiveComposite(
    (1920, 1080),
    (100, 0), "cody maison body",
    (900, 280), "cody maison smile")

image cody maison sad composition = LiveComposite(
    (1920, 1080),
    (100, 0), "cody maison body",
    (900, 280), "cody maison frown")

image cody maison angry composition = LiveComposite(
    (1920, 1080),
    (960, 0), "cody maison body",
    (1765, 280), "cody maison frown")

image cody maison happy:
    "cody maison happy composition"

image cody maison sad:
    "cody maison sad composition"

image cody maison angry:
    "cody maison angry composition"
    subpixel True
    block:
        ease 0.1 xpos 69
        ease 0.1 xpos -69
        repeat

#  ____  _                 _ 
# |  _ \(_) __ _ _ __  ___(_)
# | |_) | |/ _` | '_ \|_  / |
# |  __/| | (_| | | | |/ /| |
# |_|   |_|\__,_|_| |_/___|_|
# Artist: Maxwell Paul Brickner

image pianzi:
    "characters/pianzi/pianzi.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  ____             _____     
# |  _ \ __ _ ____ |_   _|_ _ 
# | |_) / _` |_  /   | |/ _` |
# |  __/ (_| |/ /    | | (_| |
# |_|   \__,_/___|   |_|\__,_|        
# Artist: Maxwell Paul Brickner

image paz ta:
    "characters/paz ta/paz ta.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  ____              ____             _   
# |  _ \ ___   ___  | __ ) _   _ _ __| |_ 
# | |_) / _ \ / _ \ |  _ \| | | | '__| __|
# |  _ < (_) |  __/ | |_) | |_| | |  | |_ 
# |_| \_\___/ \___| |____/ \__,_|_|   \__|
# Artist: Maxwell Paul Brickner

image roe burt:
    "characters/roe burt/roe burt.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image roe burt point:
    "characters/roe burt/roe burt point.webp"
    yalign -0.1
    subpixel True
    block:
        parallel:
            linear 0.1 yzoom 1.0  
            linear 0.1 yzoom 0.75
        parallel:
            linear 0.1 xzoom 1.0  
            linear 0.1 xzoom 0.75
        repeat

#  ___ ____ _____ 
# |_ _/ ___|_   _|
#  | |\___ \ | |  
#  | | ___) || |  
# |___|____/ |_|  
# Artist: Maxwell Paul Brickner

image ist normal:
    "characters/ist/ist.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image ist shotgun:
    "characters/ist/ist s.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image ist tape:
    "characters/ist/ist tape.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

#  __  __       _           _          _                   ____  _ 
# |  \/  | ___ | |__   ___ | |__  _ __(_) ___  _   _ ___  |  _ \(_)
# | |\/| |/ _ \| '_ \ / _ \| '_ \| '__| |/ _ \| | | / __| | |_) | |
# | |  | | (_) | |_) | (_) | |_) | |  | | (_) | |_| \__ \ |  __/| |
# |_|  |_|\___/|_.__/ \___/|_.__/|_|  |_|\___/ \__,_|___/ |_|   |_|
# Artist: Maxwell Paul Brickner
# Da+da-da*da/da! Let's have one for Mobobrious π!

# Deviant Nudist Snake & Bodyguards
image dns:
    "characters/mobobrious/dns.webp"
    yalign 1.0
    subpixel True

#   ____                 _       
#  / ___|_   _  ___  ___| |_ ___ 
# | |  _| | | |/ _ \/ __| __/ __|
# | |_| | |_| |  __/\__ \ |_\__ \
#  \____|\__,_|\___||___/\__|___/
# Artist: Maxwell Paul Brickner

image guest fairy:
    "characters/guests/guest fairy.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image guest cyber:
    "characters/guests/guest cyber.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image guest gamer:
    "characters/guests/guest gamer.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image guest funky:
    "characters/guests/guest funky.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image guest furry:
    "characters/guests/guest furry.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image guest otaku:
    "characters/guests/guest otaku.webp"
    yalign 0.2
    subpixel True

image guest traffic head:
    im.FactorScale("characters/guests/guest traffic head.webp",0.75,0.75)
    yalign 0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image guest welchertaku:
    "characters/guests/guest welchertaku.webp"
    yalign 0.45
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

# Cosplay cop was gonna play a larger role, but eh?
image guest cosplay cop:
    "characters/cosplay cop/cosplay cop.webp"
    yalign 0.25
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat

image raised hand:
    "characters/guests/raised hand.webp"
    yalign -0.1
    subpixel True
    block:
        easeout 10.0 rotate 10.0
        easeout 20.0 rotate -20.0
        easeout 10.0 rotate 10.0
        repeat

#  ____  _        _      _              
# / ___|| | _____| | ___| |_ ___  _ __  
# \___ \| |/ / _ \ |/ _ \ __/ _ \| '_ \ 
#  ___) |   <  __/ |  __/ || (_) | | | |
# |____/|_|\_\___|_|\___|\__\___/|_| |_|
# Artist: Kirsten McLaughlin
# Based on ANO's custom tabletop role playing game.

image skeleton:
    "kirsten_art/skeleton top.webp"
    yalign 0.1
    subpixel True
    block:
        easeout 10.0 rotate 1.0
        easeout 20.0 rotate -2.0
        easeout 10.0 rotate 1.0
        repeat
