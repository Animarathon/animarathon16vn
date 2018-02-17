# Animarathon XVI: Operation Ohio Chinese Panel
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
#   ____ _     _                        ____                  _ 
#  / ___| |__ (_)_ __   ___  ___  ___  |  _ \ __ _ _ __   ___| |
# | |   | '_ \| | '_ \ / _ \/ __|/ _ \ | |_) / _` | '_ \ / _ \ |
# | |___| | | | | | | |  __/\__ \  __/ |  __/ (_| | | | |  __/ |
#  \____|_| |_|_|_| |_|\___||___/\___| |_|   \__,_|_| |_|\___|_|
#  ____                  _   ____  _
# |  _ \ __ _ _ __   ___| | |  _ \| | __ _ _ __  
# | |_) / _` | '_ \ / _ \ | | |_) | |/ _` | '_ \ 
# |  __/ (_| | | | |  __/ | |  __/| | (_| | | | |
# |_|   \__,_|_| |_|\___|_| |_|   |_|\__,_|_| |_|
#
# By the end of the panel the player should experience the following outcomes.
#
# ! Positive Outcome (Player doesn't nap.)
# 💭 Be exposed to non-japanese cartoons.
# 💭 Be exposed to a non-roman writing system.
# 💭 Understand that China has a long history.
# 💭 Dispel stereotypes about Chinese martial arts.
# $ Gain a in game reward for learning.
# Ψ Feel that this learning was done of their own free will.
#
# ! Negative Outcomes (The player took a nap.)
# 💭 Experience some minor wordplay.
# $ Gain a in game reward to encourage better sleeping habits.
# Ψ Feel that this choice was made of their own free will. 

label chinese:

    scene bg panel room old
    with dissolve

    play music this_reminds_me_of_something_p0 fadeout 1

    show text "{size=70}Chapter 3: Chinese Creations!{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard='True')
    
    hide text
    with dissolve

    show crowd
    with easeinbottom

    jump chinese_menu

label chinese_menu:

    menu:

        ann_thoughts "Looks like the chinese cartoon panel is about to start. What should I do?"

        "Stay awake for the panel":

            call chinese_awake

        "Consider the Panel":

            call chinese_considerations

            jump chinese_menu

        "Take a nap outside the panel":

            call chinese_asleep

    stop music fadeout 1

    return

label chinese_awake:

    show pianzi
    with easeinright

    pz "{image=chinese 004}"
    # Hello! My name is conman!

    menu:

        ann_thoughts "My Mandarin isn't the best, but I believe he said he's a conman? How should I respond?"

        "{image=chinese 003} (Hello?)":

            pz "{image=chinese 006}"
            # Good! You speak Chinese!

            hide pianzi
            with easeoutright

            ann_thoughts "He said he was happy that I spoke Chinese I think."

            show guest gamer
            with easeinright

            guest_gamer "d00d 1 c4n7 und3r574nd j00!"
            # Dude I can not understand you. (Referring to his language)
            # I used the gamer guest because 1337 is probably only somewhat more intelligible for many players new to gaming then Chinese.

            hide guest
            with easeoutright

            ann_thoughts "I think that he's saying that he can't understand what's being said."

            show pianzi
            with easeinright

            pz "{image=chinese 009}?"
            # eh?

            hide pianzi
            with easeoutright

            ann_thoughts "He just said eh? What kind of response is that?"

            show guest funky
            with easeinright

            guest_funky "Mellow out your jive tongue brother! It ain't groovy! Dig it?"
            # Please make your language more understandable. Do you understand what I am saying?

            hide guest
            with easeoutright

            ann_thoughts "A jive tongue? What's that supposed to mean?"

        "{image=chinese 002} (What a fantastic title! It brings me joy!)":

            # Your name is conman? He He Ha Ha He He Ha Ha He He!

            show pianzi
            with easeinright

            pz "{image=chinese 008}?"
            # I like my name! My name is Conman!

            hide pianzi
            with easeoutright

            ann_thoughts "He says he really liked that! Nice!"
            # That's not what he said.

            show pianzi
            with easeinright

            pz "{image=chinese 007}! Sorry! Not all of you speak chinese! Not to purplehead though! She called me a conman!"
            # Sorry!

            hide pianzi
            with easeoutright

            show ann disgust
            with easeinleft

            a "{image=chinese 001} (You're named conman, and you are also a conman!)"

            hide ann
            with easeoutleft

            show pianzi
            with easeinright

            pz "{image=chinese 005}! I forgive you purple! I eat sorghum and gnaw on iron - you'll need more then that to get under my skin!"
            # Sorry!

            hide pianzi
            with easeoutright

    queue music this_reminds_me_of_something_p1

    show pianzi
    with easeinright

    pz "Welcome to the {i}Chinese Cartoon Panel{/i}! You've seen Anime, but did you know China also has cartoons?"

    hide pianzi
    with easeoutright

    show guest otaku
    with easeinright

    guest_otaku "Hontou ni?! Watashi think there was only Japanese, American, and Canadian cartoons ~uguu~?"

    hide guest
    with easeoutright

    queue music this_reminds_me_of_something_p2

    show pianzi
    with easeinright

    pz "A panel is most useful when it is empty, so I didn't write a script. What would you like to learn about Chinese Cartoons?"

    hide pianzi
    with easeoutright

    show ann smug
    with easeinleft

    a "Really? I don't think that phrase works quite like that."

    hide ann
    with easeoutleft

    show pianzi
    with easeinright

    if last_ordered != "Dumplings":

        pz "The best way to deal with a large topic is to split it up. You know some Mandarin purple, so why don't you pick?"

    if last_ordered == "Dumplings":

        pz "The best way to deal with a large topic is to split it up. You smell like dumplings purple, so why don't you pick?"

    hide pianzi
    with easeoutright

    queue music this_reminds_me_of_something_p4

    menu:

        ann_thoughts "What should I ask about Chinese Cartoons?"

        "History of Chinese Cartoons":

            show pianzi
            with easeinright

            pz "The roots of Chinese Cartoons lie in 1000 year old shadow puppetry. The technique is similar to cel animation."

            hide pianzi
            with easeoutright

            show guest cyber
            with easeinright

            guest_cyber "Cel Animation and kino is so 1980's though. Digital CGI is where it's at now."

            hide guest
            with easeoutright

            show pianzi
            with easeinright

            pz "... A recurring story in Chinese cartoons is 1500's classic {i}Journey to the West{/i}. Some of it's heroes like Sun Wukong have become well known."

            hide pianzi
            with easeoutright

            show guest furry
            with easeinright

            guest_furry "One of my friends is a Monkey King too! You should see his extending staff!"

            hide guest
            with easeoutright

            show pianzi
            with easeinright

            pz "... You can take his staff and spin on it. Forget this panel, I'm grabbing dumplings."

            hide pianzi
            with easeoutright

        "Gong Fu":

            show pianzi
            with easeinright

            pz "May Chinese cartoons have Gung Fu!"

            hide pianzi
            with easeoutright

            show guest cyber
            with easeinright

            guest_cyber "I know about Gong Fu! You see it in Kung Fu movies!"

            hide guest
            with easeoutright

            show pianzi
            with easeinright

            pz "Gong Fu encompasses many skills, from fighting to Tea Preparation!"

            hide pianzi
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "5h0w u5 y0ur m0v3s!"
            # Show us your moves!

            hide guest
            with easeoutright

            show pianzi
            with easeinright

            pz "Excuse me? I don't actually know Gong Fu."

            hide pianzi
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "C0m3 0n! 5h0w u5 y0ur m0v3s!"
            # Come on! Show us your moves!

            hide guest
            with easeoutright

            show pianzi
            with easeinright

            pz "Forget this panel. You guys are bad qi!"

            hide pianzi
            with easeoutright

        # "Locations in Chinese Cartoons":
        #
        #    show pianzi
        #    with easeinright
        # 
        #    pz "Let's start from the top. Harbin is a northern city in China with beautiful snow."
        #
        #    hide pianzi
        #    with easeoutright
        #

    return

#     _        _
#    / \   ___| | ___  ___ _ __  
#   / _ \ / __| |/ _ \/ _ \ '_ \ 
#  / ___ \\__ \ |  __/  __/ |_) |
# /_/   \_\___/_|\___|\___| .__/ 
#                         |_|
label chinese_asleep:

    play music this_reminds_me_of_something_p4 fadeout 1

    show black
    with irisin

    a "Sleep is good. mmmm..."

    show orange
    with dissolve

    hide black
    with dissolve

    ann_thoughts "Hey auntie... Where's my ang-pao..."

    show red
    with dissolve

    hide orange
    with dissolve

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "Last year... Year of the rooster... How did it get orange... Orange chicken... Stop..."

    $ energy += 10

    hide crowd

    hide red
    with irisout

    ann_thoughts "Oh my. Looks like everyone's gone now."

    return

#   ____                _     _                _   _                 
#  / ___|___  _ __  ___(_) __| | ___ _ __ __ _| |_(_) ___  _ __  ___ 
# | |   / _ \| '_ \/ __| |/ _` |/ _ \ '__/ _` | __| |/ _ \| '_ \/ __|
# | |__| (_) | | | \__ \ | (_| |  __/ | | (_| | |_| | (_) | | | \__ \
#  \____\___/|_| |_|___/_|\__,_|\___|_|  \__,_|\__|_|\___/|_| |_|___/

label chinese_considerations:

    menu:
    
        ann_thoughts "Was there anything I wanted to consider before the panel starts?"

        "Who is the panelist?":

            ann_thoughts "[pz] is considered an expert in the field of Chinese Cartoons."

            ann_thoughts "Some call his opinions fraudulent though."

            ann_thoughts "I wonder what he'll have to say?"

        "What is a Chinese cartoon?":

            ann_thoughts "A Chinese cartoon is a cartoon made in China."

        "That's all":

            return

    jump chinese_considerations
