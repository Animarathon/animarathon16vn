# Animarathon XVI: Operation Ohio Kawaii Kafe Date: Orion
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

label kawaii_kafe_date_orion:

    show ann disgust
    with easeinleft

    a "It paired us? Man, Animarathon really is a rip off!"

    hide ann
    with easeoutleft

    $ hunger -= 20

    show orion normal
    with easeinright

    o "You're telling me!"

    hide orion
    with easeoutright

    show ann normal
    with easeinleft

    a "..."

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "..."

    hide orion
    with easeoutright

    menu:

        ann_thoughts "This is awkward. Should I break the silence?"

        "Ask [o] about last night.":

            call orion_story

        "Start an argument.":

            call orion_argument

        "Stay Quiet.":

            show ann normal
            with easeinleft

            a "..."

            hide ann
            with easeoutleft

            show orion normal
            with easeinright

            o "..."

            hide orion
            with easeoutright

    show ann normal
    with easeinleft

    a "We should get going."

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "Yeah! Let's go!"

    hide orion
    with easeoutright

    return

label orion_story:

    show ann normal
    with easeinleft

    a "It was Wal-Beer-Gis night last night at TSUN right? Got any stories?"

    hide ann
    with easeoutleft

    # More based on Kent's spring parties then anything at TSUN.

    show orion normal
    with easeinright

    o "Do I! It almost immediately got out of control! The riot police were already waiting."

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "That's a given. I bet the crowd reacted responsibly."

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "The crowd started shouting USA USA USA! They were throwing bottles and the cops threw flashbangs and tear gas back."

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "How exciting."

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "It was! I escaped through someone's backyard. Then these dudes wearing masks started following me. I lost em by ducking into a cellar."

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "Wow! Breaking into a stranger's basement! That's a bright idea!"

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "I got caught, but the owner was in a good mood, so we drank beer together and drove to the bus station in his golf cart!"

    hide orion
    with easeoutright

    show ann disgust
    with easeinleft

    a "[o]! Drunk driving isn't good, even in a golf cart!"

    hide ann
    with easeoutleft

    show orion happy
    with easeinright

    o "And that's why I was hungover this morning!"

    hide orion
    with easeoutright

    return

label orion_argument:

    show ann smug
    with easeinleft

    a "So how's Floopsie?"

    hide ann
    with easeoutleft

    show orion sad
    with easeinright

    o "[a]..."

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "Are you still part of the {b}Floopsie Troopsie{/b}?"

    hide ann
    with easeoutleft

    show orion sad
    with easeinright

    o "[a]!!!"

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "So you {b}ARE{/b} still part of the {b}Floopsie Troopsie{/b}! That's so 2011!"

    hide ann
    with easeoutleft

    show orion sad
    with easeinright

    o "S...So what?!"

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "You know that's a Canadian cartoon right?"

    hide ann
    with easeoutleft

    # I actually like Canadians.

    show orion sad
    with easeinright

    o "E-Eh?"

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "Wow! You just said {i}eh{/i}! Those Canadian cartoons must be rubbing off on you!"

    hide ann
    with easeoutleft

    show orion smug
    with easeinright

    o "Cross check! Some Canadian cartoons are pretty good!"

    # Cross check is a hockey term, if you don't follow sports.

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "Yeah right! They always spill maple syrup on their animation cells!"

    hide ann
    with easeoutleft

    show orion smug
    with easeinright

    o "The maple tint problem stopped after the switch to digital animation!"

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "All their cartoons have mandatory French dubs!"

    hide ann
    with easeoutleft

    show orion smug
    with easeinright

    o "That's how I aced French class!"

    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "If you ever download a Canadian cartoon without paying, the red horsie cops will abduct you across the border!"

    hide ann
    with easeoutleft

    show orion smug
    with easeinright

    o "That's a lie! They aren't called the red horsie cops!"

    hide orion
    with easeoutright

    show ann happy
    with easeinleft

    a "Face it [o]. Your taste is garbage"

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "They're just cartoons!"

    hide orion
    with easeoutright

    return
