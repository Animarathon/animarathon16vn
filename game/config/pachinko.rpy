# Animarathon XVI: Operation Ohio Pachinko
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
# Author :      Maxwell Paul Brickner (Adapted from RenPy MIT licensed tutorial code.)
# Maintainer :  Maxwell Paul Brickner

#  _____ _   _    _    _   _ _  __ __   _____  _   _ 
# |_   _| | | |  / \  | \ | | |/ / \ \ / / _ \| | | |
#   | | | |_| | / _ \ |  \| | ' /   \ V / | | | | | |
#   | | |  _  |/ ___ \| |\  | . \    | || |_| | |_| |
#   |_| |_| |_/_/   \_\_| \_|_|\_\   |_| \___/ \___/ 
# A huge thank you to Renpy Tom for his wonderful renpy engine, and the tutorial it includes.
# Thank you! ^ _ ^ -M

#  __  __ ___ _____   _     _                         
# |  \/  |_ _|_   _| | |   (_) ___ ___ _ __   ___ ___ 
# | |\/| || |  | |   | |   | |/ __/ _ \ '_ \ / __/ _ \
# | |  | || |  | |   | |___| | (_|  __/ | | | (_|  __/
# |_|  |_|___| |_|   |_____|_|\___\___|_| |_|\___\___|
# The following is adapted the Renpy Tutorial by pytom, which is licensed under the MIT license.
# https://github.com/renpy/renpy/blob/3b5e7c821a5945ee2913b36b5ca0634c00f208d0/tutorial/game/demo_transform.rpy
# Please see the help page of the game for more info.

    #  ____             _                                   _ 
    # | __ )  __ _  ___| | ____ _ _ __ ___  _   _ _ __   __| |
    # |  _ \ / _` |/ __| |/ / _` | '__/ _ \| | | | '_ \ / _` |
    # | |_) | (_| | (__|   < (_| | | | (_) | |_| | | | | (_| |
    # |____/ \__,_|\___|_|\_\__, |_|  \___/ \__,_|_| |_|\__,_|
    #                       |___/

label pachinko_1:

    show bg rave with vpunch

    call pachinko_create

    show text "{size=50}SMASH THE BUTTON AND WIN THE MONEY!{/size}" at truecenter with dissolve
    $ renpy.pause(3.0, hard="True")
    hide text

    system "test"

    call pachinko_cleanup

    hide bg rave with vpunch

    return
    
    #   ____                _         ____        _ _
    #  / ___|_ __ ___  __ _| |_ ___  | __ )  __ _| | |___ 
    # | |   | '__/ _ \/ _` | __/ _ \ |  _ \ / _` | | / __|
    # | |___| | |  __/ (_| | ||  __/ | |_) | (_| | | \__ \
    #  \____|_|  \___|\__,_|\__\___| |____/ \__,_|_|_|___/

label pachinko_create:

    python:
        last_time = None
        balls = [
        
                 Ball("pachi_ball", 1050, 150, function=balls_update2),
                 Ball("pachi_ball", 900, 700),
                 Ball("pachi_ball", 950, 060),
                 Ball("pachi_ball", 700, 260),
                 Ball("pachi_ball", 850, 360),
                 Ball("pachi_ball", 400, 500),
                 Ball("pachi_ball", 250, 170),
                 Ball("pachi_ball", 400, 640),
                 Ball("pachi_ball", 870, 130),
                 Ball("pachi_ball", 1090, 1060),
                 Ball("pachi_ball", 1700, 600),
                 Ball("pachi_ball", 1000, 800),
                 Ball("pachi_ball", 600, 900),
                 Ball("pachi_ball", 1000, 300),
                 Ball("pachi_ball", 100, 600),
                 Ball("pachi_ball", 700, 400),
                 Ball("pachi_ball", 1500, 600),
                 Ball("pachi_ball", 419, 419),
                 Ball("pachi_ball", 777, 777),
                 
                 ]
        for i, b in enumerate(balls):
            renpy.show("ball%d" % i, what=b.transform)

    return

    #   ____ _
    #  / ___| | ___  __ _ _ __  _   _ _ __
    # | |   | |/ _ \/ _` | '_ \| | | | '_ \ 
    # | |___| |  __/ (_| | | | | |_| | |_) |
    #  \____|_|\___|\__,_|_| |_|\__,_| .__/ 
    #                                |_|

label pachinko_cleanup:

    # Get rid of the Pachinko Balls
    python:
        # Use Transmission Order.
        print(' . ...     .  .')
        for i,b in enumerate(balls):
            renpy.hide("ball%d" % i)
    return

label pachinko_init:
    init python:
        class Ball(object):
            def __init__(self, filename, x, y, function=None):

                self.transform = Transform(child=filename, xanchor=0.5, yanchor=0.5, rotate=0, function=function)
                self.x = x
                self.y = y

                #  ____                      _    ____             __ _
                # / ___| _ __   ___  ___  __| |  / ___|___  _ __  / _(_) __ _ 
                # \___ \| '_ \ / _ \/ _ \/ _` | | |   / _ \| '_ \| |_| |/ _` |
                #  ___) | |_) |  __/  __/ (_| | | |__| (_) | | | |  _| | (_| |
                # |____/| .__/ \___|\___|\__,_|  \____\___/|_| |_|_| |_|\__, |
                #       |_|                                             |___/ 
                MAX_SPEED = 750

                self.dx = renpy.random.uniform(-MAX_SPEED, MAX_SPEED)
                self.dy = renpy.random.uniform(-MAX_SPEED, MAX_SPEED)

                # Rotation speed.
                self.drotate = renpy.random.uniform(0, 180)

        def balls_collide(p1, p2):
    
            DOUBLE_RADIUS = 25
    
            x21 = p2.x - p1.x
            y21 = p2.y - p1.y

            d = math.hypot(x21, y21)
    
            if d > DOUBLE_RADIUS:
                return

            vx21 = p2.dx - p1.dx
            vy21 = p2.dy - p1.dy

            if (vx21 * x21 + vy21 * y21) > 0:
                return

            if x21 == 0:
                x21 = .00001

            a = y21 / x21
            dvx2 = -(vx21 + a * vy21) / (1 + a * a)

            p2.dx += dvx2
            p2.dy += a * dvx2
    
            p1.dx -= dvx2
            p2.dy -= a * dvx2
    
        def balls_update2(pilot, st, at):

            global last_time

            #  ____        _ _    ____             __ _
            # | __ )  __ _| | |  / ___|___  _ __  / _(_) __ _ 
            # |  _ \ / _` | | | | |   / _ \| '_ \| |_| |/ _` |
            # | |_) | (_| | | | | |__| (_) | | | |  _| | (_| |
            # |____/ \__,_|_|_|  \____\___/|_| |_|_| |_|\__, |
            #                                          |___/ 
            RADIUS = 25 / 2
            LEFT = RADIUS
            RIGHT = 1920 - RADIUS
            TOP = RADIUS
            BOTTOM = 1080 - RADIUS

            if last_time is None:
                dt = 0
            else:
                dt = st - last_time
    
            last_time = st

            #   ____      _ _ _     _
            #  / ___|___ | | (_)___(_) ___  _ __  
            # | |   / _ \| | | / __| |/ _ \| '_ \ 
            # | |__| (_) | | | \__ \ | (_) | | | |
            #  \____\___/|_|_|_|___/_|\___/|_| |_|
            # Handle current collisions.
            for i in xrange(0, len(balls)):
                for j in xrange(i + 1, len(balls)):
                    balls_collide(balls[i], balls[j])
    
            for i in balls:
    
                i.x += i.dx * dt
                i.y += i.dy * dt
    
                if i.x < LEFT:
                    i.x = LEFT
                    i.dx = abs(i.dx)
    
                if i.x > RIGHT:
                    i.x = RIGHT
                    i.dx = -abs(i.dx)
    
                if i.y < TOP:
                    i.y = TOP
                    i.dy = abs(i.dy)
    
                if i.y > BOTTOM:
                    i.y = BOTTOM
                    i.dy = -abs(i.dy)

            #  _____                     __
            # |_   _| __ __ _ _ __  ___ / _| ___  _ __ _ __ ___  ___ 
            #   | || '__/ _` | '_ \/ __| |_ / _ \| '__| '_ ` _ \/ __|
            #   | || | | (_| | | | \__ \  _| (_) | |  | | | | | \__ \
            #   |_||_|  \__,_|_| |_|___/_|  \___/|_|  |_| |_| |_|___/
            # Update the transforms.
            for i in balls:
    
                # This is the code that deals with Ren'Py to update the
                # various transforms. Note that we use absolute coordinates
                # to position ourselves with subpixel accuracy.
                i.transform.xpos = absolute(i.x)
                i.transform.ypos = absolute(i.y)
                i.transform.rotate = (i.drotate * st) % 360.0
    
                i.transform.update()
    
            return 0
