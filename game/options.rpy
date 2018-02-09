## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Animarathon 16: Operation Ohio")
# A-NWO-VN-16-VIP Anime In Northwest Ohio Visual Novel 16 Variation in Production


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.0"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
This visual novel was created by Anime In Northwest Ohio members for Animarathon XVI from December 2016 to February 2018.

Anime In Northwest Ohio is an official student organization at a public university in Bowling Green, Ohio that promotes Japanese Popular Culture in Northwest Ohio.

Animarathon is a student run anime convention, and is made possible by convention visitors and community support.

We hope to see you next year! :D

ANO thanks {a=https://gee.pm/}GeePM{/a} for allowing us to feature him in our game.

{b}Music Credits{/b}

Music by {a=https://twitter.com/SimGretina}Sim Gretina{/a} are licensed under the {a=https://creativecommons.org/licenses/by/3.0/}CC BY 3.0{/a} License.

* {a=https://soundcloud.com/simgretina/royalty-free-yo}Yo{/a}

* {a=https://soundcloud.com/simgretina/royalty-free-breathe}Breathe{/a}

* {a=https://soundcloud.com/simgretina/royalty-free-moist-mechas}Moist Mechas{/a}

* {a=https://soundcloud.com/simgretina/water}Water{/a}

* {a=https://soundcloud.com/simgretina/02-this-reminds-me-of-something}This Reminds Me Of Something{/a}

* {a=https://soundcloud.com/simgretina/royalty-free-orange-beach}Orange Beach{/a}

{a=https://musopen.org/music/107/modest-mussorgsky/pictures-at-an-exhibition/}Promenade Moderator non tanto pesante{/a} as preformed by the Skidmore College Orchestra is licensed under the {a=https://creativecommons.org/publicdomain/mark/1.0/}CC PD{/a} License

Works preformed by the {a=https://musopen.org/music/performer/musopen-string-quartet/}The MuseOpen String Quartet{/a} are used under the {a=https://creativecommons.org/publicdomain/mark/1.0/}CC PD{/a}

* {a=https://musopen.org/music/1589/ludwig-van-beethoven/string-quartet-no-6-in-b-flat-major-op-18-no-6/}String Quartet No. 6 in B Flat Major - IV{/a} 

{b}Audio Credits{/b}

{a=https://kenney.nl/}Kenny Vleugels's{/a} assets are licensed under the {a=https://creativecommons.org/publicdomain/zero/1.0/}CC0 1.0{/a}.

* {a=https://kenney.nl/assets/ui-audio}UI Audio{/a}

{b}ANO Credits{/b}

The dedicated ANO members that made this game.

* Skeleton Artist & Frog Sensei Manga Artist: Kirsten McLaughlin

* Frog Sensei & Floops.ai concept: Alex Kidd

* Programmer & General Art: Max Brickner

{b}Appendix{/b}

Loose your {b}Power Chip{/b}, and can't make it to the ANO office?

{b}Power Code{/b}: 419-352-8475

Thank you for RTFM.

{b}Open Source License Information{/b}

Anime In Northwest Ohio isn't the officially associated with any of these groups or assets.

{b}OpenStreetMap{/b}

OpenStreetMap data is {b}© OpenStreetMap contributors{/b} and is used under the {a=https://www.openstreetmap.org/copyright}Open Data Commons Open Database License{/a}.

{b}USGS Orthoimagery{/b}

This game makes use of Public Domain {a=https://www.usgs.gov/}United States Geological Survey High Resolution Orthoimagery{/a} of Wood County Ohio, USA.

{b}Typography{/b}

This game makes use of the{a=https://www.theleagueofmoveabletype.com/junction}Junction{/a}, {a=https://www.theleagueofmoveabletype.com/knewave}Knewave{/a}, and {a=https://www.theleagueofmoveabletype.com/sniglet}Sniglet{/a} typefaces provided under the Open Font License, which is included in the game font directory.

For pre-rendered Chinese this game uses {a=https://www.google.com/get/noto/}Noto Sans{/a} licensed under the SIL Open Font License 1.1.

{b}Neural Networks{/b}

The {a=http://www.robots.ox.ac.uk/%7Evgg/research/very_deep/}VGG 19 Layer Convolutional Neural Network Model{/a} is used under the {a=https://creativecommons.org/licenses/by/4.0/}Creative Commons BY 4.0 License{/a}

{a=https://github.com/jcjohnson/neural-style}Neural Style{/a} is MIT licensed, see it's {a=https://github.com/jcjohnson/neural-style/}repository{/a} for more information.

{b}VR{/b}

{a=https://aframe.io/}A-Frame{/a} is MIT licensed, see their {a=https://github.com/aframevr/aframe}repo{/a} for more information.

{b}Visual Assets{/b}

This game makes use of Art provided by {a=http://www.metmuseum.org/}The Metropolitan Museum of Art{/a} under the {a=https://creativecommons.org/publicdomain/zero/1.0/}CC0 1.0{/a}, for more information please see the license file in the game art directory.

{b}Animarathon XV Game Code{/b}

This game code is licensed under the {a=https://www.gnu.org/licenses/gpl-3.0.en.html}GNU GPL Version 3{/a}. See the included license files for more information.

{b}Animarathon XV Game Art{/b}

This game art is licensed under the {a=https://creativecommons.org/licenses/by/4.0/}Creative Commons BY 4.0 License{/a} for original assets except where otherwise noted. See the included license files for more information.
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "animarathon16"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

define config.sample_sound = "audio/kenny-ui/click1.opus"
# define config.sample_voice = ""


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "<from 0.0 to 6.7>music/This Reminds Me Of Something.opus"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = dissolve


## Used when entering the main menu after the game has ended.

define config.end_game_transition = dissolve


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.5)
define config.window_hide_transition = Dissolve(.5)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 64


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 16


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "aXVI-1515968027"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    # build.classify('**.html', None)
    # Excluding HTML breaks one panel.

    ## To archive files, classify them as 'archive'.

    # build.classify('**.png', 'archive')
    # build.classify('**.jpg', 'archive')
    # build.classify('**.webp', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    # build.documentation('*.html')
    build.documentation('*.txt')
    build.documentation('*.md')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Shy Ann (BG9001)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "animarathon/test-project"
