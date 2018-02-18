# Animarathon XVI: Operation Ohio Special Graphics Definitions
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
#  ____                  _       _ 
# / ___| _ __   ___  ___(_) __ _| |
# \___ \| '_ \ / _ \/ __| |/ _` | |
#  ___) | |_) |  __/ (__| | (_| | |
# |____/| .__/ \___|\___|_|\__,_|_|
#       |_|                        

#   ____      _                
#  / ___|___ | | ___  _ __ ___ 
# | |   / _ \| |/ _ \| '__/ __|
# | |__| (_) | | (_) | |  \__ \
#  \____\___/|_|\___/|_|  |___/

# These define colors that can be used as backgrounds.

image white = "#ffffff"

image grey = "#666666"

image gunmetal = "#92a1a5"

image black = "#000000"

image orange = "#ff7300"

image pink = "#e56372"

image brown = "#4f2c1d"

image blue = "#002664"

image purple = "#754aa9"

image sky blue = "#4c84e6"

image yellow = "#eaab00"

image red = "#bb0000"

#  _____                     __                          
# |_   _| __ __ _ _ __  ___ / _| ___  _ __ _ __ ___  ___ 
#   | || '__/ _` | '_ \/ __| |_ / _ \| '__| '_ ` _ \/ __|
#   | || | | (_| | | | \__ \  _| (_) | |  | | | | | \__ \
#   |_||_|  \__,_|_| |_|___/_|  \___/|_|  |_| |_| |_|___/

# These provide special transformations not included with Ren'Py

# Flips an image horizontally.
transform flip:
    xzoom -1.0

#   ____ _ _      _      _           ____            _   _                  
#  / ___| (_) ___| | __ | |_ ___    / ___|___  _ __ | |_(_)_ __  _   _  ___ 
# | |   | | |/ __| |/ / | __/ _ \  | |   / _ \| '_ \| __| | '_ \| | | |/ _ \
# | |___| | | (__|   <  | || (_) | | |__| (_) | | | | |_| | | | | |_| |  __/
#  \____|_|_|\___|_|\_\  \__\___/   \____\___/|_| |_|\__|_|_| |_|\__,_|\___|

image ctc:
    anim.Blink("particles/ctc.webp")
    
image ctc crossbones:
    anim.Blink("particles/crossbones.webp")
    
image ctc pachi:
    anim.Blink("particles/pachi.webp")

#  _____ _ _   _        ____                           
# |_   _(_) |_| | ___  / ___|  ___ _ __ ___  ___ _ __  
#   | | | | __| |/ _ \ \___ \ / __| '__/ _ \/ _ \ '_ \ 
#   | | | | |_| |  __/  ___) | (__| | |  __/  __/ | | |
#   |_| |_|\__|_|\___| |____/ \___|_|  \___|\___|_| |_|

# These define special title screen graphics and animations.

image title text:
    "backgrounds/title.webp"
    yzoom 0
    linear 0.5 yzoom 1.0
    parallel:
        linear 5.0 xzoom 0.95
        linear 5.0 xzoom 1.0
        repeat

image title ball 1:
    "backgrounds/title ball.webp"
    subpixel True
    parallel:
        rotate 0
        linear 16.0 rotate 360
        repeat
    parallel:
        linear 5.0 xzoom 0.9
        linear 5.0 xzoom 1.0
        repeat

image title ball 2:
    "backgrounds/title ball.webp"
    subpixel True
    parallel:
        rotate 0
        linear 15.0 rotate -360
        repeat
    parallel:
        linear 5.0 xzoom 1.1
        linear 5.0 xzoom 1.0
        repeat

image title ball 3:
    "backgrounds/title ball.webp"
    subpixel True
    parallel:
        rotate 0
        linear 5.0 rotate -360
        repeat
    parallel:
        linear 5.0 xzoom 1.1
        linear 5.0 xzoom 1.0
        repeat

image title ball 4:
    "backgrounds/title ball.webp"
    subpixel True
    parallel:
        rotate 0
        linear 7.0 rotate -360
        repeat
    parallel:
        linear 5.0 xzoom 1.1
        linear 5.0 xzoom 1.0
        repeat

image title floops ai leg:
    "characters/floopsai/floops ai leg.webp"
    subpixel True
    block:
        linear 5.0 yzoom 1.1
        linear 5.0 yzoom 0.5
        repeat

# Mutant Floops.ai was a mistake.
image title = LiveComposite((1920,1080),
                          (0,0), "white",
                          (1200,250), "title ball 1",
                          (1150,250), "title ball 2",
                          (1000,250), "title ball 1",
                          (1100,250), "title ball 3",
                          (900,250), "title ball 1",
                          (800,250), "title ball 2",
                          (500,250), "title ball 1",
                          (600,250), "title ball 4",

                          (700,550), "title floops ai leg",
                          (800,550), "title floops ai leg",
                          (1300,550), "title floops ai leg",
                          (1400,550), "title floops ai leg",

                          (780,500), "title text")

#   ____ _     _                      
#  / ___| |__ (_)_ __   ___  ___  ___ 
# | |   | '_ \| | '_ \ / _ \/ __|/ _ \
# | |___| | | | | | | |  __/\__ \  __/
#  \____|_| |_|_|_| |_|\___||___/\___|
# The purpose of converting text into graphics is to save on file size.
# Chinese Font files take up a LOT of space. Over a dozen megabytes are saved by this.
# Only because there is a little Chinese is this OK.
# If I were expecting the player to actually read I would suck it up and add the font file for real.
# But given my level of expertise with Chinese... (My Chinese is extremely bad, just ask anyone in the Chinese Club!)

# 谢谢!再见
# Thanks! Goodbye!
image chinese 000:
    "chinese/0.webp"

# 你叫骗子和你是骗子
# Your name is conman and you are a conman!
image chinese 001:
    "chinese/1.webp"

# 你叫骗子? 哈哈呵呵哈哈呵呵哈哈!
# Your name is conman? He He Ha Ha He He Ha Ha He He!
image chinese 002:
    "chinese/2.webp"

# 你好?
# Hello?
image chinese 003:
    "chinese/3.webp"

# 你好! 我叫骗子!
# Hello! My name is conman!
image chinese 004:
    "chinese/4.webp"

# 呵呵
# Ha Ha
image chinese 005:
    "chinese/5.webp"

# 好! 你说中文!
# Good! You speak Chinese!
image chinese 006:
    "chinese/6.webp"

# 对不起!
# I'm sorry!
image chinese 007:
    "chinese/7.webp"

# 我喜欢名字!我叫骗子!
# I like my name! My name is Conman!
image chinese 008:
    "chinese/8.webp"

# 啊
# Eh?
image chinese 009:
    "chinese/9.webp"

#  ____       _              _       _
# / ___|  ___| |__   ___  __| |_   _| | ___ 
# \___ \ / __| '_ \ / _ \/ _` | | | | |/ _ \
#  ___) | (__| | | |  __/ (_| | |_| | |  __/
# |____/ \___|_| |_|\___|\__,_|\__,_|_|\___|

# Header

image schedule_title:
    Text("Animarathon XVI Day 1 Schedule", size=36)

image schedule_large_panel_room:
    Text("Large Panel Room", size=20)

image schedule_small_panel_room:
    Text("Small Panel Room", size=20)

# 1

image schedule_cosplay:
    Text("Advanced Cosplay Panel", size=20)

image schedule_taiko:
    Text("Taiko Today", size=20)

# 2

image schedule_kawaii:
    Text("Kawaii Kafe", size=20)

# 3

image schedule_gpm:
    Text("GPM DëVërsë Is Hell", size=20)

image schedule_noodle:
    Text("The Noodle Panel", size=20)

# 4

image schedule_welchert:
    Text("Welchert In The Crib: Z is TOP ANIME", size=16)

image schedule_chinese:
    Text("The Chinese Cartoon Panel", size=20)

# 5

image schedule_group_photo:
    Text("Group Photo", size=20)

# 6

image schedule_robot:
    Text("ANIMECHATHON", size=20)

image schedule_favorite_anime:
    Text(favorite_anime + " Panel", size=20)
# Concatenates string value with the word panel.

image side_schedule = LiveComposite(
    (600, 1080),
    (0, 0), "orange",
    (0, 0), "schedule_title",
    (0, 100), "schedule_large_panel_room",
    (300, 100), "schedule_small_panel_room",
    (0, 150), "schedule_cosplay",
    (300, 150), "schedule_taiko",
    (240, 200), "schedule_kawaii",
    (0, 250), "schedule_gpm",
    (300, 250), "schedule_noodle",
    (240, 300), "schedule_group_photo",
    (0, 350), "schedule_welchert",
    (300, 350), "schedule_chinese",
    (0, 400), "schedule_robot",
    (300, 400), "schedule_favorite_anime")


#  ____  _                            _             
# / ___|| |_ _ __ ___  __ _ _ __ ___ (_)_ __   __ _ 
# \___ \| __| '__/ _ \/ _` | '_ ` _ \| | '_ \ / _` |
#  ___) | |_| | |  __/ (_| | | | | | | | | | | (_| |
# |____/ \__|_|  \___|\__,_|_| |_| |_|_|_| |_|\__, |
#                                             |___/ 

image streaming text 000:
    Text("I <3 you GPM!", size=80)

image streaming text 001:
    Text("MODS!!!", size=80)

image streaming text 002:
    Text("Type ur password in chat it hides it see ****!", size=60)

image streaming text 003:
    Text("User has been kicked for violating TOS.", size=60)

image streaming text 004:
    Text("Succ", size=90)

image streaming text 005:
    Text("Someone named gpm_ebooks is spamming my pm wtf...", size=40)

image streaming text 006:
    Text("Can someone ban gpm_ebooks please? He's spamming me!", size=40)

image streaming text 007:
    Text("ROFL", size=60)

image streaming text 008:
    Text("Aww! Very cute!", size=55)

image streaming text 009:
    Text("d00d w7f!", size=40)

image streaming text 010:
    Text("I'd let GPM repaint me! <3", size=40)

image streaming text 011:
    Text(">:3", size=60)

image streaming text 012:
    Text("Elargement Product! FREE elargement product make U bigger now!", size=40)

image streaming text 013:
    Text("how do post in chat???", size=40)

image streaming text 014:
    Text("Sure was nice of GPM to invite us to his livestream!", size=40)

image streaming text 015:
    Text("Take clothes off plz", size=40)

image streaming text 016:
    Text("Plz do nut bulli. ;-(", size=69)

image streaming text 017:
    Text("Anyone wanna RP? - Danknutta", size=60)

image streaming text 018:
    Text("GPM check out my fursona!!! >:-3", size=40)

image streaming text 019:
    Text("Noooooooooooooooooo!", size=50)

image streaming text 020:
    Text("lol so hard i poo", size=60)

image streaming text 021:
    Text("help i forgot my username", size=40)

image streaming text 022:
    Text("Holy Toledo!", size=40)

image streaming text 023:
    Text("If you post that meme one more time I swear...", size=50)

image streaming text 024:
    Text("Hey GPM can u throw on some dubstep bangers?", size=40)

image streaming text 025:
    Text("GPM confirmed a cute! <3", size=69)

image streaming text 026:
    Text("I'd like to order 3 XL pizzas, cheez loq, and 5 diet two liters.", size=40)

image streaming text 027:
    Text("gpm can i be ur doki doki waifu?", size=60)

image streaming text 028:
    Text("gay purple man moar liek GAY purple man am i rite???", size=40)

image streaming text 029:
    Text("VISUAL NOVEL NOT A REAL GAME WRRYYYYYYY", size=40)

image streaming text 030:
    Text("_/(*_*)\_ D O N T - D O - I T", size=50)
# It's supposed to be a guy shrugging. My ascii art one liners ain't the best. :-(

image streaming text 031:
    Text("Anyone else playing this game in 2XXX?", size=50)

image streaming text 032:
    Text("I'm a Time Traveler from 2038! A terrible event is about to happen!", size=30)

image streaming text 033:
    Text("this is not real.", size=60)

image streaming text 034:
    Text("should i post over 1tb hentai folder?", size=40)

image streaming text 035:
    Text("yo GPM can i get a meme in here?", size=40)

image streaming text 036:
    Text("lets cyber", size=60)

image streaming text 037:
    Text("gpm is illuminate do not deceive trick", size=40)

image streaming text 038:
    Text("superstar streamer!", size=60)
# XD

image streaming text 039:
    Text("XD XD XD XD XD XD XD", size=40)

image streaming text 040:
    Text("DESU DESU DESU DESU DESU", size=40)

image streaming text 041:
    Text("i thought gpm was kill????", size=90)

image streaming text 042:
    Text("clevelandese shaman streamer where?", size=40)

image streaming text 043:
    Text("how do i doughnut. DUCKING AUTOCORRECT I MEAN DONATE", size=40)

image streaming text 044:
    Text("gpm turn volume up i cant here plox", size=50)

image streaming text 045:
    Text("guys GPM is ripping off my OC gaelic lavender male", size=40)

image streaming text 046:
    Text("guys i cant make it stop please make it STOP!", size=60)
# FOR REAL

image streaming text 047:
    Text("gpm can you form a boy band?", size=50)

image streaming text 048:
    Text("this calls for MAMBO! LOL IM SO RANDOM!!!", size=50)

image streaming text 049:
    Text("PLAYFEEL NOT PACHINKO OK?!", size=40)

image streaming text 050:
    Text("GPM is a space alien don't believe his lies!", size=40)

image streaming text 051:
    Text("GPM. Algee Pee Mmmm. GPM DID TOLEDO WATER CRISIS 2014!!!", size=40)

image streaming text 052:
    Text("guys why arent my emotes working", size=50)

image streaming text 053:
    Text("how do i log out chat can please kick me please", size=40)

image streaming text 054:
    Text("I would share my chocolate milk with GPM.", size=40)

image streaming text 055:
    Text("GPm how do i make big money streaming", size=60)

image streaming text 056:
    Text("hey gpm wanna grab a sandwich at the deli?", size=40)
# Fo real

image streaming text 057:
    Text("DO A PUSH UP!", size=50)

image streaming text 058:
    Text("No bueno", size=60)

image streaming text 059:
    Text("Me gusta le GPM", size=50)

image streaming text 060:
    Text("I TROLL U!!! UPSET? YOU SHOULD BE!", size=40)

image streaming text 061:
    Text("STOP", size=50)

image streaming text 062:
    Text("GPM Dakimakura where?", size=50)

image streaming text 063:
    Text("MARRY ME GPM <3", size=60)

image streaming text 064:
    Text("This is a bad stream too much water. 7/10", size=40)
# GET IT?

image streaming text 065:
    Text("can someone call an ambulance cuz i'm dying!!! lmao!!!", size=40)

image streaming text 066:
    Text("help grand dad saw me watching this how do i explain?", size=40)

image streaming text 067:
    Text("I've got a gat you take that back!", size=40)

image streaming text 068:
    Text("419 represent!", size=90)

image streaming text 069:
    Text("U A TRUE NUTA", size=69)

image streaming text 070:
    Text("this is bait", size=50)

image streaming text 071:
    Text("is this $9001 dollar computer cool for streaming?", size=50)

image streaming text 072:
    Text("tentacle monster when", size=70)

image streaming text 073:
    Text("I'm taping this stream you sickos!", size=40)

image streaming text 074:
    Text("GTFO!!!", size=60)

image streaming text 075:
    Text("sage", size=60)

image streaming text 076:
    Text("this game succs, not even any real H scenes.", size=40)

image streaming text 077:
    Text("op is a gay purple man", size=40)

image streaming text 078:
    Text("SPOILER: ORION KILLS FROG SENSEI", size=60)

image streaming text 079:
    Text("you cant ban me!! I have 777 proxy!!!!!11!!!11!", size=40)

image streaming text 080:
    Text("Anime is disgusting. Get out of there GPM!", size=40)

image streaming text 081:
    Text("Stop forcing memes!", size=40)

image streaming text 082:
    Text("BANHAMMER TIEM!!!", size=50)

image streaming text 083:
    Text("WTF are with these old memes????", size=40)

image streaming text 084:
    Text("rabu", size=80)

image streaming text 085:
    Text("dress as a magical girl or i wont donate", size=60)

image streaming text 086:
    Text("NEEDS MOAR DRIFTING", size=50)

image streaming text 087:
    Text("How come the block game doesnt have guns.", size=40)

image streaming text 088:
    Text("Is GPM moving to Japan now?", size=40)

image streaming text 089:
    Text("help my computer cant handle this stream ", size=40)

image streaming text 090:
    Text("anyone else watching on dial up?", size=46)

image streaming text 091:
    Text("GPM I CHALLENGE YOU TO DUEL WITH MY KATANA!", size=50)

image streaming text 092:
    Text("gpm is a pretty cool guy", size=60)

image streaming text 093:
    Text("how come your streams not vr?", size=40)

image streaming text 094:
    Text("HA! HA! HA!", size=50)

image streaming text 095:
    Text("legalize gay purple man", size=40)

image streaming text 096:
    Text("how come it says i got to wait before i post moar?", size=40)

image streaming text 097:
    Text("Me too! XD", size=60)

image streaming text 098:
    Text("Me too! DX", size=62)

image streaming text 099:
    Text("its a prank my dude.", size=60)

image streaming text 100:
    Text("What did GPM just say? I flushed my toilet and couldn't hear him.", size=40)

image streaming text 101:
    Text("GPM will you join my web blog?", size=40)

image streaming text 101:
    Text("GPM for president of the universe 2020!", size=40)

image streaming text 102:
    Text("GPM should stream while ice skating!", size=40)

image streaming text 102:
    Text("AEIOU", size=40)

image streaming text 103:
    Text("XD", size=40)

image streaming text 104:
    Text("DX", size=40)

image streaming text 105:
    Text("he said that! IN BED!", size=40)

image streaming text 106:
    Text(";-)", size=40)

image streaming text 107:
    Text("AAAAAAAAAAAAA", size=50)

image streaming text 108:
    Text(":^)", size=60)

image streaming text 109:
    Text(":^(", size=60)

image streaming text 110:
    Text("(*_*)", size=60)

image streaming text 111:
    Text("ayy", size=50)

image streaming text 112:
    Text("WHO SAID THAT", size=50)

image streaming text 113:
    Text("A E S T H E T I C S", size=40)

image streaming text 114:
    Text("F", size=50)

image streaming text 115:
    Text("nice meme", size=50)

image streaming text 116:
    Text("AMIRITE?", size=60)

image streaming text 117:
    Text("THE STREAM IS A LIE!", size=60)

image streaming text 118:
    Text("HOW!", size=60)

image streaming text 119:
    Text("HET!", size=60)

image streaming text random:
    choice:
        "streaming text 000"
    choice:
        "streaming text 001"
    choice:
        "streaming text 002"
    choice:
        "streaming text 003"
    choice:
        "streaming text 004"
    choice:
        "streaming text 005"
    choice:
        "streaming text 006"
    choice:
        "streaming text 007"
    choice:
        "streaming text 008"
    choice:
        "streaming text 009"
    choice:
        "streaming text 010"
    choice:
        "streaming text 011"
    choice:
        "streaming text 012"
    choice:
        "streaming text 013"
    choice:
        "streaming text 014"
    choice:
        "streaming text 015"
    choice:
        "streaming text 016"
    choice:
        "streaming text 017"
    choice:
        "streaming text 018"
    choice:
        "streaming text 019"
    choice:
        "streaming text 020"
    choice:
        "streaming text 021"
    choice:
        "streaming text 022"
    choice:
        "streaming text 023"
    choice:
        "streaming text 024"
    choice:
        "streaming text 025"
    choice:
        "streaming text 026"
    choice:
        "streaming text 027"
    choice:
        "streaming text 028"
    choice:
        "streaming text 029"
    choice:
        "streaming text 030"
    choice:
        "streaming text 031"
    choice:
        "streaming text 032"
    choice:
        "streaming text 033"
    choice:
        "streaming text 034"
    choice:
        "streaming text 035"
    choice:
        "streaming text 036"
    choice:
        "streaming text 037"
    choice:
        "streaming text 038"
    choice:
        "streaming text 039"
    choice:
        "streaming text 040"
    choice:
        "streaming text 041"
    choice:
        "streaming text 042"
    choice:
        "streaming text 043"
    choice:
        "streaming text 044"
    choice:
        "streaming text 045"
    choice:
        "streaming text 046"
    choice:
        "streaming text 046"
    choice:
        "streaming text 047"
    choice:
        "streaming text 048"
    choice:
        "streaming text 049"
    choice:
        "streaming text 050"
    choice:
        "streaming text 051"
    choice:
        "streaming text 052"
    choice:
        "streaming text 053"
    choice:
        "streaming text 054"
    choice:
        "streaming text 055"
    choice:
        "streaming text 056"
    choice:
        "streaming text 057"
    choice:
        "streaming text 058"
    choice:
        "streaming text 059"
    choice:
        "streaming text 060"
    choice:
        "streaming text 061"
    choice:
        "streaming text 062"
    choice:
        "streaming text 063"
    choice:
        "streaming text 064"
    choice:
        "streaming text 065"
    choice:
        "streaming text 066"
    choice:
        "streaming text 067"
    choice:
        "streaming text 068"
    choice:
        "streaming text 069"
    choice:
        "streaming text 070"
    choice:
        "streaming text 071"
    choice:
        "streaming text 072"
    choice:
        "streaming text 073"
    choice:
        "streaming text 074"
    choice:
        "streaming text 075"
    choice:
        "streaming text 076"
    choice:
        "streaming text 077"
    choice:
        "streaming text 078"
    choice:
        "streaming text 079"
    choice:
        "streaming text 080"
    choice:
        "streaming text 081"
    choice:
        "streaming text 082"
    choice:
        "streaming text 083"
    choice:
        "streaming text 084"
    choice:
        "streaming text 085"
    choice:
        "streaming text 086"
    choice:
        "streaming text 087"
    choice:
        "streaming text 088"
    choice:
        "streaming text 089"
    choice:
        "streaming text 090"
    choice:
        "streaming text 091"
    choice:
        "streaming text 092"
    choice:
        "streaming text 093"
    choice:
        "streaming text 094"
    choice:
        "streaming text 095"
    choice:
        "streaming text 096"
    choice:
        "streaming text 097"
    choice:
        "streaming text 098"
    choice:
        "streaming text 099"
    choice:
        "streaming text 100"
    choice:
        "streaming text 101"
    choice:
        "streaming text 102"
    choice:
        "streaming text 103"
    choice:
        "streaming text 104"
    choice:
        "streaming text 105"
    choice:
        "streaming text 106"
    choice:
        "streaming text 107"
    choice:
        "streaming text 108"
    choice:
        "streaming text 109"
    choice:
        "streaming text 110"
    choice:
        "streaming text 111"
    choice:
        "streaming text 112"
    choice:
        "streaming text 113"
    choice:
        "streaming text 114"
    choice:
        "streaming text 115"
    choice:
        "streaming text 116"
    choice:
        "streaming text 117"
    choice:
        "streaming text 118"
    choice:
        "streaming text 119"

image display streaming text:
    block:
        alpha 0.0
        "streaming text random"
        linear 5.0 alpha 1.0
        linear 5.0 alpha 0.0
        repeat
#   ___  _   _               
#  / _ \| |_| |__   ___ _ __ 
# | | | | __| '_ \ / _ \ '__|
# | |_| | |_| | | |  __/ |   
#  \___/ \__|_| |_|\___|_|   

image union3d effect:
    "backgrounds/union3d.webp"
    alpha 0.0
    yzoom 0.0
    parallel:
        linear 1.0 alpha 1.0
    parallel:
        linear 1.0 yzoom 1.0

image union3d = LiveComposite((1000,1080),
                              (0,100), "union3d effect",
                              (0,280), "union3d effect",
                              (0,460), "union3d effect",
                              (0,640), "union3d effect")

image openstreetmap copyright = LiveComposite((1000,1080),
                                    (900,0), "popups/osm copyright.webp")
    

image pachi_ball:
    "particles/pachi.webp"
                
image sakura 0:
    "particles/sakura.webp"

image sakura 1:
    At("sakura 0", flip)

image sakura = SnowBlossom(Animation("sakura 0", 1,"sakura 1", 1))

image confetti 0:
    "particles/confetti.webp"

image confetti 1:
    "particles/confetti.webp"
    xzoom -1.0

image confetti = SnowBlossom(Animation("confetti 0", 1,"confetti 1", 1))

image 3D Tutorial:
    "backgrounds/title.webp"
    subpixel True
    block:
        linear 3.0 xzoom 0.0
        linear 3.0 xzoom 1.0
        repeat

image union repainted:
    "popups/union.webp"
    pause 2.0
    "neural_style/union.webp" with dissolve

image game over:
    "backgrounds/gameover.webp"
