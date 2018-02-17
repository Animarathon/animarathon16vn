# Animarathon XVI: Operation Ohio Advanced Cosplay Panel
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
#     _       _                               _    ____                _               ____                  _ 
#    / \   __| |_   ____ _ _ __   ___ ___  __| |  / ___|___  ___ _ __ | | __ _ _   _  |  _ \ __ _ _ __   ___| |
#   / _ \ / _` \ \ / / _` | '_ \ / __/ _ \/ _` | | |   / _ \/ __| '_ \| |/ _` | | | | | |_) / _` | '_ \ / _ \ |
#  / ___ \ (_| |\ V / (_| | | | | (_|  __/ (_| | | |__| (_) \__ \ |_) | | (_| | |_| | |  __/ (_| | | | |  __/ |
# /_/   \_\__,_| \_/ \__,_|_| |_|\___\___|\__,_|  \____\___/|___/ .__/|_|\__,_|\__, | |_|   \__,_|_| |_|\___|_|
#                                                               |_|            |___/
#  ____                  _   ____  _
# |  _ \ __ _ _ __   ___| | |  _ \| | __ _ _ __  
# | |_) / _` | '_ \ / _ \ | | |_) | |/ _` | '_ \ 
# |  __/ (_| | | | |  __/ | |  __/| | (_| | | | |
# |_|   \__,_|_| |_|\___|_| |_|   |_|\__,_|_| |_|
#
# By the end of the panel the player should experience the following outcomes.
#
# ! Positive Outcome (Player doesn't nap.)
# 💭 Be exposed to the concept of integrating electronics into clothing.
# 💭 Be exposed to practical applications of wearable computing beyond the current consumer offerings.
# 💭 Learn that Japan alone is not responsible for cosplay, and that Ohio played a historical roll in cosplay.
# 💭 Demonstrate the concept of mutually assured destruction without explicitly referring to nuclear war.
# $ Gain a in game reward for learning.
# Ψ Feel that this learning was done of their own free will.
#
# ! Negative Outcomes (The player took a nap.)
# 💭 Experience some minor wordplay.
# $ Gain a in game reward to encourage better sleeping habits.
# Ψ Feel that this choice was made of their own free will.

label cosplay:

    scene bg cosplay lab
    with dissolve

    play music this_reminds_me_of_something_p0 fadeout 1

    show text "{size=70}Chapter 1: Cosplay Crisis!{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard='True')

    hide text
    with dissolve

    show crowd
    with easeinbottom

    jump cosplay_menu

label cosplay_menu:

    menu:

        ann_thoughts "Looks like the advanced cosplay panel is about to start. What should I do?"

        "Stay awake for the panel":

            call cosplay_awake

        "Consider the Panel":

            call cosplay_considerations

            jump cosplay_menu

        "Take a nap outside the panel":

            call cosplay_asleep

    stop music fadeout 1

    return

label cosplay_awake:

    show rei ya normal
    with easeinright

    ry "Welcome to the advanced cosplay panel! Starting with the basics, how many of you know what cosplay is?"

    hide rei ya
    with easeoutright

    show guest otaku
    with easeinright

    guest_otaku "{i}Sumimasen [ry]-san{/i}! Cosplay is like a watashi! Sugoi desu ne {i}ugu{/i}!"

    # Thank you so much honorable Rei Ya! Cosplay is like me (Refering to the garmets I am wearing)! It's super isn't it? ugu (Literally a meaningless sound made to sound cute.)

    hide guest
    with easeoutright

    show guest gamer
    with easeinright

    guest_gamer "C0spl4y d035n'7 1mpr0v3 DPS 4t 4ll my d00d! G17 g00d, GTF0 c0sm3t1k 5k1nz K? 1m40!"

    # Cosplay is purely ornimental. In the heat of combat you will do no more damage in cosplay then in normal clothing. Please learn what you are doing and remove pointless cosmetics ok? I'm laughing very hard.

    hide guest
    with easeoutright

    show guest funky
    with easeinright

    guest_funky "Cosplay is a funky outfit baby! You can't boogie on my dancefloor with that getup! Dig it?"

    hide guest
    with easeoutright

    show rei ya normal
    with easeinright

    ry "Sigh..."

    hide rei ya
    with easeoutright

    show guest otaku
    with easeinright

    guest_otaku "Watashi right! Watashi feeling it! Watashi oniisan! {i}yatta! suki! suki! ~nya~!{/i}"

    # I'm right! I'm feeling great about how correct I am! I'm like a big brother to you! I did it! I like it! I like it! Meow (The noise a cat makes)!
    
    hide guest
    with easeoutright

    show rei ya normal
    with easeinright

    ry "You're all wrong."

    hide rei ya
    with easeoutright

    show guest otaku
    with easeinright

    guest_otaku "Hontou? Itai! Gomenasai mahou [ry] chan!"

    # Really? It hurts as though I am in pain! Please forgive me Rei Ya you magical friend!
    
    hide guest
    with easeoutright

    queue music this_reminds_me_of_something_p1

    show rei ya normal
    with easeinright

    menu:

        ry "Who wants to win $5? I will pay $5 for a serious answer. Use your PDA if you must."

        "A cosplay is a kawaii":

            hide rei ya
            with easeoutright

            show ann genki
            with easeinleft

            a "It's gotta be a kawaii right? {i}Uguu{/i}! I'm so kawaii!"

            hide ann
            with easeoutleft

            show rei ya normal
            with easeinright

            ry "Sorry that's way off. Cute or not a cosplay is a costume. Why don't you pick our next topic [a]? It will be more adorable that way."

            hide rei ya
            with easeoutright

        "A cosplay is a kaiju":

            hide rei ya
            with easeoutright

            show ann genki
            with easeinleft

            a "It's gotta be a kaiju right? {b}Rawr{/b}! I'm a monster!"

            hide ann
            with easeoutleft

            show rei ya normal
            with easeinright

            ry "That's wrong. A cosplay is a costume although it can be of a kaiju. [a] is truly a monster, so she should pick our next topic."

            hide rei ya
            with easeoutright

        "A cosplay is a tentacle":

            hide rei ya
            with easeoutright

            show ann genki
            with easeinleft

            a "It's a tentacle for sure! Is it the kind with suction cups or one of the slippery ones?"

            hide ann
            with easeoutleft

            show rei ya normal
            with easeinright

            ry "Sorry that's way off. A cosplay is a costume - even with tentacles. Why don't you pick our next topic? It will be more interesting that way."

            hide rei ya
            with easeoutright

        "A cosplay is a costume":

            hide rei ya
            with easeoutright

            show ann happy
            with easeinleft

            a "Cosplay is just a costume right? Usually of a fictional character? People at an Anime convention should know this!"

            hide ann
            with easeoutleft

            show rei ya normal
            with easeinright

            ry "That's right. My question was rhetorical. Since the rest of the audience doesn't care, why don't you pick what we'll cover?"

            python:
                money += 5
                what_is_cosplay = True

            hide rei ya
            with easeoutright

    menu:

        ann_thoughts "I get to choose what we'll talk about next?"

        "3D Printing Cosplay":

            show rei ya normal
            with easeinright

            ry "3D Printers can be useful tools for cosplay makers. With hot extruder on plastic action, you can make useful trinkets and tools."

            hide rei ya
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "4YY d00d! 3D-P r c001! 1 u53 D0Z3 2 3D Pr1n7 phr3k3 c453 m0ds 4 fr33 @ d4 1337br4ry!"

            # Excuse me panelist! 3D Printers are fashionable. I use them to print modifications for my computer case that could be described as freaky. I do this for free using my library of elite status.

            hide guest
            with easeoutright

            show guest otaku
            with easeinright

            guest_otaku "Watashi don't like 3D-P... Oh! Gamer-Kun said 3D Printer! So sugoi!"

            # I do not like three dimensional Pigs... I'm sorry! Mr. Video Gamer was discussing 3D Printers. 3D Printers are super!

            hide guest
            with easeoutright
        
            show rei ya normal
            with easeinright

            ry "You can often use a 3D Printer at a public library. Some libraries also carry some other useful tools for cosplay."

            hide rei ya
            with easeoutright

            show guest otaku
            with easeinright

            guest_otaku "Watashi saw 3DP on my way to the manga section of the library... I mean literature dojo to study the my katana!"

            # I saw a 3D Printer on my way to the Japanese comic section of the library... I mean to say a area where martial artists can hone their literature skills so I can hone my Japanese swordsmanship.

            hide guest
            with easeoutright

            show rei ya normal
            with easeinright

            ry "Laser Cutters can cut some fabrics very cleanly, and automated embroidery machines can make it pop with nearly the same vector file."

            hide rei ya
            with easeoutright

            show rei ya silver
            with dissolve

            ry "Let's end this panel now, and show you how cleanly I can cut! This is a cosplay stick up! Pachinko Balls and Wallets in the bag!"

        "Electric Cosplay":

            show rei ya normal
            with easeinright
 
            menu:
 
                ry "Pick what you know right [a]? Time for a shock quiz! What kind of electricity is used in cosplay?"

                "AC":

                    ry "Are you thinking about EL wire or something? Outside that it's not really used much in cosplay."

                    hide rei ya
                    with easeoutright

                    show ann normal
                    with easeinleft
                    
                    a "Don't forget Tesla Coils! There are some man portable units that look sick in action! It's too bad they aren't always convention safe."

                    hide ann
                    with easeoutleft

                    show rei ya normal
                    with easeinright

                    ry "I know right? Did you know that one of Nikola Tesla's personal coils ended up in a Toledo school? It's a small world."

                "DC":

                    ry "Of course you would know that [a]. That's correct."

                    hide rei ya
                    with easeoutright

                    show ann normal
                    with easeinleft
                    
                    a "I think most people here would know that. Edison himself grew up nearby in the Firelands."

                    hide ann
                    with easeoutleft

                    show rei ya normal
                    with easeinright

                    ry "I know right? Did you know that BG has a large DC solar plant? It has to be converted to AC for the grid of course."

                "AC & DC":

                    ry "That's right! DC is the most used current in cosplay, but AC is also used for things like EL wire!"

            hide rei ya
            with easeoutright

            show rei ya normal
            with easeinright

            menu:

                ry "Let's move on to power sources. Most electric cosplays use a battery for power. Does anyone know how power is delivered to cosplay components?"

                "Silver and Steel Thread":
 
                    ry "That's right. Silver and Steel threads are common choices for electrified cosplays."

                "Hemp and Flax Twine":

                    ry "What in the blazes made you say that? Most cosplayers use silver and steel threads for their flexibility."

                "Copper and Gold Wire":

                    ry "Good guess. It's normally not used, but is thematically appropriate in Cyberpunk cosplay."

                "Stay Quiet":

                    ry "Nobody knows? Most cosplayers use silver and steel threads."

            hide rei ya
            with easeoutright

            show guest otaku
            with easeinright

            guest_otaku "Watashi want to know what powers this can give you!"

            # I want to know what abilities this technique can grant one.

            hide guest
            with easeoutright

            show rei ya normal
            with easeinright

            ry "You can make your cosplay a lot more expressive with electricity. Lights, Motors, Screens, and even heat for comfort."

            hide rei ya
            with easeoutright

            show guest cyber
            with easeinright

            guest_cyber "This is all proof that [ry] is a {b}Fraudster{/b} right here folks! If cosplay had electricity, it would {b}electrocute people{/b}!"

            hide guest
            with easeoutright

            show rei ya normal
            with easeinright

            ry "{i}Heh{/i} I won't deny that's a possibility. If you take the right safety precautions there's not a chance."

            hide rei ya
            with easeoutright

            show guest cyber
            with easeinright

            guest_cyber "Ha I knew it! I'll ride the shockwaves of the net with the story of the century!{nw}"

            hide guest
            with easeoutright

            show rei ya normal
            with easeinright

            ry "{b}For you{/b} it's possible. Electrical cosplay could hurt someone, especially if it was designed specifically to hurt people."

            hide rei ya
            with easeoutright

            show guest cyber
            with easeinright

            guest_cyber "Is that a threat?"

            hide guest
            with easeoutright

            show rei ya silver
            with dissolve

            ry "Sure is buddy! This panel is a stick up! Pachinko Balls and Wallets in the bag!"

        "Show off your cosplay skills already":

            show rei ya silver
            with easeinright

            ry "{b}For you{/b}? Certainly. Let's end this panel now, and begin the cosplay stick up! Pachinko Balls and Wallets in the bag!"

    hide rei ya
    with dissolve

    queue music yo_p2

    show guest furry
    with easeinright

    guest_furry "Thanks [ry]! You've inspired me to make a better fursuit! Wan!"

    hide guest
    with easeoutright

    show rei ya silver
    with dissolve
    
    ry "Thanks! Always hurts to let a fan down by stealing from them."

    hide rei ya
    with dissolve

    show guest cyber
    with easeinright

    guest_cyber "I always knew you were a fraud [ry]! You stole from your fans with fake videos so of course you would steal money too!"

    hide guest
    with easeoutright

    show rei ya silver
    with dissolve
    
    ry "I admit to everything. Let the police know so my victims can file extra charges when they catch me."

    hide rei ya
    with dissolve

    show guest otaku
    with easeinright

    guest_otaku "Senpai noticed me! Take my yens senpai! So sugoi desu ne!"

    # My superior has given me attention! I wish for my superior to have my money! It's so amazing, isn't it?

    hide guest
    with easeoutright

    show rei ya silver
    with dissolve
    
    menu:
    
        ry "It's your turn now sister. Pachinko balls and money in the bag and nobody gets hurt."

        "Your dress would look better with black eyes.":

            ry "I'd like to see you try! Balls and money in the bag, or you're dead."

        "Actually I'll be robbing you.":

            ry "Nice Try! I spent all my money on cosplay! Balls and money in the bag, or you're dead."

        "Ok, but I'll need a [favorite_anime] cosplay in return.":

            ry "I hate [favorite_anime] almost as much as I hate you [a]! Balls and money in the bag, or you're dead."

        "Has the cosplay competition already started? I don't recognize your character!":

            ry "Wisegal! I must not have made myself clear, balls and money in the bag, or you're dead."

    hide rei ya
    with dissolve

    show ann smug
    with easeinleft

    a "You and what army? I was captain of the kickboxing team in High School! I could crack your skull open under my heel in 10 seconds flat!"

    hide ann
    with easeoutleft

    show rei ya silver
    with dissolve

    ry "Oh my! I didn't show off my threat! As you nitwits were arguing about what cosplay is, I sewed threads from my supercapacitors to your shirts!"

    hide rei ya
    with dissolve

    show ann disgust
    with easeinleft

    a "Are you insane?! Regular capacitors are already easily lethal! A weaponized supercapacitor is lethal for sure!"

    hide ann
    with easeoutleft

    show rei ya silver
    with dissolve

    ry "You're not as stupid as you look [a]! I've got hundreds of volts to play with so you better be a-farad!"

    hide rei ya
    with dissolve

    menu:

        ann_thoughts "There's got to be a way out! What should I do?"

        "Suck my gut in":

            $ cleverness += 1

            show ann smug
            with easeinleft

            a "Shock off [ry]!"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "Good choice [a]. I've been waiting for this!"

            hide rei ya
            with dissolve

            show ann smug
            with easeinleft

            a "I'm waiting."

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "You should be extra crispy by about now..."

            hide rei ya
            with dissolve

            show ann smug
            with easeinleft

            a "What's the matter [ry], or should I say {b}Rei Yamato{/b}? I remember you from the Cleveland Fashion Hackathon last year! Make another defective invention?"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "I hate you [a]! You can never give me a break about my setbacks! I may as well go to jail now. At least I won't see your face there."

            hide rei ya
            with dissolve

        "Leap back":

            $ cleverness += 1

            show rei ya silver
            with dissolve

            ry "What are you doing?! I almost tripped! Don't do that again [a]! You're my hostage!" with vpunch

            hide rei ya
            with dissolve

            show ann smug
            with easeinleft

            a "Don't do this?"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "Ouf! My hip bone! Owie!"

            hide rei ya
            with dissolve

            show ann smug
            with easeinleft

            a "That your supercap pack on the floor? I'd recognize that craftsmanship anywhere. You're Rei Yamato from last year's Cleveland Fashion Hackathon aren't you?"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "{b}I hate you [a]{/b}! Your bone conducting necklace phone was {b}dumb{/b}! My quick plastic surgery kit deserved first place!"

            hide rei ya
            with dissolve

            show ann smug
            with easeinleft

            a "Glitch please! Your kit was so defective it got you disqualified! Besides if my necklace phone is so dumb then why are you wearing an imitation?"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "{b}Fine [a]{/b}! You clearly want to ruin my life, so I give up. The police can have [ann_ry]. You win again."

            hide rei ya
            with dissolve

        "Negotiate":

            $ negotiation += 1

            show ann smug
            with easeinleft

            a "Hey I remember you! Your real name is Rei Yamato! We competed in the Cleveland Fashion Hackathon last year! You've got some skills!"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "Do skills even matter? My quick plastic surgery kit deserved first place, but it got disqualified because of the incident!"

            hide rei ya
            with dissolve

            show ann smug
            with easeinleft

            a "Bull! We all make mistakes! You need to keep honing your skills and atone for your setbacks!"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "I wouldn't call manslaughter a setback, but you're right [a]. At this point [ann_ry] is going to prison no matter what, but I will atone one day."

            hide rei ya
            with dissolve

        "Berate":

            $ intimidation += 1

            show ann smug
            with easeinleft

            a "Hey I remember you now! Your real name is Rei Yamato! I beat you in the Cleveland fashion hackathon last year! You're such a {b}dork{/b} [ry]!"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "{b}I hate you [a]{/b}! Your bone conducting necklace phone was {b}dumb{/b}! My quick plastic surgery kit deserved first place!"

            hide rei ya
            with dissolve

            show ann smug
            with easeinleft

            a "Bull! The judges were right to disqualify you after what you did to your partner! I bet you never even apologized after the fact!"

            hide ann
            with easeoutleft

            show rei ya silver
            with dissolve

            ry "I could never face her family after that! {b}Fine [a]{/b}! You clearly want to ruin my life, so I give up. The police can have [ann_ry]. You win again."

            hide rei ya
            with dissolve

    queue music this_reminds_me_of_something_p4

    show rei ya silver
    with dissolve

    ry "Please allow me to cut my threads off..."

    hide rei ya
    with dissolve

    show black

    ry "Whoops! Accidentally shorted the lights! One moment please!"

    a "Hey! Don't try anything now!"

    ry "Don't worry. I'll hold onto you so you know I'm not bolting for the door."

    a "Ouch! Holy Toledo that's my face!"
    
    ry "Is this better?"

    a "Hey hey hey! You don't need to tug on my shirt! I get that you aren't leaving!"

    hide black

    show rei ya ann smug
    with easeinright

    ry_ann "Behold cosplayers! I have brought the vile [ann_ry] to {b}justice{/b}! I am [ry_ann], {b}the most ethical cosplayer in the galaxy{/b}!"

    hide rei ya
    with easeoutright

    show ann rei ya normal
    with easeinleft

    ann_ry "Nya?"

    hide ann
    with easeoutleft

    show guest cosplay cop
    with easeinright

    guest_cosplay_cop "I'm the {b}[guest_cosplay_cop]{/b}! I got a tip about some {b}Cosplay Crime{/b} going on here! I need to apprehend the {b}cosplay criminal{/b}!"

    hide guest
    with easeoutright

    show rei ya ann smug
    with easeinright

    ry_ann "[ann_ry] did it! She's a {b}cosplay criminal{/b}, who uses her {b}cosplay cantrips{/b} to {b}conlift citizens{/b}!"

    hide rei ya
    with easeoutright

    show guest cosplay cop
    with easeinright

    guest_cosplay_cop "{b}Cosplay conlifting{/b} is one of the most serious {b}cosplay crimes{/b}! Stop in the name of Senpai and everything will be diajoubou in {b}Cosplay Court{/b}!"

    hide guest
    with easeoutright

    show ann rei ya normal
    with easeinleft

    ann_ry "That dastard is just pretending to be me! Her acting is terrible too!"

    hide ann
    with easeoutleft

    show rei ya ann smug
    with easeinright

    ry_ann "Have you ever looked in a mirror? You're clearly the ugly hag {b}[ann_ry]{/b}! I'm [ry_ann], the real deal! Don't accept substitutes!"

    hide rei ya
    with easeoutright

    show guest cosplay cop
    with easeinright

    guest_cosplay_cop "Listen, I only have one set of {b}cosplay cuffs{/b}, so figure it out or I'll bust a {b}Cosplay Cap{/b} in both of you. Defendant you're up."

    hide guest
    with easeoutright

    menu:

        ann_thoughts "What should I do?"

        "Establish Mens Rea":

            show ann rei ya normal
            with easeinleft

            ann_ry "Think about it your honor! What motivation would [ry] have to stick around after a cosplay crime?"

            hide ann
            with easeoutleft

            show guest cosplay cop
            with easeinright

            guest_cosplay_cop "How do you mean defendant? You were in the process of {b}Cosplay Conlifting{/b} weren't you?"

            hide guest
            with easeoutright

            show rei ya ann smug
            with easeinright

            ry_ann "[ry] was probably gonna stick around for some murder! Her real name is Rei Yamato! Not only is she a {b}cosplay conlifter{/b}, she's a {b}cosplay killer{/b}!"

            hide rei ya
            with easeoutright

            show guest cosplay cop
            with easeinright

            guest_cosplay_cop "I should have known! Rei Yamato {b}cosplay slayed{/b} her partner last year at the Cleveland Fashion Hackathon while testing her quick plastic surgery kit."

            hide guest
            with easeoutright

            show rei ya ann smug
            with easeinright

            ry_ann "Her Mens Rea is to tie up loose ends! I beat her at the Hackathon, and I know about how she killed her own partner! {b}It wasn't an accident{/b}!"

            hide rei ya
            with easeoutright

            show guest cosplay cop
            with easeinright

            guest_cosplay_cop "I have to say defendant, I've never seen someone lose a trial so quickly. You're going to the maximum fashion {b}Cosplay Clink{/b} for a long time!"

            hide guest
            with easeoutright

            show ann rei ya normal
            with easeinleft

            ann_ry "You're right that it wasn't an accident. However [ry] didn't kill anyone because [a] was that corpse, and she didn't even know it!"

        "Call Witnesses To Stand":

            show ann rei ya normal
            with easeinleft

            ann_ry "Your honor, I'd like to call some witnesses to the stand!"

            hide ann
            with easeoutleft

            show guest cosplay cop
            with easeinright

            guest_cosplay_cop "Eh, why not? You in the bodysuit, get up here!"

            hide guest
            with easeoutright

            show guest cyber
            with easeinright

            guest_cyber "She's a fraud but If you lock her up I'll have to find someone else to harass online! Please let her go!"

            hide guest
            with easeoutright

            show guest otaku
            with easeinright

            guest_otaku "You bring dishonor to senpai's name! [ry] is my omae and her moe posts make me doki doki every night. Daisuki rabu [ry] sama!"

            # Do not remove the honor the name of my superior! Rei Ya is my friend, and her cute online articles make my heart beat every night. I love, love, the honorable Rei Ya!

            hide guest
            with easeoutright

            show guest furry
            with easeinright

            guest_furry "[ry] ain't so bad! She inspired me to make my fursuit better! Wan! Wan! Wan! Give her a treat but don't put her in a cage!"

            hide guest
            with easeoutright

            show rei ya ann smug
            with easeinright

            ry_ann "As if you know the real [ry]! Her real name is Rei Yamato! Not only is she a {b}cosplay conlifter{/b}, she's a {b}cosplay killer{/b}!"

            hide rei ya
            with easeoutright

            show guest cosplay cop
            with easeinright

            guest_cosplay_cop "I should have known! Rei Yamato {b}cosplay slayed{/b} her partner last year at the Cleveland Fashion Hackathon testing her defective quick plastic surgery kit."

            hide guest
            with easeoutright

            show ann rei ya normal
            with easeinleft

            ann_ry "Actually [ry] didn't kill anyone. [a] was that corpse!"

        "Object":

            show ann rei ya normal
            with easeinleft

            ann_ry "I object! [ry] is in truth Rei Yamato! I'm the real [a]!"

            hide ann
            with easeoutleft

            show guest cosplay cop
            with easeinright

            guest_cosplay_cop "How do you mean defendant? You are clearly [ry]. You are aware that Rei Yamato is guilty of {b}Cosplay Killing{/b}?"

            hide guest
            with easeoutright

            show ann rei ya normal
            with easeinleft

            ann_ry "Actually [ry] didn't kill anyone. [a] was that corpse!"

        "Update Autopsy Report":

            show ann rei ya normal
            with easeinleft

            ann_ry "Do you remember the {b}Cleveland Fashion Hackathon Incident{/b} a year ago? I need to update the autopsy report from that."

            hide ann
            with easeoutleft

            show guest cosplay cop
            with easeinright

            guest_cosplay_cop "How do you mean defendant? I caught the perp, Rei Yamato, after she accidentally killed her partner testing her quick plastic surgery kit."

            hide guest
            with easeoutright

            show rei ya ann smug
            with easeinright

            ry_ann "Nice try {b}Gray Blah{/b}. I was there when it happened too, because I won that hackathon with my charisma and wit. It doesn't matter though!"

            hide rei ya
            with easeoutright

            show ann rei ya normal
            with easeinleft

            ann_ry "It's important because [a] was that corpse and [ry] is really Rei Yamato!"

    hide ann
    with easeoutleft

    queue music this_reminds_me_of_something_p3

    show rei ya ann smug
    with easeinright

    ry_ann "Heh, you really are crazy! That assistant is dead as a doorknob! She went to the morgue and everything!"

    hide rei ya
    with easeoutright

    show ann rei ya normal
    with easeinleft

    ann_ry "Yeah right! We all got wasted at the club after the intro ceremony but your assistant got caught using a fake id. She could have done better then {b}Notmi Kegger{/b}."

    hide ann
    with easeoutleft

    show rei ya ann smug
    with easeinright

    ry_ann "I think you mean {b}your{/b} assistant got caught! I am the ethical hero [ry_ann] who would never fabricate a fake ID for a friend!"

    hide rei ya
    with easeoutright

    show ann rei ya normal
    with easeinleft

    ann_ry "Bull! When {b}Notmi Kegger{/b} was caught, [ry] came up with a drunk plan to cover it up to save face. I drunkenly accepted."

    hide ann
    with easeoutleft

    show rei ya ann smug
    with easeinright

    ry_ann "That sounds like something drunk [ry] would do... Not that {b}I{/b} would know too much about that! Her dead assistant got sent to the morgue though!"

    hide rei ya
    with easeoutright

    show guest cosplay cop
    with easeinright

    guest_cosplay_cop "Dead people are sent to the morgue! I took the corpse to Reliable Ryan's Organ {size=16}Chop{/size}{size=12} Shop{/size}... I mean {b}morgue{/b} myself!"

    hide guest
    with easeoutright

    show ann rei ya normal
    with easeinleft

    ann_ry "I stumbled out of that morgue with a huge hangover and gave the mortician a heart attack. Your assistant is still in juvie but you didn't kill her."

    hide ann
    with easeoutleft

    show guest cosplay cop
    with easeinright

    guest_cosplay_cop "{size=8}That explains the no zombies rule they made at the organ chop shop...{/size}"

    hide guest
    with easeoutright

    show rei ya ann smug
    with easeinright

    ry_ann "If I didn't kill my assistant after all... I'm coming clean! I'm really [ry]! I committed cosplay identity theft on [a] using my quick plastic surgery kits!"

    hide rei ya
    with easeoutright

    queue music this_reminds_me_of_something_p1

    show black

    ry "For our decency I'm cutting the lights while I undo this."

    a "Holy Toledo! That's my leg!"

    hide crowd
    hide black

    show rei ya normal
    with easeinright

    ry "So what's my sentence? You wouldn't deny the world my genius for too long right?"

    hide rei ya
    with easeoutright    

    show guest cosplay cop
    with easeinright

    guest_cosplay_cop "I hope you can wear a {b}convict cosplay{/b} because that's the only kind allowed in the {b}Cosplay Clink{/b}! You'll be there for a whole hour!"

    hide guest
    with easeoutright

    show rei ya normal
    with easeinright

    ry "So long [a]. I'll be back to collect! Don't forget to sell those pachinko balls! They're worth more then the cash I stole!"

    hide rei ya
    with easeoutright

    show ann normal
    with easeinleft

    a "Hey! Don't hoist your stolen goods on me! Huh... All the guests left... Guess I'll hold onto this for now."

    hide ann
    with easeoutleft

    python:
        money += 100
        pachinko_balls += 30000

    return
            
#     _        _
#    / \   ___| | ___  ___ _ __  
#   / _ \ / __| |/ _ \/ _ \ '_ \ 
#  / ___ \\__ \ |  __/  __/ |_) |
# /_/   \_\___/_|\___|\___| .__/ 
#                         |_|
label cosplay_asleep:

    play music this_reminds_me_of_something_p4 fadeout 1

    show black
    with irisin

    a "Sleep is good. mmmm..."

    show orange
    with dissolve

    hide black
    with dissolve

    ann_thoughts "Why is everyone here dressed so tacky..."

    show blue
    with dissolve

    hide orange
    with dissolve

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "It's 2018... Get with it..."

    $ energy += 10

    hide crowd

    hide blue
    with irisout

    ann_thoughts "Oh my. Looks like everyone's gone now."

    return
#   ____                _     _                _   _                 
#  / ___|___  _ __  ___(_) __| | ___ _ __ __ _| |_(_) ___  _ __  ___ 
# | |   / _ \| '_ \/ __| |/ _` |/ _ \ '__/ _` | __| |/ _ \| '_ \/ __|
# | |__| (_) | | | \__ \ | (_| |  __/ | | (_| | |_| | (_) | | | \__ \
#  \____\___/|_| |_|___/_|\__,_|\___|_|  \__,_|\__|_|\___/|_| |_|___/

label cosplay_considerations:

    menu:
    
        ann_thoughts "Was there anything I wanted to consider before the panel starts?"

        "Who is the panelist?":

            ann_thoughts "[ry] started cosplaying a year ago. Amazingly she is already considered one of the top ten cosplayers globally."

            ann_thoughts "For some reason, I get Deja Vu whenever I see pictures of her, although I'm pretty sure we've never met."

            ann_thoughts "[ry] is well known online for her videos where she changes into totally different characters within seconds on camera."

            ann_thoughts "Her fans say she's just that skilled. Some say she cosplays all the time, and her identity as [ry] is just a cosplay."

            ann_thoughts "Her skeptics say her videos are fake, although extensive examination of her footage has revealed no obvious doctoring."

            ann_thoughts "The flame wars between her fans and skeptics are pretty epic. I wonder what she'll have to say?"

        "What is cosplay?":

            ann_thoughts "Cosplay is wearing a costume of a fictional character, kind of like Halloween."

            ann_thoughts "At Anime conventions, many people cosplay as their favorite characters."

            ann_thoughts "Cosplay is well known for being Japanese, but I think it started outside of Japan."

        "That's all":

            return

    jump cosplay_considerations
