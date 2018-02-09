# Animarathon XVI: Operation Ohio Kawaii Kafe
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

label kawaii_kafe:

    play music breathe fadeout 1

    scene bg kafe
    with dissolve

    menu:

        ann_thoughts "Looks like they aren't ready. They do have some menus though."

        "Read the menu.":

            kawaii_m "FOOD: Kawaii Avocado Sugoi Sandwich"

            kawaii_m "Drinks: Doki Doki Sugar Black Coffee"

            menu:

                ann_thoughts "Should I read the back?"

                "Read the back.":

                    kawaii_m "HISTORY OF THE KAWAII KAFE"

                    kawaii_m "In 1965 the University started using it's Ivn-N 1401 Computer to speed up speed dating."

                    kawaii_m "In 1969 the computer was stolen. The program was ported to an EG Shooting Star, which is used to this day!"
                    # Electrical Graphing Shooting Star

                    kawaii_m "Though our dating algorithm is proprietary, it's only fair you get a sneak peak of our secret sauce!"

                    kawaii_m "cout \<\< guest_id\[i\] \"Is most compatible with \" \<\< guest_id\[rand()\] << endl;"
                    # \ is an escape character. It doesn't render.
                    # Using ALGOL or ASM would be more accurate the c++ here.
                    # However I'm not sure how to write that accurately for this model.

                    kawaii_m "As you can see, it's impossible to cheat!"

                    ann_thoughts "What garbage!\n This code just randomly selects guests!" with hpunch

                "Don't read the back.":

                    ann_thoughts "I'm ready to order!"

        "Don't read the menu":

            ann_thoughts "I already know what I want."

    ann_thoughts "It looks like they have a punch card attached to the menu."

    kawaii_m "This is the mandatory personality quiz! Complete it to find true love!"

    menu:

        kawaii_m "Q0: I feel like my choices matter."

        "0":

            $ kawaii_selection = "ann"

        "1":

            $ kawaii_selection = "adorina"

        "2":

            $ kawaii_selection = "adroina"

        "3":

            $ kawaii_selection = "orion"

        "4":

            $ kawaii_selection = "frog sensei"

        "20" if kawaii_calcium_manga == True:

            $ kawaii_selection = "skeleton"

    menu:

        kawaii_m "Q1: If Kawaii Kafe ran out of Doki Doki Sugar Black Coffee, I'd be cool with that."

        "0":

            pass

        "1":

            pass

        "2":

            pass

        "3":

            pass

        "4":

            pass

    ann_thoughts "I bet they never planned on giving us that in the first place."

    menu:

        kawaii_m "Q2: I enjoy meeting strangers at the deli."

        "0":

            pass

        "1":

            pass

        "2":

            pass

        "3":

            pass

        "4":

            pass

    ann_thoughts "Like a corner deli for a sandwich? Why is this even a question?"
    # ;-)

    menu:

        kawaii_m "Q3: When I see crazy anime hair, I make a happy face."

        "0":

            ann_thoughts "I can't take crazy anime hair seriously."

        "1":

            ann_thoughts "I'm not a fan of crazy anime hair."

        "2":

            ann_thoughts "Crazy anime hair is just OK."

        "3":

            ann_thoughts "Crazy anime hair is kind of cute."

        "4":

            ann_thoughts "Crazy anime hair is too funny not to like."

    menu:

        kawaii_m "Q4: For breakfast I like to enjoy a nice _____."

        "0":

            pass

        "1":

            pass

        "2":

            pass

        "3":

            pass

        "4":

            pass

    ann_thoughts "Who eats numbers for breakfast?! What I like to eat for breakfast is not a number!"

    ann_thoughts "Not a number... NaN. Naan. Naan bread actually sounds pretty good for breakfast!"

    menu:

        kawaii_m "Q5: I am in year _ of college."

        "0":

            ann_thoughts "I'm not going to give a real number."

        "1":

            ann_thoughts "I don't want to reveal how old I am!"

        "2":

            ann_thoughts "I could pass for a sophomore right?"

        "3":

            ann_thoughts "I was a junior not long ago..."

        "4":

            ann_thoughts "Can't wait to get out of here!"

    menu:

        kawaii_m "Q6: I am satisfied with my Animarathon experience."

        "0":

            $ kawaii_selection = "orion"

            ann_thoughts "Animarathon is a huge rip off this year!"

        "1":

            ann_thoughts "I'm not a fan of Animarathon."

        "2":

            ann_thoughts "Animarathon is OK."

        "3":

            ann_thoughts "Animarathon has been surprisingly entertaining this year!"

        "4":

            ann_thoughts "Animarathon has been way more interesting this year!"

    menu:

        kawaii_m "Q7: Avocado sandwiches are the most romantic treat."

        "0":

            ann_thoughts "What's romantic about an avocado sandwich?"

        "1":

            ann_thoughts "I can think of better foods."

        "2":

            ann_thoughts "Avocado sandwiches are ok, I guess?"

        "3":

            ann_thoughts "It's good, but avocado toast is better."

        "4":

            ann_thoughts "The aroma of a fresh avocado sandwich is an aphrodisiac."

    menu:

        kawaii_m "Q8: When I receive my avocado sandwich I will cut it with my katana."

        "0":

            pass

        "1":

            pass

        "2":

            pass

        "3":

            pass

        "4":

            pass

    ann_thoughts "Were we supposed to bring a katana?"

    menu:

        kawaii_m "Q9: Maids are cute!"

        "0":

            pass

        "1":

            pass

        "2":

            pass

        "3":

            pass

        "4":

            pass

    ann_thoughts "I'm done!"

    show orion normal
    with easeinright

    o "Ayy it's [a]! We going to the Kawaii Kafe or what?"

    hide orion
    with easeoutright

    show ann happy
    with easeinleft

    a "[o] you're free! What happened?"

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "You wouldn't believe it! [fs] tied my waist to a tree and made me throw knives at him!"

    hide orion
    with easeoutright

    show ann happy
    with easeinleft

    a "Bodacious! Did he catch them or something?"

    hide ann
    with easeoutleft

    show orion smug
    with easeinright

    o "Nah! Ninth one I threw hit him between his eyes! Bullseye!"

    hide orion
    with easeoutright

    show ann disgust
    with easeinleft

    a "Bogus! I'm not paying your bail again!"

    hide ann
    with easeoutleft

    show orion normal
    with easeinright

    o "It's cool! He just pulled it out with a resplendent look on his face."

    hide orion
    with easeoutright

    show ann disgust
    with easeinleft

    a "Seriously? People die when they're stabbed in the brain! I bet that mask of his absorbed the blow."

    hide ann
    with easeoutleft

    show orion smug
    with easeinright

    o "That's no mask. It's his actual skin."

    hide orion
    with easeoutright

    show ann disgust
    with easeinleft

    a "What?! There's no way his head is naturally that big!"

    hide ann
    with easeoutleft

    show orion smug
    with easeinright

    o "He bragged about getting subdermal implants including ch-LCD skin and scandium-titanium alloy armor."

    hide orion
    with easeoutright

    show ann happy
    with easeinleft

    a "That knife must have been blocked by his armor!"

    hide ann
    with easeoutleft

    show orion sad
    with easeinright

    o "So uh... Don't look now, but [fs] is standing right behind you."

    hide orion
    with easeoutright

    ann_thoughts "Drat! Double drat! He probably heard everything!"

    show ann normal
    with easeinleft

    a "Let's go to the Kawaii Kafe and finish talking later."

    hide ann
    with easeoutleft

    show adorina maid normal
    with easeinright

    aa "Welcome to Kawaii Kafe desu! Please hand over your punch card desu!"

    hide adorina maid normal
    with easeoutright

    show shooting star off at truecenter
    with easeintop

    aa "An algorithm will pair you with your perfect date desu!"

    show shooting star on at truecenter

    aa "3 desu... 2 desu... 1 desu...! Moshi Moshi desu! You're perfect date desu..."

    hide shooting star
    with easeouttop

    # Catch in case nothing is set.

    if kawaii_selection == "Nothing":

        $ kawaii_selection = "orion"

    # Determine Results

    if kawaii_selection == "ann":

            show adorina maid genki
            with easeinright

            aa "You desu! Romance is true desu!"

            hide adorina
            with easeoutright

            call kawaii_kafe_date_ann

    if kawaii_selection == "orion":

            show adorina maid genki
            with easeinright

            aa "[o] desu! Romance is blood desu!"

            hide adorina
            with easeoutright

            call kawaii_kafe_date_orion

    if kawaii_selection == "adroina":

            show adorina maid genki
            with easeinright

            aa "Me desu! Romance is a miracle desu!"

            hide adorina
            with easeoutright

            call kawaii_kafe_date_adorina

    if kawaii_selection == "frog sensei":

            show adorina maid genki
            with easeinright

            aa "[fs] desu! Romance is served desu!"

            hide adorina
            with easeoutright

            call kawaii_kafe_date_frog_sensei

    if kawaii_selection == "skeleton":

            show adorina maid genki
            with easeinright

            aa "Calcium-kun desu!?"

            hide adorina
            with easeoutright

            call kawaii_kafe_date_skeleton

    return
