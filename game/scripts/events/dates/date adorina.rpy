# Animarathon XVI: Operation Ohio Kawaii Kafe Date: Adorina
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

label kawaii_kafe_date_adorina:

    show adorina maid normal
    with easeinright

    if magical_girl == False:

        aa "It's you desu! You're that guy with the moe sister desu!"

        hide adorina
        with easeoutright

        show ann embarrassed
        with easeinleft

        a "Actually I'm not a guy and [o] isn't{nw}"

        hide ann
        with easeoutleft

    if magical_girl == True:

        aa "It's you desu! Have you been making us lots of desu dollars as a magical girl desu?"

        if money >= 100000:

            hide adorina
            with easeoutright

            show ann genki
            with easeinleft

            a "You betcha! We're loaded now!"
    
            hide ann
            with easeoutleft

        if money >= 10000:

            show ann genki
            with easeinleft

            a "You betcha! We're loaded now!"
    
            hide ann
            with easeoutleft

        if (money <= 10000) and (money >= reset_money):

            show ann happy
            with easeinleft

            a "Thanks! I've made a bit of money"
    
            hide ann
            with easeoutleft

        if (money < reset_money) and (money >= 0):

            ann_thoughts "Holy Toledo! I can't let her know I spent the money!"

            show ann embarrassed
            with easeinleft

            a "Yeah, uh, that money thing! Sure! Yup!"
    
            hide ann
            with easeoutleft

        if money <= 0:

            ann_thoughts "Holy Toledo! I can't let her know I'm in debt!"

            show ann embarrassed
            with easeinleft

            a "Y-you betcha!"
    
            hide ann
            with easeoutleft

            show adorina maid smug
            with easeinright

            aa "If you're lying, I will shank you open and sell your organs.{w} I know a guy in Cleveland who buys for a good price desu."

            hide adorina
            with easeoutright

            show ann embarrassed
            with easeinleft

            a "O-of course!"
    
            hide ann
            with easeoutleft

    show adorina maid normal
    with easeinright

    aa "Hey Mr. Arnold! You better eat that desulicious avocado sandwich desu! I unwrapped it from catering myself desu!"

    hide adorina
    with easeoutright

    ann_thoughts "Come on. [o] is a hard name to remember, but how hard is a name like [a] to remember?"

    $ hunger -= 20

    show ann happy
    with easeinleft

    a "I'll take this avocado sandwich and snack on it! By the way, my name is [a] and my brother's name is O{nw}"

    hide ann
    with easeoutleft

    show adorina maid genki
    with easeinright

    aa "I've got my eye on your sister Oregano desu! She's moe! In other words the perfect mascot desu!"

    aa "We could force her into an kawaii mascot uniform desu! Maybe a pink alpaca or a pink pony desu!{nw}"

    aa "Nah, ponies are so 2011, what about a frog desu?{nw}"

    aa "But we already have unkawaii [fs] desu...{nw}"

    aa "Maybe we could steal one of the computer club's computers and use CGI to make Oregon into a mascot desu...{nw}"

    aa "But everyone knows that high quality kinos are better desu!{nw}"

    aa "Cantonese Shaman Girl Desu?{nw}"

    aa "Your sister, she's way cute though desu!{nw}"

    aa "Maybe we could use you as a mascot Antonio desu!{nw}"

    aa "Forget it Antonio, you're too ugly desu!{nw}"

    aa "Back to the original plan, [o] in a costume desu.{nw}"

    hide adorina
    with easeoutright

    show ann happy
    with easeinleft

    a "You got his name right! That's amazing!{nw}"

    hide ann
    with easeoutleft

    show adorina maid genki
    with easeinright

    aa "Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu{nw}"

    aa "Do you remember the Kent Brawnies and Liftasisters from Animarathon XIII desu?{nw}"

    aa "Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu{nw}"

    aa "Of course you desu don't, they got banned for lifting guests desu!{nw}"

    aa "Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Mon Desu{nw}"

    aa "Can blame them, life is short so you gotta go quick desu.{nw}"

    aa "Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu Ex Machina{nw}"

    aa "AEIOU as they say in the tyroleans and in moonspeak desu.{nw}"

    aa "Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Desu, Deku{nw}"

    aa "Hey Mr. Amadeus, what do you think da da da da desu de gozaimasu-desu?"
    # Not referring to Ann here at all. She knows the walls have ears.

    hide adorina
    with easeoutright

    ann_thoughts "What a motormouth. I think she's talking to me now."

    show ann normal
    with easeinleft

    a "What's up?"

    hide ann
    with easeoutleft

    show adorina maid smug
    with easeinright

    aa "Thank you for meeting with me, It's been a desulight."

    hide adorina
    with easeoutright

    return
