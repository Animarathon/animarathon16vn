# Animarathon XVI: Operation Ohio Noodle Panel
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
#  _   _                 _ _        ____                  _ 
# | \ | | ___   ___   __| | | ___  |  _ \ __ _ _ __   ___| |
# |  \| |/ _ \ / _ \ / _` | |/ _ \ | |_) / _` | '_ \ / _ \ |
# | |\  | (_) | (_) | (_| | |  __/ |  __/ (_| | | | |  __/ |
# |_| \_|\___/ \___/ \__,_|_|\___| |_|   \__,_|_| |_|\___|_|
#  ____                  _   ____  _
# |  _ \ __ _ _ __   ___| | |  _ \| | __ _ _ __  
# | |_) / _` | '_ \ / _ \ | | |_) | |/ _` | '_ \ 
# |  __/ (_| | | | |  __/ | |  __/| | (_| | | | |
# |_|   \__,_|_| |_|\___|_| |_|   |_|\__,_|_| |_|
#
# Playtesters complained that there was not enough swearing and mature content.
# I don't like to swear needlessly to preserve impact for when I want to swear.
# So you can take this panel as innocent or as filled with innuendos.
#
# By the end of the panel the player should experience the following outcomes.
#
# ! Positive Outcome (Player doesn't nap.)
# 💭 Learn about how Ohio is a leader in food innovation.
# 💭 Be exposed to history trivia.
# 💭 Be exposed to global cultures through descriptions of delicious food.
# $ Gain a in game reward for learning.
# Ψ Feel that this learning was done of their own free will.
#
# ! Negative Outcomes (The player took a nap.)
# 💭 Experience some minor wordplay.
# $ Gain a in game reward to encourage better sleeping habits.
# Ψ Feel that this choice was made of their own free will. 

label noodles:

    scene tea room
    with dissolve

    play music water fadeout 1

    show text "{size=70}Chapter 2: Nefarious Noodles!{/size}" at truecenter
    with dissolve

    $ renpy.pause(3.0, hard='True')
    
    hide text
    with dissolve

    show crowd
    with easeinbottom

    jump noodles_menu

label noodles_menu:

    menu:

        ann_thoughts "Looks like the noodle panel is about to start. What should I do?"

        "Stay awake for the panel":

            call noodles_awake

        "Consider the Panel":

            call noodles_considerations

            jump noodles_menu

        "Take a nap outside the panel":

            call noodles_asleep

    stop music fadeout 1

    return

label noodles_awake:

    ann_thoughts "Looks like I'm a bit early."

    show guest furry
    with easeinright

    menu:

        guest_furry "Pssst-a! Over here!"

        "Approach the furry":

            play music yo_p0 fadeout 1

            hide guest
            with easeoutright

            show ann normal
            with easeinleft

            a "What's up furry dude?"

            hide ann
            with easeoutleft

            show guest furry
            with easeinright

            guest_furry "I'm an undercover chef. Can you help me meet [pt] alone? I just need to conduct some business."

            hide guest
            with easeoutright

            show ann normal
            with easeinleft

            a "You wanna interview her? Why are you asking me Mr...?"

            hide ann
            with easeoutleft

            show guest furry
            with easeinright

            mrcustard "Call me Mr. Custard. Your hair is the same diameter as Angel Hair pasta. [pt] {b}really{/b} likes that, so she'll fall for you."

            hide guest
            with easeoutright

            menu:

                ann_thoughts "Mr. Custard? What a baloney name."

                "Use an online handle":

                    show ann normal
                    with easeinleft

                    a "I'm [online_handle]. What do you want, and what's in it for me if I accept?"

                "Make up a stupid alias":

                    show ann normal
                    with easeinleft

                    a "I'm Impa Stah. What do you want, and what's in it for me if I accept?"

                "Make up a stupider name":

                    show ann normal
                    with easeinleft

                    a "I'm [a] Computer. What do you want, and what's in it for me if I accept?"

                "Use real name":

                    show ann normal
                    with easeinleft

                    a "I'm [a]. What do you want, and what's in it for me if I accept?"

            hide ann
            with easeoutleft

            show guest furry
            with easeinright

            mrcustard "Take [pt] to room 101, and I'll interview her there. Payment is $250 in cash upfront and $1000 in an online escrow account."

            hide guest
            with easeoutright

            menu:
    
                ann_thoughts "Should I extract the panelist for $1250? "

                "Accept the job":

                    show ann happy
                    with easeinleft

                    a "That payment is pretty Gouda. I'll do it."

                    hide ann
                    with easeoutleft

                    python:
                        money += 250
                        custard_job_accept = True

                    show guest furry
                    with easeinright

                    mrcustard "Excellent. I'll see you both in room 101."

                    hide guest
                    with easeoutright

                "Reject the job":

                    show ann disgust
                    with easeinleft

                    a "This is fishier then budget sushi. I'm out."

                    hide ann
                    with easeoutleft

                    show guest furry
                    with easeinright

                    mrcustard "No use crying over spilled milk. Thank you for your time miss."

                    hide guest
                    with easeoutright

                    play music water fadeout 1

        "Ignore the furry.":

            hide guest
            with easeoutright

            ann_thoughts "I'm here for ramen, not raccoons."

    show crowd
    with easeinbottom

    show paz ta
    with easeinright

    pt "It's the noodle panel my noodles! Please grab the sample tray under your seat and let's get started!"

    hide paz ta
    with easeoutright

    ann_thoughts "Free noodles! Woo!"

    show guest fairy
    with easeinright

    guest_fairy "Aye my lady ye slay me! Though it ain't against the rules of nature; it be against the con rules to serve food as a panelist."

    hide guest
    with easeoutright

    ann_thoughts "It's true. Food that doesn't go through proper channels is prohibited here because it's a potential biohazard."

    show paz ta
    with easeinright

    pt "Don't be Fettuccine Afraid-O! Anyone who rats us out will be eating through the mouth."

    hide paz ta
    with easeoutright

    ann_thoughts "[pt] is looking at me all of a sudden! Are those kitchen eyes?"

    show paz ta
    with easeinright

    pt "Hey angel hair! What's your favorite noodle?"

    hide paz ta
    with easeoutright

    show ann normal
    with easeinleft

    menu:

        ann_thoughts "Is she asking for a topic recommendation?"

        "European Pastas":

            hide ann
            with easeoutleft

            show paz ta
            with easeinright

            pt "Mia Angel Hair! What I wouldn't do to see you in a Corzetti! You are truly a woman of culture!"

            hide paz ta
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "d00d W3 g0nn4 74lk 4b0ut 5p4gh3tT1 0R Wu7?"

            # Excuse me! Are we going to talk about spaghetti? If not what are we going to be discussing tonight?

            hide guest
            with easeoutright

            show paz ta
            with easeinright

            pt "Hmpf. Gnocchi off you tiny pillus. I was getting to that."

            hide paz ta
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "4yy 1m40 d00d k33p c001 1t'5 ju57 4 d34d m33m br0."

            # Well said! I'm laughing so strongly it feels like my butt may fall off. Please do not take my earlier remark seriously, I simply could not resist using an old fashioned meme (Infections expression).

            hide guest
            with easeoutright

        "Ohio Chilis":

            hide ann
            with easeoutleft

            show paz ta
            with easeinright

            pt "Oh Angel Hair! You really goetta me!"
            # Goetta - A signature meat of the Cincinnati area.

            hide paz ta
            with easeoutright

            show guest otaku
            with easeinright

            guest_otaku "{b}Ohayo not Ohio!{/b} Onegaishimasu talk about superior Nippon noodles!"
            # Hello in Japanese, not Ohio USA! Please talk about Japanese noodles, which are superior!

            hide guest
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "Y0 4n1m3 n3rd? 1 h4ngry 4 ch1l1. 1nt3rup7 d4 p4n31 m04r 4nd 1 b4n U! P10x!"

            # I would like to get the attention of the anime enthusiast. I am hungry for chili and it has caused me anger. If you interrupt the panel any more I will remove you from the area. Please stop. 

            hide guest
            with easeoutright

            show paz ta
            with easeinright

            pt "As I was saying... Cincinnati Chili is served over spaghetti! What a bold choice!"

            hide paz ta
            with easeoutright

        "Asian Noodles":

            hide ann
            with easeoutleft

            show paz ta
            with easeinright

            pt "Angel Hair! Kesme now! You have excellent taste!"
            # Kesme - A hearty noodle dish from central Asia.

            hide paz ta
            with easeoutright

            show guest otaku
            with easeinright

            guest_otaku "{b}BAKA!{/b} Kesme is not a Nippon noodle!"
            # Idiot! Kesme is not a noodle of Japanese Origin!

            hide guest
            with easeoutright

            show paz ta
            with easeinright

            pt "I was getting to that you phogetable man! You probably know about Ramen, but Udon know what you're missing out on without Soba!"
            # Pho - A popular Vietnamese noodle.
            # Ramen - A popular Japanese wheat noodle served in broth and topped.
            # Udon - A thick Japanese noodle.
            # Soba - Thin Japanese buckwheat noodles.

            hide paz ta
            with easeoutright

            show guest otaku
            with easeinright

            guest_otaku "I've seen those in my Japanese animes like [favorite_anime]! Ramen... {b}Rabu{/b}!"

            hide guest
            with easeoutright

            show paz ta
            with easeinright

            pt "You sound like you don't know your own noodle from an eggroll. I can see why a yak lover like you lusts for hot boned broth with proked noodles though."
            # Eggroll - Chinese-American deep fried appetizer with filling.
            # lust for hot boned broth with proked noodles - want ramen noodles.

            hide paz ta
            with easeoutright

            show guest otaku
            with easeinright

            guest_otaku "Yak? Japan does not have unkawaii animals like yaks. Does senpai mean baka Chinese noodles?"

            # What do you mean by the word Yak? Japan does not have uncute animals like yaks. Does the panelist mean stupid Chinese noodles?

            hide guest
            with easeoutright

            show paz ta
            with easeinright

            pt "Hey! Don't diss Chinese noodles! My 11th removed Granddad Marco Polo stole the secret of their extra thick BiangBiang noodles!."
            # BiangBiang Noodles - Chinese noodles from the ancient province of Shaanxi 
            # I just made the secret up for Paz Ta's character. I don't believe there is any evidence to suggest that this is true.

            hide paz ta
            with easeoutright

            show guest gamer
            with easeinright

            guest_gamer "Y0 0p wu7 d0 k0r34nz 347 wh3n 7h3y pwn n00bz 1n g4m3z s1771n 1n d0z3 g4ng4m pc c4f3z?"

            # Listen up Original Poster (Referring to the panelist, Paz Ta), what do Koreans eat when they beat new players in games while sitting in those Gangam District PC cafes?

            hide guest
            with easeoutright

            show paz ta
            with easeinright

            pt "Koreans bust a load of flavor with dotoriguksu nut noodles from Gangdong! The D in Dotoriguksu stands for delicious in Korean!"

            hide paz ta
            with easeoutright

            ann_thoughts "I'm pretty sure that's not true, but I don't know enough Korean to dispute that."

        "Toledo Hot Dogs":

            hide ann
            with easeoutleft

            show paz ta
            with easeinright

            menu:

                pt "Mamma Mia Angel Hair! You don't think a hot dog is THAT do you?"

                "A hot dog is not THAT. It is a hot dog":

                    pt "Then we are in agreement Angel Hair. Sometimes a hot dog is just a hot dog."

                "A hot dog is not THAT. It is a sandwich":

                    pt "We are much alike Angel Hair. A hot dog is nothing more then meat between a bun."

                "A hot dog is not THAT. It is a sausage":

                    pt "Then we are in agreement Angel Hair. A hot dog is nothing more then a hunk of meat."

                "A hot dog is THAT":

                    pt "Holy Toledo Angel Hair! So you think a hot dog is a fat noodle..."

            hide paz ta
            with easeoutright

    ann_thoughts "[pt] pulls some spaghetti from under her apron and attempts to arrange it into a heart."

    ann_thoughts "It just falls on the ground."

    # FIXME: I'm not sure if I can pull this off with artwork. If I can it would be better to do it that way.

    ann_thoughts "Everyone is looking at me, and this is very uncomfortable."

    show paz ta
    with easeinright

    menu:

        pt "Have my noodles impressed you Angel Hair? Will you caprese be mine?"

        "No.":

            pt "Mama Mia!"

            hide paz ta
            with easeoutright

        "Forhgettaboutit.":

            pt "Mama Mia! I derailed my panel for you {b}wet noodle{/b}!"

            hide paz ta
            with easeoutright

        "Let's meet one on one in room 101." if custard_job_accept:

            play music yo_p1 fadeout 1

            $ negotiation += 1

            pt "Mama Mia! Rigatoni Ron has the best romance tips!"

            hide paz ta
            with easeoutright

            scene panel room dark
            with dissolve

            show guest furry
            with easeinright

            mrcustard "Thanks for playing along [a]."

            hide guest
            with easeoutright

            queue music yo_p2

            show ann smug
            with easeinleft

            a "Accept no impastas. Now about that escrow account."

            hide ann
            with easeoutleft

            show paz ta
            with easeinright

            pt "Mama Mia! I forgot to pay Rigatoni Ron! The escrow account at 127.0.0.1 can be unlocked with the password {b}long_pork_meatball_sushi{/b}"

            # There's no place like home.
            # Use ipv4. The ipv6 version of ::1 won't trick non techs.

            hide paz ta
            with easeoutright

            show ann disgust
            with easeinleft

            a "You knew?! What's going on?"

            hide ann
            with easeoutleft

            show guest furry
            with easeinright

            mrcustard "My real name isn't [mrcustard]. I'm [pt]'s manager and we're all out of her secret ingredient. You should be honored to be the centerpiece of her new dish."

            hide guest
            with easeoutright

            menu:

                ann_thoughts "What's going on?!"

                "You need me for Nyotaimori!":

                    show paz ta
                    with easeinright

                    pt "Figa! You figured it out! We were gonna open a Japanese Italian restaurant in Youngstown and we need a model. Are you in?"

                    hide paz ta
                    with easeoutright

                    show guest furry
                    with easeinright

                    mrcustard "Sign on payment is $1000, and the salary is $20 an hour. Youngstown has a low cost of living and a great park."

                    hide guest
                    with easeoutright

                    show paz ta
                    with easeinright

                    pt "{i}eheheh{/i} So many ways to eat..."

                    hide paz ta
                    with easeoutright

                    menu:

                        ann_thoughts "Sounds fishy, but any job involving sushi probably is."

                        "Accept Job":

                            show guest furry
                            with easeinright

                            mrcustard "Excellent. We'll give you the sign on bonus at the restaurant."

                            hide guest
                            with easeoutright

                            show paz ta
                            with easeinright

                            pt "{i}eheheh{/i} {size=8}Screwed like a corkscrew cocktail.{/size}"

                            hide paz ta
                            with easeoutright

                            show guest furry
                            with easeinright

                            mrcustard "Ignore her. Please take this card. It has the escrow account info on it."

                            hide guest
                            with easeoutright

                            python:
                                money += 1000
                                paz_ta_nyotaimori = True

                            return

                        "Decline Job":

                            show paz ta
                            with easeinright

                            pt "{i}eheheh{/i} I knew this fakery was pointless! It's two to one! Let's just eat her now!"

                            hide paz ta
                            with easeoutright

                    jump cannibal_discovery

                "You're cannibals!":

                    show paz ta
                    with easeinright

                    pt "Figa! You figured it out! My secret meatball recipe calls for prime human cuts!"

                    hide paz ta
                    with easeoutright

                    label cannibal_discovery:

                        # TODO: Fix indentation
                        pass

                    show guest furry
                    with easeinright

                    mrcustard "People have really been loving her secret ingredients. I'm sure they'll love you too."

                    hide guest
                    with easeoutright

                    show paz ta
                    with easeinright

                    pt "It's not like we lie or anything! We ask guests if they want our special {i}Raw Man{/i}, and they say yes!"

                    hide paz ta
                    with easeoutright

                    show guest furry
                    with easeinright

                    mrcustard "What about {i}Can I get hu-many meat-balls{/i}? That's a classic!"

                    hide guest
                    with easeoutright

                    show ann disgust
                    with easeinleft

                    a "Why pick me? There were larger people in that panel you know!"

                    hide ann
                    with easeoutleft

                    show paz ta
                    with easeinright

                    pt "Your online four star review screwed our perfect record! A shame too - I really do like angel hair."

                    hide paz ta
                    with easeoutright

                    show ann disgust
                    with easeinleft

                    a "I knew your meatballs were weird! I'm updating my review from four stars to one after this you psychos!"

                    hide ann
                    with easeoutleft

                    show guest furry
                    with easeinright

                    mrcustard "Anyone who disses our meatballs publicly gets burned - Well Done!"

                    hide guest
                    with easeoutright

                    menu:
                    
                        ann_thoughts "Holy Toledo! These guys really are cannibals!"

                        "Time for Magical Girl JUSTICE!" if magical_girl:

                            show ann genki
                            with easeinleft

                            a "Taste some {b}TWO COURSE JUSTICE{/b}!" with vpunch

                            hide ann
                            with easeoutleft

                            show guest furry
                            with easeinright

                            mrcustard "Ouf! Ouchie!{nw}" with vpunch

                            hide guest
                            with easeoutright

                            show paz ta
                            with easeinright

                            pt "Figa! You can't eat justic- Owie! {nw}" with vpunch

                            hide paz ta
                            with easeoutright

                            show ann genki
                            with easeinleft

                            a "{b}Justice{/b} is {b}served{/b}" with vpunch

                            hide ann
                            with easeoutleft

                        "The only person getting served tonight is you!":

                            ann_thoughts "I was captain of the kickboxing team in high school. These doughboys are nothing."

                            show ann disgust
                            with easeinleft

                            a "Ladies and gentlemen, tonight we've got a two course meal! First up? Custard - Well beaten!" with vpunch

                            hide ann
                            with easeoutleft

                            show guest furry
                            with easeinright

                            mrcustard "Ouch!{nw}" with vpunch

                            hide guest
                            with easeoutright

                            show ann disgust
                            with easeinleft

                            a "My only cut you deserve is an uppercut!" with vpunch

                            hide ann
                            with easeoutleft

                            show paz ta
                            with easeinright

                            pt "Figa! {nw}"

                            hide paz ta
                            with easeoutright

                            show ann genki
                            with easeinleft

                            a "{b}Justice{/b} is {b}served{/b}" with vpunch

                            hide ann
                            with easeoutleft

                        "Your gig is up! I already called the Health Inspector.":

                            ann_thoughts "It's a lie but they might eat it up."

                            show guest furry
                            with easeinright

                            mrcustard "I don't buy it. How did you know in advance?"

                            hide guest
                            with easeoutright

                            show ann smug
                            with easeinleft

                            a "Your panel was so dirty, it only seemed logical your business was dirty too."

                            hide ann
                            with easeoutleft

                            show paz ta
                            with easeinright

                            pt "Wait, you remembered to give the Health Inspector's car a {b}Youngstown Tune Up{/b} right?"

                            hide paz ta
                            with easeoutright

                            show guest furry
                            with easeinright

                            mrcustard "Eh? I thought you wanted me to give her car a {b}Cleveland Steamer{/b}!"

                            hide guest
                            with easeoutright

                            show paz ta
                            with easeinright

                            pt "Figa! Figa! Figa! We gotta clean up shop pesto!"

                            hide paz ta
                            with easeoutright

                        "I have Creutzfeld-Jakob Disease.":

                            ann_thoughts "It's a lie but they might buy it. An outbreak of CJD will get traced right back to them."

                            show paz ta
                            with easeinright

                            pt "Figa! Figa! Figa! It's unethical to serve someone with CJD. Sorry to waste your time!"

                            hide paz ta
                            with easeoutright

                    show will
                    with easeinright

                    ww "What in tarnation is causing the racket in here? You're disturbing the mango library folks."
                    # Mango ain't a typo. He means manga though.

                    hide will
                    with easeinright

                    show paz ta
                    with easeinright

                    pt "Mango Library? Serves them right! Mangos aren't nearly as good as tomatoes!"

                    hide paz ta
                    with easeoutright

                    show ann smug
                    with easeinleft

                    a "Howdy partner! These yellow-bellies are plumb cannibals."

                    hide ann
                    with easeoutleft

                    show paz ta
                    with easeinright

                    pt "Figa! This is a misunderstanding! True yellow plumbs can not be found in America!"

                    hide paz ta
                    with easeoutright

                    show will
                    with easeinright

                    ww "Cosplaying the Donner Party ain't against Animarathon rules, but LARPing them is! You boys are coming with me!"
                    # The Donner Party is a group of pioneers who used cannibalism.

                    hide will
                    with easeinright

                    ann_thoughts "Time to get out of here!"

                    ann_thoughts "I'll just withdraw from that online escrow account while they're busy..."

                    ann_thoughts "Done! $1000 from those cannibal scum."

                    $ money += 1000

        "Thanks? Maybe some other time.":

            pt "Mama Mia! Thank you!"

            hide paz ta
            with easeoutright

            ann_thoughts "[pt] leaves her business card on top of my hair and leaves with a hop and a skip."

            $ paz_ta_date = True

            ann_thoughts "This is still really uncomfortable. Everyone is staring."

    return

#     _        _
#    / \   ___| | ___  ___ _ __  
#   / _ \ / __| |/ _ \/ _ \ '_ \ 
#  / ___ \\__ \ |  __/  __/ |_) |
# /_/   \_\___/_|\___|\___| .__/ 
#                         |_|
label noodles_asleep:

    play music this_reminds_me_of_something_p4 fadeout 1

    show black
    with irisin

    a "Sleep is good. mmmm..."

    show orange
    with dissolve

    hide black
    with dissolve

    ann_thoughts "No more instant ramen... I'd rather eat tasty iron woks..."

    show red
    with dissolve

    hide orange
    with dissolve

    a "{size=70}SNORE{/size}"
    # TODO: Make snore SFX

    ann_thoughts "Don't eat that... the noodles... are people..."

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

label noodles_considerations:

    menu:
    
        ann_thoughts "Was there anything I wanted to consider before the panel starts?"

        "Who is the panelist?":

            ann_thoughts "[pt] is a renowned Italian Chef from Yongstown Ohio. Despite only being 22 years old she's considered a prodigy."

            ann_thoughts "Some would even call her a cooking prodigy. However many note that her social skills are rather lacking."

            ann_thoughts "I've been to her restaurant once before but I think it was overhyped. I wonder what she'll have to say?"

        "What are noodles?":

            ann_thoughts "Noodles are a kind of food. Ramen and some kinds of pasta such as spaghetti are popular noodles."

            ann_thoughts "Instant noodles are particularly popular here because they're cheap and quick to make."

        "That's all":

            return

    jump noodles_considerations
