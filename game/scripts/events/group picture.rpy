# Animarathon XVI: Operation Ohio Satellite Picture
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

label satellite_group_picture:

    scene bg cherry
    with dissolve

    ann_thoughts "The air is crisp, and the cherry blossoms are in full bloom!"

    show frog sensei
    with easeinright

    fs "Welcome to our mandatory group photo tadpoles! Everyfroggy huddle up ribbit!"

    hide frog sensei
    with easeoutright

    show crowd
    with easeinbottom

    ann_thoughts "I'm being squashed... This better be over soon."

    fs "OK Everyfroggy! The photographer should be passing by soon! Please look up at the camera and croak!"

    show guest furry
    with easeinright

    guest_furry "Catgirl photographer where nya?"
    # Where is the female photographer dressed as a cat? (Cat noises)

    hide guest
    with easeoutright

    show frog sensei
    with easeinright

    fs "Oh, just about 450 kilometers away! It's a hop really ribbit!"

    hide frog sensei
    with easeoutright

    ann_thoughts "The air falls silent for a moment. The photographer isn't even here."

    show guest funky
    with easeinright

    guest_funky "Not groovy!"

    hide guest
    with easeoutright

    show guest gamer
    with easeinright

    guest_gamer "y0! 1 c0u1d b fr4gg1n n00bz! f5? f4! cy4!"
    # Hey! I could be killing new players! Refresh(F5) Frog Sensei (FS)? I'm quitting (F4) this! See you!

    hide guest
    with easeoutright

    show guest fairy
    with easeinright

    guest_fairy "Oy, [fs]! Photographs misalign my chakra! Namaste and Piss off!"

    hide guest
    with easeoutright

    show guest otaku
    with easeinright

    guest_otaku "[fs] commit Hara Kiri AND Seppuku, or I'll become hikikomori and never come here again!"
    # Frog Sensei, kill yourself by stabbing yourself in the gut twice to regain your honor, or I will become a shut in and never come here again!

    hide guest
    with easeoutright

    show guest traffic head
    with easeinright

    guest_traffic_head "What's going on?! Help me please!"

    hide guest
    with easeoutright

    show guest welchertaku
    with easeinright

    guest_welchertaku "Animarathon XVI was a mistake. 7/10 not enough Welchert."

    hide guest
    with easeoutright

    show guest cosplay cop
    with easeinright

    guest_cosplay_cop "I'm glad the photographer isn't here! Everyone here is dressed in crimes against fashion... Even me!"

    hide guest
    with easeoutright

    hide crowd
    with easeoutbottom

    ann_thoughts "Looks like it's just [fs], [o], and a few stragglers."

    show frog sensei
    with easeinright

    fs "The photographer is here ribbit! Look up and tongues out everyfroggy!"

    hide frog sensei
    with easeoutright

    menu:

        ann_thoughts "Should I look up?"

        "Look up.":

            show sky blue
            with dissolve

            ann_thoughts "The air looks particularly nice today."

            hide sky blue
            with dissolve

        "Don't look up":

            ann_thoughts "Everyone else is looking up at the sky."

            ann_thoughts "Nothing is happening."

    show frog sensei
    with easeinright

    fs "Tadpoles, thank you for participating in our first annual Group Satellite Picture!"

    hide frog sensei
    with easeoutright

    ann_thoughts "A group satellite picture? Somebody once told me modern Satellites have enough resolution to make out individuals."

    show orion
    with easeinright

    o "Wouldn't using a plane be cheaper for you?"

    hide orion
    with easeoutright

    show frog sensei
    with easeinright

    fs "Cheaper yes, but not nearly as cool ribbit! Besides, I have big plans for my plane!"

    hide frog sensei
    with easeoutright
    

    return
