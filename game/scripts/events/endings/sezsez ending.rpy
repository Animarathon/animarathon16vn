# Animarathon XVI: Operation Ohio Sezsez Ending
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

label sezsez_ending:

    play sound switch37
    scene bg machine

    show sezsez liberty
    with easeinright

    sl "{size=70}THANK YOU! YEAH?{/size}"

    hide sezsez
    with easeoutright

    show ann genki
    with easeinleft

    a "Woah! You talked!"

    hide ann
    with easeoutleft

    show sezsez liberty
    with easeinright

    sl "{size=70}YEAH!{/size} {size=8}ahem{/size} We could {i}use you{/i}r help to get something!"
    # "You" being emphesised in "your" is not a typo.

    hide sezsez
    with easeoutright

    show ann normal
    with easeinleft

    a "Can't get it yourself huh? Let's hear it."

    hide ann
    with easeoutleft

    ann_thoughts "If the request is unreasonable I can always turn it down."

    show sezsez liberty
    with easeinright

    sl "In half an hour an IST admin will be moving a backup tape from Hayes Hall to Club Jerome."

    hide sezsez
    with easeoutright

    ann_thoughts "IST stands for Information Systems & Technology. That admin is a university employee!"

    show sezsez amadeus
    with easeinright

    sa "Our masks make us look sketchy, but you could get close for a snatch and grab."

    hide sezsez
    with easeoutright

    label sz_questions:

        menu:

            ann_thoughts "They want to hire me for a snatch and grab against the University. Do I have any questions?"

            "Are you out of your minds?":

                show sezsez liberty
                with easeinright

                sl "{size=70}YEAH!{/size}"

                hide sezsez
                with easeoutright

                show sezsez amadeus
                with easeinright

                sa "It's really not. Our guy on the inside set this up. We get the tape and they can justify a bigger budget for security."

                hide sezsez
                with easeoutright

                show sezsez liberty
                with easeinright

                sl "That admin normally doesn't do this because he's legally blind. We managed to get the right people to call off today so he has to run the tape."

                hide sezsez
                with easeoutright

                show sezsez amadeus
                with easeinright

                sa "This guy's old and blind, but he's still protective of his systems. Grab it and run or he might try to put up a fight."

                hide sezsez
                with easeoutright

                ann_thoughts "I'd rather not beat up a blind person."

                ann_thoughts "I'll have to be quick If I want to avoid a fight."

            "The University still uses data tapes?":

                show sezsez liberty
                with easeinright

                sl "Believe it or not {size=70}YEAH!{/size}"

                hide sezsez
                with easeoutright

                show ann normal
                with easeinleft

                a "Most consumers stopped using data tapes by the 1990's. I'm guessing there's a reason for that?"

                hide ann
                with easeoutleft

                show sezsez amadeus
                with easeinright

                sa "Darn straight. Why clog up the intranet when you can sneaker it over faster anyway?"

                hide sezsez
                with easeoutright

                show sezsez liberty
                with easeinright

                sl "Their first generation IVY-N 3593 tapes hold 300GB each, which is more then enough for administration data."

                hide sezsez
                with easeoutright

                show ann normal
                with easeinleft

                a "So what if you get the tape though? University data is almost always encrypted and unreadable in transit."

                hide ann
                with easeoutleft

                show sezsez amadeus
                with easeinright

                sa "Yo that's for other departments! They didn't bother with software encryption and hardware encryption didn't get added till second gen drives."

                hide sezsez
                with easeoutright

                show ann normal
                with easeinleft

                a "Then once we have the drive, there should be nothing stopping us from reading the data?"

                hide ann
                with easeoutleft

                show sezsez liberty
                with easeinright

                sl "{size=70}YEAH!{/size}"

                hide sezsez
                with easeoutright

            "YEAH!":

                ann_thoughts "They probably wouldn't invite me to commit a felony unless they had a good reason."

                show sezsez liberty
                with easeinright

                sl "{size=70}YEAH!{/size}"

                hide sezsez
                with easeoutright

                jump tape_ask

            "NAH!":

                ann_thoughts "Robbing blind people? How disgusting."

                show sezsez liberty
                with easeinright

                sl "That's a shame..."

                hide sezsez
                with easeoutright

                show sezsez amadeus
                with easeinright

                sa "Plan B then. Man I didn't wanna risk this..."

                hide sezsez
                with easeoutright

                return

label tape_ask:

    show ann smug
    with easeinleft

    a "So why do you want this tape? Looking for dirt? Slipping in some fake data? Or does information just wanna be free?"

    hide ann
    with easeoutleft

    show sezsez amadeus
    with easeinright

    sa "We're shaking the hornets nest so they'll pin it on someone who's actually a threat while we chill at our safehouse."

    hide sezsez
    with easeoutright

    show sezsez liberty
    with easeinright

    sl "You're aware of [fs]. We're looking to shut him down before he can shut {b}us{/b} down. Lots of people saw you with him earlier."

    hide sezsez
    with easeoutright

    show ann smug
    with easeinleft

    a "Oh, I'm well acquainted with [fs]. I guess my brother wasn't the only person he's targeting here."

    hide ann
    with easeoutleft

    show sezsez liberty
    with easeinright

    sl "Lots of people saw you with him earlier. Once that tape gets stolen we'll let it slip that he coerced you into doing it."

    hide sezsez
    with easeoutright

    show sezsez amadeus
    with easeinright

    sa "You're OK with being a deniable asset right? Just play along and we'll cover you."

    hide sezsez
    with easeoutright

    show ann normal
    with easeinleft

    a "If you know [fs] is up to something, why can't the police take care of it?"

    hide ann
    with easeoutleft

    show sezsez amadeus
    with easeinright

    sa "Dude's crazy, but he's sneaky with crime. There's never enough when we snitch on that guy, even when he'd kidnapping dudes."

    hide sezsez
    with easeoutright

    show ann smug
    with easeinleft

    a "So you're pinning a crime he didn't commit on him? Won't that just backfire when they prove he's innocent."

    hide ann
    with easeoutleft

    show sezsez liberty
    with easeinright

    sl "Not entirely. In a very direct way [fs] is coercing us to do this."

    hide sezsez
    with easeoutright

    show sezsez amadeus
    with easeinright

    sa "Yo just spit it out man. [fs] is gonna drop a few billion mofos tonight including us unless we catch him with his pants down."

    hide sezsez
    with easeoutright

    show ann embarrassed
    with easeinleft

    a "Wait did I hear that right? How could [fs] possibly kill a few billion people?"

    hide ann
    with easeoutleft

    show sezsez liberty
    with easeinright

    sl "That's why there was pachinko this year. It's a cover for his insidious plan."

    hide sezsez
    with easeoutright

    show sezsez amadeus
    with easeinright

    sa "Those balls are weapons that will surpass anything mankind has seen before."

    hide sezsez
    with easeoutright

    show ann genki
    with easeinleft

    a "Pshaw! You almost had me going for a minute there."

    hide ann
    with easeoutleft

    show sezsez liberty
    with easeinright

    sl "This is no prank. Underneath that sleek exterior, are two incredibly potent chemical weapons."

    hide sezsez
    with easeoutright

    show sezsez amadeus
    with easeinright

    sa "That motherfrogger double dipped us! These balls have a lanthanum clay under the crust, and a pure scandium core on the inside!"

    hide sezsez
    with easeoutright

    show ann smug
    with easeinleft

    a "Yo! Chemistry major checking in! Lanthanum and Scandium are just elements! Mostly harmless too! Sounds like you got duped!"

    hide ann
    with easeoutleft

    show sezsez amadeus
    with easeinright

    sa "Yo iron's just an element too and you can make bullets outta that! Just listen up while lady liberty explains!"

    hide sezsez
    with easeoutright

    menu:

        "Give me the long version":

            show sezsez liberty
            with easeinright

            sl "Thanks. That lanthanum clay is the part of a plan to artificially induce a limnic eruption in Lake Erie."

            hide sezsez
            with easeoutright

            show ann normal
            with easeinleft

            a "I've never heard of a limnic eruption before. What's that?"

            hide ann
            with easeoutleft

            show sezsez liberty
            with easeinright

            sl "A limnic eruption occurs when a lake builds up carbon dioxide for an extended period of time, then releases it all at once."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "It's like the nastiest fart ever. It pushes all the oxygen up a few stories and you choke to death."

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "Lake Erie is already supersaturated with carbon dioxide and despite being a holomictic lake. The water cycle just isn't fast enough in a great lake."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "Translation: Lake Erie's drinking a diet soda after it ate three jumbo meals with extra dip. It ain't working!"

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "The algae in Lake Erie are one of the major factors keeping that gas in check. That lanthanum clay will kill them off for a while."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "The only good thing is that this is temporary. It has to be a clay, pure lanthanum won't bind phosphors needed for this to work."

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "The other requirement is significant geological activity. Fortunately the Liberty Gravity Anomaly and Bowling Green Faultline are mostly dormant."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "There's a reason why [fs] hired some noisy DJs for that rave tonight though! And it ain't because he don't turn down!"

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "[fs]'s hid several large surface transducers across town, and synced them with the music to just make it sound like a really loud rave."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "But when they crank that music to 11, Molly ain't the only thing that's gonna be popping tonight!"

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "The CO2 ejected from the great lakes would extend several miles inland before dispersing. There would be no warning."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "Detroit, Toledo, Cleveland, and Buffalo! Taken out! We'd get capped too, unless we pack everyone in the top of the library."

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "That's nothing compared to what the scandium is going to do though."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "Lake Erie eventually drains to the Atlantic. After that the currents will cause total global saturation."

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "Algae treats scandium like essential nutrients, but scandium has no nutritional value."
            # Iron specifically

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "It's like an all you can eat laundry detergent capsule buffet."

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "All the algae in the oceans would die of malnutrition."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "Since all life in the ocean eventually relies on algae, they too would eventually die."

            hide sezsez
            with easeoutright

            show sezsez liberty
            with easeinright

            sl "All the global communities that rely on fish to survive would be displaced at best, and war for food at worst."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "Kiss your sushi goodbye."

            hide sezsez
            with easeoutright

        "Give me the quick version":

            show sezsez amadeus
            with easeinright

            sa "[fs] is gonna gas the midwest and kill all the life in the ocean to make a global famine. You in or what?"

            hide sezsez
            with easeoutright

        "Let's just do this":

            show sezsez amadeus
            with easeinright

            sa "Rock on!"

            hide sezsez
            with easeoutright

        "I'm out. See you.":

            ann_thoughts "These guys are nuts if they think pure elements are that dangerous."

            show sezsez liberty
            with easeinright

            sl "That's a shame..."

            hide sezsez
            with easeoutright

            show sezsez amadeus
            with easeinright

            sa "Plan B then. Man I didn't wanna risk this..."

            hide sezsez
            with easeoutright

            return

    show ann normal
    with easeinleft

    a "How do you even know [fs] was planning this?"

    hide ann
    with easeoutleft

    show sezsez amadeus
    with easeinright

    sa "How do you think we know this? He hangs with my bro and gloated bout his plan. We looked into it and everything checks out!"

    hide sezsez
    with easeoutright

    show sezsez liberty
    with easeinright

    sl "If you get caught on the way back, spill the drink you got at rays on them, then toss the fries on them."

    hide sezsez
    with easeoutright

    show sezsez amadeus
    with easeinright

    sa "It won't distract them for too long. Make sure you jet after that!"

    hide sezsez
    with easeoutright

    show ann normal
    with easeinleft

    a "OK, let's do this..."

    hide ann
    with easeoutleft

    #  _____ _            _   _      _     _   
    # |_   _| |__   ___  | | | | ___(_)___| |_ 
    #   | | | '_ \ / _ \ | |_| |/ _ \ / __| __|
    #   | | | | | |  __/ |  _  |  __/ \__ \ |_ 
    #   |_| |_| |_|\___| |_| |_|\___|_|___/\__|

    scene bg garden
    with dissolve

    show ist normal
    with easeinright

    ist "Hello, sir? I'm still on the esplanade right? I haven't passed by the library right?"

    hide ist
    with easeoutright

    show ann disgust
    with easeinleft

    a "This is a stick up. Hand over the tape, and I won't shoot you."

    hide ann
    with easeoutleft

    play sound switch37

    ann_thoughts "I click my heals to mimic the sound of a gun cock."

    show ist tape
    with easeinright

    ist "Take it! Oh happy days! Thanks for helping me justify a real budget for our department!"

    hide ist
    with easeoutright

    show ann happy
    with easeinleft

    a "Uhh, thanks? I'll be going now."

    hide ann
    with easeoutleft

    show ist shotgun
    with easeinright

    ist "Not so fast miss. I can hear well enough to know you were bluffing, and where to shoot. I only needed an attempted theft, not a real one."

    hide ist
    with easeoutright

    show ann disgust
    with easeinleft

    a "Look out! There are some dudes with rifles sneaking up on you!"

    hide ann
    with easeoutleft

    show ist shotgun
    with easeinright

    ist "I wasn't born yesterday! Come back in 10 years, and try that again {nw}"

    hide ist
    with hpunch

    show dns
    with easeinright

    dns "Sorry love, but this guy's ours! Let's give a cheer for our new tape!"

    hide dns
    with easeoutright
    
    ann_thoughts "Jam it! These guys are here for the tape too! What are the chances?"

    show dns
    with easeinright

    mobo "THREE ONE FOUR FIVE PI! PI! PI!" with hpunch

    dns "You've gotta be kidding me! You forgot a one!" with vpunch

    hide dns
    with easeoutright

    ann_thoughts "Time to log out! I'll have to shake them! I can't let them keep beating up that old guy though!"

    show ann disgust
    with easeinleft

    a "Special Delivery! Oops! Sorry about the spill!"

    hide ann
    with easeoutleft

    show dns
    with easeinright

    mobo "We said PI! Not FRY!" with hpunch
    
    mobo "The garlic is so strong we can taste it from behind our gasmasks!" with hpunch

    dns "Ohhhh.... I'm feeling a bit... Queasy..." with vpunch
    
    mobo "S-Sir! Urk" with hpunch

    hide dns
    with easeoutright
    
    mobo "It's sloshing around in my mask! Help!"

    ann_thoughts "That DMSO cocktail should preoccupy them for a while."

    show ann genki
    with easeinleft

    a "Zoinks!"

    hide ann
    with easeoutleft

    scene bg bowling green
    with dissolve

    ann_thoughts "Ducking into downtown Bowling Green should shake them before I meet back up with SEZSEZ on campus."

    ann_thoughts "If they're smart they won't even think about crossing Wooster Street!"

    scene bg film room
    with dissolve

    show sezsez liberty
    with easeinright

    sl "{size=70}YEAH!{/size} You made it!"

    hide sezsez
    with easeoutright

    show ann disgust
    with easeinleft

    a "You didn't tell me there were others going after that tape! Why not let them take the heat?"

    hide ann
    with easeoutleft

    show sezsez liberty
    with easeinright

    sl "{size=70}YEAH!{/size} But the moment he heard a rifle clinking around, he'd shoot the tape."

    hide sezsez
    with easeoutright

    show sezsez amadeus
    with easeinright

    sa "Bet he didn't think you were really armed too! Your distraction was just what we needed dog!"

    hide sezsez
    with easeoutright

    show sezsez liberty
    with easeinright

    sl "You did it though! The police locked down campus and started a manhunt! {size=70}YEAH!{/size}"

    hide sezsez
    with easeoutright

    show sezsez amadeus
    with easeinright

    sa "Our police scanner said [fs] was caught just five minutes before you got here! You did it bro!"

    hide sezsez
    with easeoutright

    jump end_good
