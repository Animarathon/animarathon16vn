# Animarathon XVI: Operation Ohio GIS Panel
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
#   ____ ___ ____    ____                  _ 
#  / ___|_ _/ ___|  |  _ \ __ _ _ __   ___| |
# | |  _ | |\___ \  | |_) / _` | '_ \ / _ \ |
# | |_| || | ___) | |  __/ (_| | | | |  __/ |
#  \____|___|____/  |_|   \__,_|_| |_|\___|_|
#  ____                  _   ____  _
# |  _ \ __ _ _ __   ___| | |  _ \| | __ _ _ __  
# | |_) / _` | '_ \ / _ \ | | |_) | |/ _` | '_ \ 
# |  __/ (_| | | | |  __/ | |  __/| | (_| | | | |
# |_|   \__,_|_| |_|\___|_| |_|   |_|\__,_|_| |_|
#
# By the end of the panel the player should experience the following outcomes.
#
# ! Positive Outcome (Player doesn't nap.)
# 💭 Be exposed to OSM, a open map anyone can edit.
# 💭 Learn how to use the editor iD to improve OSM.
# 💭 Be exposed to how editing OSM benefits their daily life.
# 💭 Learn an application of space technology. (Satellite imagery)
# $ Gain a in game reward for learning.
# Ψ Feel that this learning was done of their own free will.
#
# ! Negative Outcomes (The player took a nap.)
# 💭 Experience some minor wordplay.
# $ Gain a in game reward to encourage better sleeping habits.
# Ψ Feel that this choice was made of their own free will. 

label gis:

    scene panel room large
    with dissolve

    play music this_reminds_me_of_something_p0 fadeout 1

    show crowd
    with easeinbottom

    jump gis_menu

label gis_menu:

    menu:

        ann_thoughts "Looks like the [favorite_anime] panel is about to start. What should I do?"

        "Stay awake for the panel":

            call gis_awake

        "Consider the Panel":

            call gis_considerations

            jump gis_menu

        "Take a nap outside the panel":

            call gis_asleep

    stop music fadeout 1

    return

label gis_awake:

    show karth grapher
    with easeinright

    kg "Good day! Welcome to the [favorite_anime] panel!"

    hide karth grapher
    with easeoutright

    show guest otaku
    with easeinright

    if favorite_anime != "Welchert in the Crib: Z":

        guest_otaku "My omae! I love [favorite_anime]!"

    if favorite_anime == "Welchert in the Crib: Z":

        guest_otaku "Whatever! The only reason I'm here is to make fun of [favorite_anime]!"

    hide guest
    with easeoutright

    queue music this_reminds_me_of_something_p1

    show karth grapher
    with easeinright

    kg "That's what I would say, but the prefecture where [favorite_anime] is produced was hit by an earthquake!"

    hide karth grapher
    with easeoutright

    show guest otaku
    with easeinright

    if favorite_anime != "Welchert in the Crib: Z":

        guest_otaku "They had to delay the next season of [favorite_anime] indefinitely because of this!"

        hide guest
        with easeoutright

    if favorite_anime == "Welchert in the Crib: Z":

        guest_otaku "Good! I hope the studio that made [favorite_anime] falls into the earth!"

        hide guest
        with easeoutright

        ann_thoughts "Wow! The hatred in his voice really says he means it."

        show karth grapher
        with easeinright

        kg "Even if you don't like [favorite_anime] that's a little bit harsh, don't you think?"

        hide karth grapher
        with easeoutright

        show guest otaku
        with easeinright

        guest_otaku "Not at all! Everyone in that prefecture deserves to die. There is no excuse for bad anime!"

        hide guest
        with easeoutright

        ann_thoughts "What a jerk! People's lives are more important then anime."

        ann_thoughts "Even if he doesn't care about human lives, acclaimed masterpieces like {b}Zee Bick Paris Etni Trecew{/b} came out of that prefecture."

        ann_thoughts "It's wrong both morally and practically to wish death to a whole geographic region over an single anime being bad."

    show karth grapher
    with easeinright

    kg "We can help the people in that prefecture! Aid workers need maps, and we can help provide those!"

    hide karth grapher
    with easeoutright

    show guest funky
    with easeinright

    guest_funky "How can we provide maps of Japan if we're in Bowling Green? My vision is as groovy as a topographic map, but even I can't see that far!"

    hide guest
    with easeoutright

    show karth grapher
    with easeinright

    kg "By tracing new satellite imagery of the city from after the earthquake into usable maps, we can help first responders!"

    hide karth grapher
    with easeoutright

    if favorite_anime != "Welchert in the Crib: Z":

        menu:

            ann_thoughts "What would the heroes of [favorite_anime] do?"

            "They'd help out!":

                ann_thoughts "I think they'd help out!"

            "They'd leave and do something else!":

                ann_thoughts "Screw this switcheroo! I'm outta here!"

                return

    if favorite_anime == "Welchert in the Crib: Z":

        menu:

            ann_thoughts "What would Welchert do?"

            "He'd help fix his crib!":

                ann_thoughts "Welchert would help!"

            "He'd chill with Zebulon the Third instead!":

                ann_thoughts "This isn't my speed. I'll just donate some money to a charity later..."

                return

    # Players don't like being tricked. This is to give angry players an out.
    # Often when people are dragged to a mapapthon they don't actually want to attend, they contribute low quality data. Never force it.

    hide crowd
    with easeoutbottom

    show karth grapher
    with easeinright

    kg "I'm glad that some of you stayed behind! I have some laptops ready to go, so please take one and fire up the web browser!"

    hide karth grapher
    with easeoutright

    ann_thoughts "Looks like I'll have to make an account on this website... done! [online_handle] is online!"

    show karth grapher
    with easeinright

    kg "It looks like everyone is done! Great! Click on the edit button now! This will bring you into the default editor."

    hide karth grapher
    with easeoutright

    # __        __            __  __                   _
    # \ \      / /_ _ _   _  |  \/  | __ _ _ __  _ __ (_)_ __   __ _ 
    #  \ \ /\ / / _` | | | | | |\/| |/ _` | '_ \| '_ \| | '_ \ / _` |
    #   \ V  V / (_| | |_| | | |  | | (_| | |_) | |_) | | | | | (_| |
    #    \_/\_/ \__,_|\__, | |_|  |_|\__,_| .__/| .__/|_|_| |_|\__, |
    #                 |___/               |_|   |_|            |___/ 

    queue music this_reminds_me_of_something_p2

    show osm 1
    show openstreetmap copyright

    kg "You should see the satellite imagery on screen now. As a test please use it to mark that footpath!"

    show osm 2
    with dissolve

    ann_thoughts "So I need to click on this button that says {b}Line{/b}."

    show osm 3
    with dissolve

    ann_thoughts "Then I should click where the footpath is missing."

    show osm 4
    with dissolve

    ann_thoughts "I should probably click on this intersection, so the map recognizes it. If this were an overpass I shouldn't click here."

    show osm 5
    with dissolve

    ann_thoughts "I should complete the sidewalk by clicking on the end!"

    show osm 6
    with dissolve

    ann_thoughts "The path is done, but it doesn't quite match up. If I type in foot path maybe..."

    show osm 8
    with dissolve

    ann_thoughts "Yeah! It popped up! Now I just need to save my work..."

    show osm 9
    with dissolve

    a "All done!"

    kg "Great! Now it's time to do this for real! Some surveys indicated there was an unmapped hospital in your next tab."

    #     _                     __  __                   _
    #    / \   _ __ ___  __ _  |  \/  | __ _ _ __  _ __ (_)_ __   __ _ 
    #   / _ \ | '__/ _ \/ _` | | |\/| |/ _` | '_ \| '_ \| | '_ \ / _` |
    #  / ___ \| | |  __/ (_| | | |  | | (_| | |_) | |_) | | | | | (_| |
    # /_/   \_\_|  \___|\__,_| |_|  |_|\__,_| .__/| .__/|_|_| |_|\__, |
    #                                       |_|   |_|            |___/ 

    queue music this_reminds_me_of_something_p3

    show osm 10
    with dissolve

    kg "I located it for you, so all you have to do is draw it."

    ann_thoughts "It looks like it's right here in the middle of the screen."

    show osm 11
    with dissolve

    ann_thoughts "I should use the area tool to draw it!"

    show osm 16
    with dissolve

    ann_thoughts "Then I should search for hospital..."

    show osm 17
    with dissolve

    ann_thoughts "Save and done!"

    kg "Great job everyone!"

    hide openstreetmap copyright
    hide osm 17

    #     _    ____     ____                              ___      ___  ____  __  __ 
    #    / \  |  _ \   / ___| __ _ _ __ ___   ___  ___   ( _ )    / _ \/ ___||  \/  |
    #   / _ \ | |_) | | |  _ / _` | '_ ` _ \ / _ \/ __|  / _ \/\ | | | \___ \| |\/| |
    #  / ___ \|  _ <  | |_| | (_| | | | | | |  __/\__ \ | (_>  < | |_| |___) | |  | |
    # /_/   \_\_| \_\  \____|\__,_|_| |_| |_|\___||___/  \___/\/  \___/|____/|_|  |_|

    queue music this_reminds_me_of_something_p4

    show karth grapher
    with easeinright

    kg "Our panel time is almost up, but we can have a short Q&A! Meet us after Animarathon at Pollyocchi's pub for more mapping and drinks!"

    hide karth grapher
    with easeoutright

    show guest gamer
    with easeinright

    guest_gamer "15n7 d15 d4 m4p AR v1dy4 g4m3z u53?"
    # Isn't this the map that Augmented Reality games use?

    hide guest
    with easeoutright

    show karth grapher
    with easeinright

    kg "That's right! Remember that as long as your edits are truthful, there's no shame in improving your local area on the map to improve your game!"

    hide karth grapher
    with easeoutright

    show guest gamer
    with easeinright

    guest_gamer "K 7HX!"
    # That is OK! Thank you!

    hide guest
    with easeoutright

    show karth grapher
    with easeinright

    kg "That's all the time we have for this panel! See you at the pub!"

    hide karth grapher
    with easeoutright

    return

#     _        _
#    / \   ___| | ___  ___ _ __  
#   / _ \ / __| |/ _ \/ _ \ '_ \ 
#  / ___ \\__ \ |  __/  __/ |_) |
# /_/   \_\___/_|\___|\___| .__/ 
#                         |_|
label gis_asleep:

    play music this_reminds_me_of_something_p4 fadeout 1

    show black
    with irisin

    a "Sleep is good. mmmm..."

    show orange
    with dissolve

    hide black
    with dissolve

    ann_thoughts "What's the point... Of [favorite_anime]..."

    show red
    with dissolve

    hide orange
    with dissolve

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "What's the point... Of life?"

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "The shortest path between the two points... is a line..."

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

label gis_considerations:

    menu:
    
        ann_thoughts "Was there anything I wanted to consider before the panel starts?"

        "Who is the panelist?":

            ann_thoughts "[kg] is a big fan of [favorite_anime]."

            ann_thoughts "Online he's noted for making high quality maps of fictional worlds."

            ann_thoughts "I wonder what he'll have to say?"

            # FIXME

        "What is [favorite_anime]?":

            ann_thoughts "[favorite_anime] is great! I love [favorite_anime]!"

        "That's all":

            return

    jump gis_considerations
