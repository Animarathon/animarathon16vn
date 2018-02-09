# Animarathon XVI: Operation Ohio Robot Panel
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
#  ____       _           _     ____                  _ 
# |  _ \ ___ | |__   ___ | |_  |  _ \ __ _ _ __   ___| |
# | |_) / _ \| '_ \ / _ \| __| | |_) / _` | '_ \ / _ \ |
# |  _ < (_) | |_) | (_) | |_  |  __/ (_| | | | |  __/ |
# |_| \_\___/|_.__/ \___/ \__| |_|   \__,_|_| |_|\___|_|
#  ____                  _   ____  _
# |  _ \ __ _ _ __   ___| | |  _ \| | __ _ _ __  
# | |_) / _` | '_ \ / _ \ | | |_) | |/ _` | '_ \ 
# |  __/ (_| | | | |  __/ | |  __/| | (_| | | | |
# |_|   \__,_|_| |_|\___|_| |_|   |_|\__,_|_| |_|
#
# By the end of the panel the player should experience the following outcomes.
#
# ! Positive Outcome (Player doesn't nap.)
# 💭 Learn about robots and their components.
# 💭 Relate robots in anime with robots in the real world.
# $ Gain a in game reward for learning.
# Ψ Feel that this learning was done of their own free will.
#
# ! Negative Outcomes (The player took a nap.)
# 💭 Experience some minor wordplay.
# $ Gain a in game reward to encourage better sleeping habits.
# Ψ Feel that this choice was made of their own free will. 

label robot:

    scene panel room wet
    with dissolve

    play music moist_mechas fadeout 1

    show text "{size=70}Chapter 4: Robot Revolution!{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard='True')
    
    hide text
    with dissolve

    show crowd
    with easeinbottom

    jump robot_menu

label robot_menu:

    menu:

        ann_thoughts "Looks like the mecha panel is about to start. What should I do?"

        "Stay awake for the panel":

            call robot_awake

        "Consider the Panel":

            call robot_considerations

            jump robot_menu

        "Take a nap outside the panel":

            call robot_asleep

    stop music fadeout 1

    return

label robot_awake:

    show roe burt
    with easeinright

    rb "Beep beep boop beep! Welcome to the mecha panel!"

    hide roe burt
    with easeoutright

    show roe burt point
    with easeinright

    rb "{size=50}SPARKLING FINGERED!{/size}"

    hide roe burt
    with easeoutright

    show roe burt
    with easeinright

    rb "My special move has picked you! What should we cover chosen one?"

    hide roe burt
    with easeoutright

    menu:

        ann_thoughts "She's pointing at me."

        "Giant Robots":

            show roe burt
            with easeinright

            menu:

                rb "In anime we often see giant robots. Does anyone know why a giant mecha is hard to build?"

                "Biology":

                    hide roe burt
                    with easeoutright

                    show guest fairy
                    with easeinright

                    guest_fairy "Oy lass! How can robots use biology if metal ain't meat?"

                    hide guest
                    with easeoutright

                    show roe burt
                    with easeinright

                    rb "In Biology the square cube law governs how much a bone can support weight. The same is true for how much weight metal can carry."

                    hide roe burt
                    with easeoutright

                    show guest fairy
                    with easeinright

                    guest_fairy "Aye! That be true! That's why you rarely see animals larger then a horse!"

                    hide guest
                    with easeoutright

                    show roe burt
                    with easeinright

                    rb "Indeed. Some anime do describe how their mecha designs get around the square cube law though."

                    menu:

                        rb "More importantly, what would be a cool name for a biology inspired mecha move?"

                        "Genome Splice!":

                            rb "Short and simple! I like it!"

                        "Lamark's Iron Revengance!":

                            rb "A great name for a move inherited from a prototype!"

                        "Mendel's Supreme Law of Dominance!":

                            rb "A dominating name for a dominating move! Nice!"

                        "Twenty Three Special!":

                            rb "That's a good name for a human inspired move!"

                    hide roe burt
                    with easeoutright

                "Battery":

                    hide roe burt
                    with easeoutright

                    show guest furry
                    with easeinright

                    guest_furry "Nyaa ~~ Everyone knows giant robots use puur-propane, not batteries! Meow!"

                    hide guest
                    with easeoutright

                    show roe burt
                    with easeinright

                    rb "That's kind of right. Normal batteries aren't enough for giant robots. Generators or power cables are often used, but they can limit mobility."

                    menu:

                        rb "More importantly, what would be a cool name for a battery inspired mecha move?"

                        "Lithium Ejection!":

                            rb "A great name for getting rid of a lithium battery!"

                        "Battery Bukkake":

                            rb "A great name for a move where many batteries are discharged at once!"

                        "MALE TO MALE CHARGER MATING GO!":

                            rb "Male to Male connectors aren't common, but they do exist!"

                        "Super Neo Overcharge":

                            rb "Some battery chemistries can explode when overcharged... This is a great name for a desperation attack!"

                    hide roe burt
                    with easeoutright

        "Robots without microcomputers":

            show roe burt
            with easeinright

            rb "There is indeed a branch of robotics that forgoes typical computers. By using analogue electronics and Nv Neurons we can mimic biology."

            hide roe burt
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "h0wz n0 c0mpu73r b3t3r d00d?"
            # How's no computer better my dude?

            hide guest
            with easeoutright

            show roe burt
            with easeinright

            rb "Not using a typical computer can provide some benefits of biological systems, like robustness. Doing so forfeits digital advantages of course."

            hide roe burt
            with easeoutright

        "Robot parts":

            show roe burt
            with easeinright

            rb "There are a wide variety of robot parts. Can you narrow down what you'd like to talk about?"

            hide roe burt
            with easeoutright
            
            menu:

                ann_thoughts "What robot part should I pick?"

                "Computers":

                    show roe burt
                    with easeinright

                    rb "Most robots use microcontrollers which typically integrate 8bit RISC CPUs with several kilobytes of memory and IO."

                    hide roe burt
                    with easeoutright

                    show ann normal
                    with easeinleft

                    a "Isn't that a bit limiting for some robots?"

                    hide ann
                    with easeoutleft

                    show roe burt
                    with easeinright

                    rb "Some robots will use 32bit or 64bit multicore processors with powerful digital signal coprocessors, GPGPU's for machine vision, and gigabytes of RAM."

                    hide roe burt
                    with easeoutright

                    show guest gamer
                    with easeinright

                    guest_gamer "50undz l13k my r1g! Wh1 d0n7 m04r r0b07z u53 7h053?"
                    # That sounds like my gaming computer! Why don't more robots use parts like that?

                    hide guest
                    with easeoutright

                    show roe burt
                    with easeinright

                    rb "More powerful parts typically cost more, use more power, and increase complexity with more software and cooling. It's not always the best choice."

                    menu:

                        rb "More importantly, what would be a cool name for a computer inspired mecha move?"

                        "DEEP UNDERCLOCK":

                            rb "Underclocking an underused processor can help extend battery life!"

                        "THERAD-42":

                            rb "A grim reminder that sometimes software safeties aren't enough."

                        "Halt and Catch Fire":

                            rb "A last ditch instruction to securely wipe a chip!"

                        "UPLOAD.SH --i REBOOT --o UR_MAINFRAME":

                            rb "Rebooting an entire mainframe at a critical time could cause a lot of damage!"

                    hide roe burt
                    with easeoutright

                    hide roe burt
                    with easeoutright

                "Motors":

                    show roe burt
                    with easeinright

                    rb "Regular motors are good for general movement, and servo motors are good for controlled movement."

                    menu:

                        rb "More importantly, what would be a cool gimmick for a fast mecha?"

                        "Racecar transformation!":

                            rb "Good idea! Sometimes wheels are faster then legs!"

                        "Orange Paint":

                            rb "A combination of gold and crimson? I'd have to be at least 6 times faster! It's also great for school spirit!"

                        "Grappling Hook":

                            rb "Grappling hooks are always cool!"

                        "Super Fast Tunnel Drilling!":

                            rb "A cool practical device that can double as an attack!"

                    hide roe burt
                    with easeoutright


                "Sight Sensors":

                    show roe burt
                    with easeinright

                    rb "I see you want to see how a robot sees? Robots can use sonar for distance as well as photocells for levels of light and color."

                    hide roe burt
                    with easeoutright

                    show guest gamer
                    with easeinright

                    guest_gamer "Wu7 1f 4 rl r0b07 s33 7h1ng5 11k3 41mb0t?"
                    # What if a real life robot saw things like an aimbot?

                    hide guest
                    with easeoutright

                    show roe burt
                    with easeinright

                    rb "For better sight a camera is needed. Unfortunately vision is one of the things robots and humans don't see eye to eye on."

                    menu:

                        rb "More importantly, what would be a cool name for a sight inspired mecha move?"

                        "Scanlation Ripper!":

                            rb "Ah! What a beautiful name for Optical Character Recognition!"

                        "NO.IR Camera":

                            rb "Dealing with infrared light could help robots get an imagery advantage!"

                        "WIDE ANGLE SHOT":

                            rb "Using a wide angle lens can help give a robot peripheral vision! Remember to watch for distortion!"

                        "PHOTOVORE TACTICS":

                            rb "Maximising sunlight exposure is important behavior for any autonomous solar powered robot."

                    hide roe burt
                    with easeoutright

                "Hearing Sensors":

                    show roe burt
                    with easeinright

                    rb "Listen up! Robots often use microphones for hearing. Detecting loud noises is easy, but processing language is tough."

                    menu:

                        rb "More importantly, what would be a cool name for a hearing inspired mecha move?"

                        "SONAR SCANNER":

                            rb "SONAR can be used to see, even in the dark!"

                        "GUNSHOT Microphone":

                            rb "Special software could scan for noises like gunshots, great for a robot cop or a robot soldier!"

                        "GALO GEOPHONE":

                            rb "Listening to movement in the earth is good for more then earthquakes! You could also listen for a giant robot walking towards you!"

                        "SDR REVENGENCE":

                            rb "A robot might be able to use a SDR to intercept frequencies or for van eck phreaking!"
                            # SDR = Software Defined Radio here.

                    hide roe burt
                    with easeoutright

                "Touch Sensors":

                    show roe burt
                    with easeinright

                    rb "Crude touch sensors are possible with bumper switches and whiskers. Touching isn't it?"

                    menu:

                        rb "More importantly, what would be a cool name for a touch inspired mecha move?"

                        "Sparkling Fingered!":

                            hide roe burt
                            with easeoutright

                            show roe burt point
                            with easeinright

                            rb "{size=50}THAT'S MY MOVE BUDDY!{/size}"

                            rb "{size=50}SPARKLING FINGERED!{/size}"

                        "As touching as [favorite_anime]!":

                            rb "I haven't seen [favorite_anime] before. Is it touching?"

                        "Zettai Ryoiki Field":

                            rb "Enhanced sensors around weak points can help it avoid damage!"

                        "Touchscreen":

                            rb "A touchscreen seems like a lame addition, but you could use it to display sponsor ads on a mecha for big money!"

                    hide roe burt
                    with easeoutright

                "Smell Sensors":

                    show roe burt
                    with easeinright

                    rb "Robot smell? It stinks! Although gas sensors can detect specific gasses like methane or alcohol."

                    menu:

                        rb "More importantly, what would be a cool name for a smell inspired mecha move?"

                        "Alcohol Tracer":

                            rb "A good skill for a police robot!"

                        "METH MUNCHER":

                            rb "Methane can be a dangerous gas! Detecting it and removing it could be a very useful feature!"

                        "PHEROMONE++":

                            rb "A social robot might use pheromones for an added edge, or to help overcome the uncanny valley!"

                        "Co2 Scanner":

                            rb "Co2 poisoning isn't a danger for robots, but it might be for nearby people or a pilot!"

                    hide roe burt
                    with easeoutright

                "Taste Sensors":

                    show roe burt
                    with easeinright

                    rb "Most robots don't eat food, but with pH sensors a robot can measure if something is sour or bitter."

                    menu:

                        rb "More importantly, what would be a cool name for a taste inspired mecha move?"

                        "Acid Ahegao":

                            rb "In chemistry acids are sour. A strong acid could make you do more then pucker up!"

                        "Basic Bukkake":

                            rb "In chemistry bases are bitter. Getting bases all over you would be very bitter!"

                        "REACTOR Regurgitate":

                            rb "Depending on what powers the reactor, spilling out fuel could be an effective attack."

                        "WAR VORE":

                            rb "A robot eating robots? That doesn't make too much sense but it's pretty metal!"

                    hide roe burt
                    with easeoutright

                "Other Sensors":

                    show roe burt
                    with easeinright

                    rb "With hall effect sensors and Geiger tubes, robots can potentially sense things we can not."

                    menu:

                        rb "More importantly, what would be a cool name for a weird mecha move?"

                        "BACKGROUND COUNTER":

                            rb "Like a way to counter the background count of an area? That's a pretty good idea!"

                            hide roe burt
                            with easeoutright

                        "HALL EFFECTOR":

                            rb "Using the hall effect to detect nearby magnets could be very useful, even when other sensors have failed."

                            hide roe burt
                            with easeoutright

                        "Nuclear Launch Detector x3000":

                            rb "Using a nuclear launch detector chip can allow electronics to shut down, making them slightly less vulnrable to EMP!"

                            hide roe burt
                            with easeoutright

                            # I know this doesn't sound like a real thing, but it totally is. Amazing isn't it?
                            # If you're nearby the machine that needs to use this you're totally screwed though!

                        "Pilot SQUID":

                            rb "A SQUID could be useful for a brain to computer interface!"

                            hide roe burt
                            with easeoutright

                            ann_thoughts "What was the mnemonic for SQUID again? Superconducting Quantum Interference Device?"

    show roe burt
    with easeinright

    rb "Beep boop! It's time for the first ever {size=50}ANIMECHATHON!{/size}"

    hide roe burt
    with easeoutright

    ann_thoughts "Animechathon?"

    show roe burt
    with easeinright

    rb "PREPARE FOR GEAR GURO AS THESE ROBOTS TEAR EACHOTHER APART COG BY COG! IN THE ARENA IT'S KILL OR BE KILLED! PLACE YOUR BETS AND SPIN THOSE SERVOS!"

    hide roe burt
    with easeoutright

    menu:

        ann_thoughts "The room is getting pretty packed."

        "Get in the robot fight!":

            ann_thoughts "I can use one of the loner robots."

            ann_thoughts "Aww shoot. MO-E Mecha? I bet it's designed to be moe and nothing else."

            call robot_fight

        "Do not get in the robot right.":

            ann_thoughts "I better run out of here."

    return

label robot_fight:

    show roe burt
    with easeinright

    rb "Looks like we've got a last minute sign up folks! Why don't you introduce yourself?"

    hide roe burt
    with easeoutright

    menu:

        ann_thoughts "How should I address the crowd?"

        "Use my real name.":

            show ann genki
            with easeinleft

            a "I'm [a] and this is my MO-E Mecha!"

            hide ann
            with easeoutleft

        "Use an alias.":

            show ann genki
            with easeinleft

            a "I'm [online_handle] and this is my MO-E Mecha!"

            hide ann
            with easeoutleft

        "Use a stupid name.":

            show ann genki
            with easeinleft

            a "I'm [a] computer and this is my MO-E Mecha!"

            hide ann
            with easeoutleft

        "Boast.":

            show ann genki
            with easeinleft

            a "I'm gonna destroy the competition and this is my MO-E Mecha!"

            hide ann
            with easeoutleft

    show roe burt point
    with easeinright

    rb "FIRST UP! {b}CLEANING ROBOT WITH A KATANA{/b} VERSUS {b}MO-E MECHA{/b}"

    hide roe burt
    with easeoutright

    show cleaning robot
    with easeinleft

    menu:

        ann_thoughts "This controller has a few buttons. What should I push?"

        "{s}Big Jump{/s} BIPEDAL OVERDRIVE LUNGE":

            pass

        "{s}Little Jump{/s} GRASSHOPPER LEAP":

            pass

        "{s}MEGA OVERDRIVE{/s} note: mega overdrive broke":

            ann_thoughts "It's not responding anymore!"

            show roe burt point
            with easeinright

            rb "YOUR ROBOT BROKE! DISQUALIFIED!"

            hide roe burt
            with easeoutright

            return

    show moe mecha
    with easeintop

    hide cleaning robot
    with vpunch

    rb "LOOKS LIKE THE CLEANING ROBOT... GOT CLEANED! MO-E MECHA IS THE WINNER!"

    hide moe mecha
    with easeouttop

    show roe burt point
    with easeinright

    rb "NEXT UP! {b}A BALL WITH A COMPUTER TAPED TO IT{/b} WILL IT BE ABLE TO KNOCK THE {b}MO-E MECHA{/b} OFF BALANCE?"

    hide roe burt
    with easeoutright

    show ball robot
    with easeinright

    menu:

        ann_thoughts "This controller has a few buttons. What should I push?"

        "{s}Big Jump{/s} BIPEDAL OVERDRIVE LUNGE":

            pass

        "{s}Little Jump{/s} GRASSHOPPER LEAP":

            pass

        "{s}MEGA OVERDRIVE{/s} note: mega overdrive broke":

            ann_thoughts "It's not responding anymore!"

            show roe burt point
            with easeinright

            rb "YOUR ROBOT BROKE! DISQUALIFIED!"

            hide roe burt
            with easeoutright

            return

    show moe mecha
    with easeintop

    hide ball robot
    with vpunch

    rb "THE BALL HAS BURST! MO-E MECHA IS THE WINNER!"

    hide moe mecha
    with easeouttop

    show roe burt point
    with easeinright

    rb "NEXT UP! ME! {b}LETS DO THIS PUNK!{/b}"

    hide roe burt
    with easeoutright

    show ann disgust
    with easeinleft

    a "Are you crazy!? If I try to fight you you'll get killed!"

    hide ann
    with easeoutleft

    show roe burt point
    with easeinright

    rb "{b}THATS QUITTER TALK! IT'S KILL OR BE KILLED IN THE RING! THAT GOES FOR THE REFEREE TOO!{/b}"

    hide roe burt
    with easeoutright

    menu:

        ann_thoughts "This controller has a few buttons. What should I push?"

        "{s}Big Jump{/s} BIPEDAL OVERDRIVE LUNGE":

            show roe burt
            with easeinright

            ann_thoughts "Now's my chance!"

            hide roe burt
            with easeoutleft

            show moe mecha
            with easeintop

            ann_thoughts "What?! She dodged my attack!"
            with vpunch

            rb "HUMANS HAVE BETTER REFLEXES THEN ROBOTS IDIOT! I'M GONNA TEAR YOUR BOT A-PART!"

            show roe burt
            with easeinright

            hide roe burt
            with easeoutleft

            show roe burt
            with easeinright

            hide roe burt
            with easeoutleft

            show roe burt
            with easeinright

            hide roe burt
            with easeoutleft

            hide moe mecha
            with vpunch

            show roe burt point
            with easeinright

            rb "{b}LOOKS LIKE I WIN!{/b}"

            hide roe burt
            with easeoutright

        "{s}Little Jump{/s} GRASSHOPPER LEAP":

            show roe burt
            with easeinright

            ann_thoughts "Now's my chance!"

            hide roe burt
            with easeoutleft

            show moe mecha
            with easeintop

            ann_thoughts "What?! She dodged my attack!"
            with vpunch

            rb "HUMANS HAVE BETTER REFLEXES THEN ROBOTS IDIOT! I'M GONNA TEAR YOUR BOT A-PART!"

            show roe burt
            with easeinright

            hide roe burt
            with easeoutleft

            show roe burt
            with easeinright

            hide roe burt
            with easeoutleft

            show roe burt
            with easeinright

            hide roe burt
            with easeoutleft

            hide moe mecha
            with vpunch

            show roe burt point
            with easeinright

            rb "{b}LOOKS LIKE I WIN!{/b}"

            hide roe burt
            with easeoutright

        "{s}MEGA OVERDRIVE{/s} note: mega overdrive broke":

            # I was gonna have this electrocute Roe Burt to death when she touched the robot casing.
            # But that kind of tone change isn't cool.

            ann_thoughts "It's not responding anymore!"

            show roe burt point
            with easeinright

            rb "YOUR ROBOT BROKE! DISQUALIFIED!"

            hide roe burt
            with easeoutright

        "Put down the controller. Winning is not worth killing someone.":

            show ann normal
            with easeinleft

            a "There is no way to know for sure you won't get hurt in close proximity to a large robot. I forfeit."

            hide ann
            with easeoutleft

            show roe burt point
            with easeinright

            rb "{b}THAT'S RIGHT! PUTTING SAFETY ABOVE GLORY MAKES YOU A BAMF AND A WINNER IN MY BOOK!{/b}"

            hide roe burt
            with easeoutright

            python:
                achievement.grant("Robots!")
                money += 500

            ann_thoughts "I won $500!"

    return

#     _        _
#    / \   ___| | ___  ___ _ __  
#   / _ \ / __| |/ _ \/ _ \ '_ \ 
#  / ___ \\__ \ |  __/  __/ |_) |
# /_/   \_\___/_|\___|\___| .__/ 
#                         |_|
label robot_asleep:

    play music this_reminds_me_of_something_p4 fadeout 1

    show black
    with irisin

    a "Sleep is good. mmmm..."

    show orange
    with dissolve

    hide black
    with dissolve

    ann_thoughts "Don't wire wrap me..."

    show red
    with dissolve

    hide orange
    with dissolve

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "Please, don't make my buffer overflow..."

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

label robot_considerations:

    menu:
    
        ann_thoughts "Was there anything I wanted to consider before the panel starts?"

        "Who is the panelist?":

            ann_thoughts "[rb] is a professor of robotics at this university."

            ann_thoughts "She has a reputation for getting sidetracked and being eccentric."

            ann_thoughts "I wonder what she'll have to say?"

        "What are robots?":

            ann_thoughts "Robots are autonomous devices that preform work."

            ann_thoughts "Robots are popular in anime as mecha or characters."

        "That's all":

            return

    jump robot_considerations
