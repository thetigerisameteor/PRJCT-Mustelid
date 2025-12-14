# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mal angry at left
        
    with dissolve

    # These display lines of dialogue.

    Mal "You."

    show bry sad at right


    with vpunch

    Bry "WHAT?"

    show mal angry 

    Mal "I think you are a f-"

    show bry sadawkward

    Bry "..."

    show bry serious

    Mal "I hate you."
    $ persistent.main_menuimage = 3
    # This ends the game.

    return

