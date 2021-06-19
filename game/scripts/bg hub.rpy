# Define hex color for background.
image bg black = "#000000"
image circlebutton = "circle.png"
image backgroundbutton = "backgroundbutton.png"

# Skip main menu on boot.
# label main_menu:
#    return

screen vis_buttons:

    if True:
        vbox:
            textbutton ("{image=backgroundbutton}"):

                xpos 0

                xanchor 0

                ypos 0

                yanchor 0

                action Return("background")
    if True:
        vbox:
            textbutton ("{image=circlebutton}"):

                xpos 500

                xanchor 0.5

                ypos 500

                yanchor 0.5

                action Return("pub")

# The program starts here.
label start:

    # Variables
    $ succeeded_pecks = 0
    $ trials = 0

    # Block Rollback
    $ renpy.block_rollback()
    $ renpy.retain_after_load()

    # Blank screen.
    scene bg black

    label main_loop:

        $ trials = trials + 1

        # Pause program
        $ ui.pausebehavior(1, result="")
        $ ui.interact()

        call screen vis_buttons

        window show None

        if _return == "pub":

            $ succeeded_pecks = succeeded_pecks + 1

            "success"

        if _return == "background":

            "failure"

        "Number of successful pecks is [succeeded_pecks]"

        "Number of trials is [trials]."

        if trials >= 5:
            return

        jump main_loop

    # Write results

    python:
        file = open("results.txt","w")
        file.write("Trials" + trials + "Succeeded Pecks" + succeeded_pecks)
        file.close()

    # Exit to main menu
    return
