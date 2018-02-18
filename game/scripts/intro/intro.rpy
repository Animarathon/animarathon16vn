# Animarathon XVI: Operation Ohio Introductory Scene
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
#  ___       _
# |_ _|_ __ | |_ _ __ ___
#  | || '_ \| __| '__/ _ \ 
#  | || | | | |_| | | (_) |
# |___|_| |_|\__|_|  \___/ 

label intro:

    play music promenade_medium fadeout 1

    scene bg blossom
    with dissolve

    show text "{size=45}Centuries ago, this land was the Great Black Swamp.{/size}" at truecenter
    with dissolve

    $ renpy.pause(8.0, hard='True')

    hide text
    with dissolve

    scene bg building old
    with dissolve

    show text "{size=45}Today this land is Bowling Green, Ohio.{/size}" at truecenter
    with dissolve

    $ renpy.pause(6.0, hard='True')

    hide text
    with dissolve

    scene bg cherry
    with dissolve

    show text "{size=45}A small college town, where a small college anime convention is about to take place.{/size}" at truecenter
    with dissolve

    $ renpy.pause(6.0, hard='True')

    hide text
    with dissolve

    scene bg union tower
    with dissolve

    show text "{size=70}Chapter 0: Longitude Highway{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard='True')

    hide text
    with dissolve

    show text "{size=70}7:29A.M. - March 24th 2018{/size}" at truecenter
    with dissolve

    $ renpy.pause(2.45, hard='True')
    
    hide text
    with dissolve

    play music breathe fadeout 1

    show ann toast
    with easeinright

    a "Oh no! I'm running late for Animarathon!"

    hide ann
    with easeoutleft
    
    ann_thoughts "That's my brother over there. We were going to meet up at 7:20."

    show orion normal
    with easeinright

    o "Holy Toledo, It's good to see you again sis!"

    hide orion
    with easeoutright

    show ann normal
    with easeinleft

    a "It's good to see you again too [o]! How's the TSUN life treating you?"

    hide ann
    with easeoutleft

    ann_thoughts "TSUN is the university in Toledo [o] attends - Toledo State University Northern."

    show orion normal
    with easeinright

    o "What can I say? It's the work hard party hard life!"

    hide orion
    with easeoutright

    ann_thoughts "I can smell the cheap TSUNDERE booze from here, so he's being honest about the party part."
    
    ann_thoughts "TSUNDERE is what BG locals call TSUN Students. What does that stand for again?"

    show ann happy
    with easeinleft
    
    a "That's nice. Hey [o]. what does TSUNDERE stand for again?"
    
    hide ann
    with easeoutleft
    
    show orion smug
    with easeinright
    
    o "That's an easy one sis! It means {i}Toledo State University Northern Delightful Experts Raising Excellence{/i}."
    
    hide orion
    with easeoutright

    show ann smug
    with easeinleft

    a "I remember now! Down here it means {i}Those Students Up North Dreadfully Experiencing Remorseful Education{/i}. Thanks for jogging my noggin [o]!"

    hide ann
    with easeoutleft

    show orion smug
    with easeinright

    o "Oh yeah? What was the acronym for this school? {i}Beer's Great, Sex's ...{/i} Shoot, now I can't remember our acronym for your school!"

    hide orion
    with easeoutright
    
    show ann happy
    with easeinleft
    
    a "Don't let this chilly morning give you a brain freeze [o]! Let's wait for Animarathon to open inside!"

    hide ann
    with easeoutleft

    #  ___           _     _      
    # |_ _|_ __  ___(_) __| | ___ 
    #  | || '_ \/ __| |/ _` |/ _ \
    #  | || | | \__ \ | (_| |  __/
    # |___|_| |_|___/_|\__,_|\___|

    scene bg hallway fancy
    with dissolve

    show orion happy
    with easeinright
    
    o "Good idea sis! I remember that the acronym was actually BISHONEN, so I guess I was really off..."

    hide orion
    with easeoutright

    show ann happy
    with easeinleft
    
    a "Forget that! Check out how nice the newly renovated Student Union foyer is!"

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "Looks like they outdid themselves... Literally. Look how few volunteers there are."

    hide orion
    with easeoutright

    show ann normal
    with easeinleft
    
    a "Hey at least we are number one in line. All we need to do now is wait."

    hide ann
    with easeoutleft

    call display_time

    #  ____            _     _             _   _               ____            _
    # |  _ \ ___  __ _(_)___| |_ _ __ __ _| |_(_) ___  _ __   |  _ \  ___  ___| | 
    # | |_) / _ \/ _` | / __| __| '__/ _` | __| |/ _ \| '_ \  | | | |/ _ \/ __| |/ /
    # |  _ <  __/ (_| | \__ \ |_| | | (_| | |_| | (_) | | | | | |_| |  __/\__ \   <
    # |_| \_\___|\__, |_|___/\__|_|  \__,_|\__|_|\___/|_| |_| |____/ \___||___/_|\_\
    #            |___/

    show adorina normal
    with easeinright

    aa "Attention Animarathon guests desu! Registration is now open desu!"

    hide adorina
    with easeoutright

    show ann happy
    with easeinleft

    a "I'm paying for both of us!"

    hide ann
    with easeoutleft

    show adorina normal
    with easeinright

    aa "Gimmie twenty dollars desu! Thanks desu!"

    hide adorina
    with easeoutright

    show ann smug
    with easeinleft

    a "Erm, these aren't badges. These are two bags of metal marbles."

    hide ann
    with easeoutleft

    $ pachinko_discovered = True

    queue music yo_p0

    show adorina smug
    with easeinright

    menu:

        aa "Muda muda, that's right desu! Access to Animarathon is now decided with pachinko desu!"

        "What do you mean access?":

            aa "We didn't get enough volunteers for Animarathon desu. So now we ration access via pachinko desu!"

            hide adorina
            with easeoutright

            show orion normal
            with easeinright

            o "That's one of the stupidest things I've ever heard. How does that even work?"

            hide orion
            with easeoutright

            show adorina normal
            with easeinright

            aa "If a guest challenges you to pachinko you must accept desu. If you've got no balls we kick you out desu!"

            hide adorina
            with easeoutright

        "Can I have my $20 back please?":

            aa "Maybe if you beat me at pachinko desu."

            $ twenty_dollars = True

            hide adorina
            with easeoutright

        "Do you have a case of the vapors?":

            aa "The vapors are bad this year aren't they desu? I've got smelling salts if you need them desu."

            hide adorina
            with easeoutright

        "Let's get this over with.":

            hide adorina
            with easeoutright

            jump pachinko_tutorial_over

    show orion smug
    with easeinright

    o "[a], you remember the basics of pachinko right? Pachinko is pinball with gambling. Pachinko can also be a slot machine."

    hide orion
    with easeoutright

    show adorina smug
    with easeinright

    aa "You're seriously desulaying the line now desu."

    hide adorina
    with easeoutright

    show ann smug
    with easeinleft

    a "Let's do this!"

    hide ann
    with easeoutleft

label pachinko_tutorial_over:

    play music eurobeat fadeout 1

    show bg rave with vpunch

    call pachinko_create

    show text "{size=50}SMASH THE BUTTON AND WIN THE MONEY!{/size}" at truecenter with dissolve

    system "Are you a real pachinko baller? Let's go!"

    hide text

    show adorina smug
    with easeinright

    aa "I won't go easy on you just because you're cute desu! {b}SPECIAL MOVE: DESUMAKU DESU{/b}!" with vpunch

    hide adorina
    with easeoutright

    menu:

        ann_thoughts "I can't let her beat me! I need to gain the advantage!"

        "(Anime Yelling)":

            ann_thoughts "If I just show my winning spirit, I have to win!"

            show ann genki
            with easeinleft

            a "YAAAAAAAAAA!"

            $ energy -= 50

        "Chuunibyou Pose":

            ann_thoughts "If I just trick her into thinking I'm powerful, I have to win!"

            show ann genki
            with easeinleft

            a "Don't make me reveal the power of my magic arm!"

        "Zettai Ryouiki Zone":

            ann_thoughts "As long as I have the higher score, I have to win!"

            show ann genki
            with easeinleft

            a "I won't let you score {b}ANY{/b} points!"

        "Ball Bukkake":

            ann_thoughts "If I unleash all my balls at once, I have to win!"

            show ann genki
            with easeinleft

            a "Eat this!"

    hide ann
    with easeoutleft

    call pachinko_cleanup

    hide bg rave

    play music promenade_medium fadeout 1

    scene bg hallway fancy
    with vpunch

    show confetti

    show ann genki
    with easeinleft

    a "I won!"

    hide ann
    with easeoutleft

    show orion genki
    with easeinright

    o "Hey! I won too!"

    hide orion
    with easeoutright

    show adorina genki
    with easeinright

    if twenty_dollars == False:

        aa "I didn't think you'd beat me desu! Here's your badges desu."

    if twenty_dollars == True:

        aa "I didn't think you'd beat me desu! Here's your $20 and badges desu."

    hide adorina
    with easeoutright

    hide confetti
    with dissolve

    play music yo_p1 fadeout 1

    play sound window_break_right

    show adorina smug
    with easeinright

    aa "[fs] if you're just going to walk in after breaking through a window, please use the door desu. We have to pay for that desu."

    hide adorina
    with easeoutright

    show frog sensei happy
    with easeinright

    fs "Konnichiwa Ribbit. I heard some ribbit here wasn't happy with my new and improved Animarathon."

    hide frog sensei
    with easeoutright

    show ann disgust
    with easeinleft

    a "That's me! I want a normal Animarathon!"

    hide ann
    with easeoutleft

    show frog sensei
    with easeinright

    fs "That's not possible ribbit. The future of Ohio depends on this pachinko!"

    hide frog sensei
    with easeoutright

    show orion smug
    with easeinright

    o "Ohio's been fine without pachinko for centuries! Why are you really doing this?"

    hide orion
    with easeoutright

    queue music yo_p2

    show frog sensei kidnap
    with easeinright

    fs "I like your spunk genki tadpole! It's time for a one on one at my lillypad ribbit!"

    hide frog sensei
    with easeoutleft
    # The way he leaves should match the window breakage.

    show white
    with dissolve

    a "{i}ACK! SZA! HACK!{/i} Don't throw smoke grenades indoors!"
    # Acknowledge, Skip if accumulator is zero (False). Gibberish, but better then normal coughing noises

    play sound window_break_left

    fs "Sayonara ribbit!"

    a "Jam it! Get back here! You can't just kidnap people!"

    ann_thoughts "He's already outside with [o]. There's no way I can catch up now."

    scene bg hallway fancy
    with dissolve

    play music breathe fadeout 1

    hide white
    with dissolve

    ann_thoughts "The smoke dissipated thanks to all these broken windows. Time to take a breath."

    show adorina normal
    with easeinright

    aa "Our broken window fund is desu-pleted... We'll be in desu-bt..."

    hide adorina
    with easeoutright

    show ann normal
    with easeinleft

    a "What's going on? Who is [fs]?"

    hide ann
    with easeoutleft

    show adorina normal
    with easeinright

    aa "[fs] is the anime club president desu. He always kidnaps guests to train them as ninjas desu."

    hide adorina
    with easeoutright

    show ann happy
    with easeinleft

    a "So [o] isn't in any danger?"

    hide ann
    with easeoutleft

    show adorina normal
    with easeinright

    menu:

        aa "Desunately not, though I need to know if you're going to take back his hostage desu."

        "Yeah, I'm gonna get my brother back.":

            aa "Stop [fs] from breaking windows too and I'll help desu!"

            hide adorina
            with easeoutright

            show ann happy
            with easeinleft

            a "Why? Isn't [fs] your partner in crime?"

            hide ann
            with easeoutleft

            show adorina smug
            with easeinright

            aa "[fs] breaking windows is putting us into desu-bt! This is for his own good desu!"

            hide adorina
            with easeoutright

            show ann smug
            with easeinleft

            a "How could you help me?"

            hide ann
            with easeoutleft

            show adorina normal
            with easeinright

            aa "I'll make you a magical girl desu! I'd give you my yaoi paddle of justice desu! Desustroy anyone in your way and take their dollars desu!"

            hide adorina
            with easeoutright

            ann_thoughts "I thought they banned yaoi paddles? I guess it's morally gray if staff is giving me one."

            show ann smug
            with easeinleft

            a "So stop [fs] and steal people's money? That's your master plan?"

            hide ann
            with easeoutleft

            show adorina normal
            with easeinright

            aa "That's the keikaku desu! I only want 25\% of your magical girl earnings too!"
            # The \ is an escape symbol. It shouldn't render

            hide adorina
            with easeoutright

            menu:

                ann_thoughts "Should I accept her deal and become a magical girl?"

                "Become a magical girl.":

                    show adorina normal
                    with easeinright

                    aa "Sugoi desu! Take this paddle and stop [fs] desu!"

                    hide adorina
                    with easeoutright

                    $ magical_girl = True

                "No deal!":

                    show adorina smug
                    with easeinright

                    aa "What a shame desu. I have to keep this line moving desu."

                    hide adorina
                    with easeoutright

        "Nah, he can handle himself.":

            aa "I'd love to chat with you more, but registration doesn't run itself desu. Next desu!"

            hide adorina
            with easeoutright

        "Nah, I'm calling the cops.":

            aa "Suit yourself desu. Next desu!"

            hide adorina
            with easeoutright

            show ann happy
            with easeinleft

            a "Is there a police officer around here?"

            hide ann
            with easeoutleft

            show will normal
            with easeinright

            ww "Howdy miss, I'm the sharpshooting sheriff around here."

            hide will
            with easeoutright

            show ann smug
            with easeinleft

            a "Is there a {i}real{/i} police officer around here?"

            hide ann
            with easeoutleft

            show will normal
            with easeinright

            ww "Ma'am I may not be a real police officer, but by my spurs, my big iron is a tool of {b}JUSTICE{/b}!"

            hide will
            with easeoutright

            ann_thoughts "This guy is delusional. I don't wanna get someone shot."

            show ann normal
            with easeinleft

            a "Oh wow! Sorry sir! No problem here!"

            hide ann
            with easeoutleft

            show will normal
            with easeinright

            ww "If y'all say so. Happy trails!"

            hide will
            with easeoutright

    if magical_girl == False:

        ann_thoughts "Winning at pachinko back there was a fluke. I need to cheat to win."

    if magical_girl == True:

        ann_thoughts "This yaoi paddle could be useful, but I should have a contingency plan."

    show panda on at truecenter
    with easeinbottom

    ann_thoughts "I can force the probability of the pachinko machines in my favor with my PANDA and Grover's Algorithm!"
    # I'm pretty sure you can't use Grover's Algorithm this casually.

    hide panda
    with easeoutbottom

    scene yellow

    show fight
    with hpunch

    ann_thoughts "The gambling has really heated things up! I should scram!"

    jump bg_main_loop
