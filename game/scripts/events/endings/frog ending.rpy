# Animarathon XVI: Operation Ohio Frog Sensei Ending
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

label frog_ending:

    menu:

        ann_thoughts "Is working with [fs] really a good idea?"

        "Ask for more information about his plan.":

            jump fs_explain

        "I'm down with whatever this is.":

            show frog sensei
            with easeinright

            fs "Excellent ribbit!"

            hide frog sensei
            with easeoutright

            jump fs_takeoff

        "I'm out. See you.":

            show frog sensei
            with easeinright

            fs "You'll understand one day ribbit! Sayonara tadpole!"

            hide frog sensei
            with easeoutright

            return

label fs_explain:

    show ann normal
    with easeinleft

    a "I've got to ask, why did you ruin Animarathon?"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "I think you mean, why did I {b}save{/b} Animarathon ribbit."

    hide frog sensei
    with easeoutright

    show ann disgust
    with easeinleft

    a "You've got a weird way of saving it then!"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "It is a bit weird ribbit. Take this, and you can help me save it"

    hide frog sensei
    with easeoutright

    ann_thoughts "[fs] places a tiny pill in my palm."

    show ann smug
    with easeinleft

    a "You literally kidnap people! You must think I'm a sucker to just expect me to take this!"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "You're a sucker if you don't take that ribbit. It's an antidote and you've been poisoned ribbit. Swallow it with your inferior human tongue ribbit."

    hide frog sensei
    with easeoutright

    show ann disgust
    with easeinleft

    a "This could be anything from a sugar pill to a cyanide pill. No way."

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "It's true though! Everyone in northwest Ohio has the vapors!"

    hide frog sensei
    with easeoutright

    show ann smug
    with easeinleft

    a "The vapors? I hate to tell you, but it's not 1855 anymore."

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "Alright, the full story then ribbit. Hydrogen Sulfide gas from the Great Black Swamp buried under BG has been leaking, causing mass delusions."

    hide frog sensei
    with easeoutright

    ann_thoughts "I've noticed brief bad smells sometimes around here. I always figured it was just someone who didn't shower."

    show frog sensei
    with easeinright

    fs "Hydrogen Sulfide poisons the brain. It cripples your attention span, judgment, and even your memory. I tried to distribute a cure, but it failed ribbit."

    hide frog sensei
    with easeoutright

    show ann smug
    with easeinleft

    a "I guess that explains why everyone is acting crazy. Since when did you give anyone a cure though?"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "You have two cures now ribbit. The pill I just gave you is effective, but the pachinko balls were not effective ribbit."

    hide frog sensei
    with easeoutright

    show ann smug
    with easeinleft

    a "Nobody is going to eat a pachinko ball!"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "They don't need to ribbit. They have a Lanthanum clay core under a perforated Rubidium coating."

    hide frog sensei
    with easeoutright

    ann_thoughts "Lanthanum is a rare-earth element. Most REEs like Terbium are used as alloys, and not clays."

    show frog sensei
    with easeinright

    fs "Lanthanum clay has a few uses, I was interested in it's ability to absorb hydrogen gas ribbit."

    hide frog sensei
    with easeoutright

    show ann normal
    with easeinleft

    a "That would help reduce Hydrogen Sulfide right? Your plan seems inefficient."

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "It wasn't enough at all ribbit. There is just too much gas to absorb ribbit."

    hide frog sensei
    with easeoutright

    show ann smug
    with easeinleft

    a "Maybe if you didn't break so many windows, less gas would get inside the building? What's causing this gas to leak anyway?"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "Microcystins ribbit. Algae Blooms from Lake Erie are pumping out way more of that stuff then normal, and it's reached the aquifer-ibbit."

    hide frog sensei
    with easeoutright

    show ann normal
    with easeinleft

    a "Do you think the aquifer and the gas release are linked?"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "Microcystins contain acid ribbit. Dissolve and shift just a little dirt over a large area, and you release a lot of trapped gas ribbit."

    hide frog sensei
    with easeoutright

    show ann normal
    with easeinleft

    a "So what are you gonna do about it? I don't see how these balls can deal with the algae."

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "Lanthanum clay is also a phosphate binder. By sealing away their food source, algae are brought back to manageable levels ribbit."

    hide frog sensei
    with easeoutright

    show ann normal
    with easeinleft

    a "Things that can't eat starve to death!"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "Correct ribbit. We're gonna dump these balls in Lake Erie and kill the algae ribbit!"

    hide frog sensei
    with easeoutright

    menu:

        ann_thoughts "[fs] has told me his plan. Should I take his so called antidote and work with him?"

        "I'm in.":

            show frog sensei
            with easeinright

            fs "Excellent ribbit!"

            hide frog sensei
            with easeoutright

        "I'm out.":

            show frog sensei
            with easeinright

            fs "You'll understand one day ribbit! Sayonara tadpole!"

            hide frog sensei
            with easeoutright

            return

    jump fs_takeoff

label fs_takeoff:

    scene bg port

    show plane at right

    show frog sensei
    with easeinright

    fs "This is our last lily pad before the hop ribbit."

    hide frog sensei
    with easeoutright

    show ann normal
    with easeinleft

    a "Are you just going to take that?"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "I own this dragonfly ribbit. Picked this croaker up on the side of the road ribbit. It can hardly hop, but it's my polliwog ribbit."

    hide frog sensei
    with easeoutright

    show ann normal
    with easeinleft

    a "We can both fly in that? How much prep work do we need?"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "I modded it into a twinseater ribbit. I preped it last night, so now all it needs is a pre hop check."

    hide frog sensei
    with easeoutright

    show black
    with dissolve

    pause(3.0)

    hide black
    with dissolve

    show frog sensei
    with easeinright

    fs "Are you ready to become a frog, tadpole?"

    hide frog sensei
    with easeoutright

    menu:

        ann_thoughts "Do I really want to go along with this?"

        "Yes":

            show frog sensei
            with easeinright

            fs "Excellent ribbit!"

            hide frog sensei
            with easeoutright

        "No":

            show frog sensei
            with easeinright

            fs "You'll understand one day ribbit! Sayonara tadpole!"

            hide frog sensei
            with easeoutright

            return

    show ann normal
    with easeinleft

    a "Let's do this."

    hide ann
    with easeoutleft

    show black
    with dissolve

    pause(3.0)

    hide plane

    hide black
    with dissolve

    # Poorly Animated Takeoff

    #show plane takeoff at offscreenleft

    #hide plane
    #with easeoutright

    # Poorly Animated Police Chase

    #show police car at offscreenleft

    #hide police car
    #with easeoutright

    #system "Holy cow"

    scene bg clouds:

    menu:

        fs "I need you to set the landing gear switch to {b}retracted{/b} ribbit."

        "Retract landing gear":

            play sound switch37

            a "Landing gear retracted."

        "Hit the eject button":

            jump ejection_ending

    fs "Good work tadpole"

    show plane fly at truecenter
    with easeinleft

    fs "That was close ribbit."

    a "Nobody can stop us now that we're flying through, right?"

    fs "It's only you and me ribbit. And the Ohio Air Force ribbit."

    a "I forgot Ohio has their own Air Force. Do we stand a chance against their G-16 planes?"

    fs "No-bit. If we get this done right, we can bail before they scramble."

    a "What about the Ohio Navy?"

    fs "Croak. They only use the water. A frog like me can outrun them to middle island in Canada no problem ribbit!"

    menu:

        fs "Arpoaching optimal deployment position. {b}Release{/b} the primary safety ribbit."

        "Release primary safety":

            play sound switch37

            a "Primary safety is off."

        "Hit the eject button":

            jump ejection_ending

    fs "Good work tadpole."

    menu:

        fs "{b}Release{/b} the secondary safety ribbit."

        "Release secondary safety":

            play sound switch37

            a "Secondary safety is off."

        "Hit the eject button":

            jump ejection_ending

    fs "Good work tadpole."

    menu:

        fs "{b}Release{/b} the final safety ribbit."

        "Release final safety":

            play sound switch37

            a "Final safety is off."

        "Hit the eject button":

            jump ejection_ending

    fs "Good work tadpole."

    menu:

        fs "{b}Power on{/b} the payload bay door motors."

        "Power on door motors":

            play sound switch37

            a "Payload door motors activated."

            ann_thoughts "Huh. The light didn't change."

            a "Negative function [fs]."

        "Hit the eject button":

            jump ejection_ending

    fs "Ribbit?"

    menu:

        fs "{b}Fire{/b} explosive charge 3 to knock the door open."

        "Fire explosive charge 3":

            play sound switch37

            a "Explosive charge fired."

            ann_thoughts "Huh. The light didn't change. I definately didn't feel an explosion either."

            a "Negative function [fs]."

        "Hit the eject button":

            jump ejection_ending

    hide plane fly
    with easeoutleft

    ann_thoughts "Holy Toledo! He poped the cockpit open and climbed out! We're gonna die!" with vpunch

    ann_thoughts "Everything is shaking terribly! I can't even yell for him to stop!" with vpunch

    ann_thoughts "He's... Climbing back in..." with vpunch

    ann_thoughts "Woah! He just did a barrel roll to slam the cockpit shut! Wow!" with vpunch

    show plane fly at truecenter
    with easeinleft

    fs "Ribbit? You're still conscious? I ripped the doors off ribbit."

    menu:

        fs "{b}Activate{/b} pachinko deployment mechanism."

        "Activate deployment mechanism":

            play sound switch37

            a "Deployment mechanism activated."

            ann_thoughts "Huh. The light didn't change."

            a "Negative function [fs]."

        "Hit the eject button":

            jump ejection_ending

    fs "Croak! I checked that while I was down there!."

    menu:

        fs "{b}Fire{/b} the emergency solenoid."

        "Fire the emergency solenoid":

            play sound switch37

            a "Solenoid fired."

        "Hit the eject button":

            jump ejection_ending

    hide plane fly
    with easeoutright

    stop music fadeout 1

    show black
    with dissolve

    fs "Good work tadpole! That's ribb-it."

    play music promenade_medium fadeout 1

    scene bg gameover
    with dissolve

    ann_thoughts "Thousands of silver balls fall behind us."

    ann_thoughts "Our precious water has been purified, but our lives have been cursed."

    ann_thoughts "Actions like this have all manner of consequences."

    ann_thoughts "I've done what I can. One can only hope for the best"

    system "{size=70}End(World);{/size}"

    $ renpy.full_restart()

label ejection_ending:

    stop music fadeout 1

    play sound switch37

    hide plane fly
    with easeoutbottom

    show white
    with dissolve

    show frog sensei angry
    with dissolve

    fs "{size=50}YOU TOAD!!! I HOPE YOU CROAK!!!{/size}"

    hide frog sensei
    with dissolve

    play music promenade_medium fadeout 1

    scene bg gameover
    with dissolve

    a "I accept our fates."

    ann_thoughts "Thousands of silver balls fall within our chariot, still sealed in their container."

    ann_thoughts "The horizon is clear, our actions observed. It is only a matter of time before we are rescued from our fate."

    ann_thoughts "I've done what I can. One can only hope for the best."

    system "{size=70}End(Story);{/size}"

    $ renpy.full_restart()
