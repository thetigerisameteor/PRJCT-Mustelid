# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg backrooms

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mal neutral at left
        
    with dissolve

    # These display lines of dialogue.

    Mal "Bryer, Where the fuck are we?"

    show bry happy at right
    with dissolve

    Bry "Dude, don't worry. about it. This is the place we're staying in for the night."
    
    Bry "We're saving around..."

    "I check my notepad, and take out my pen to direct my eyes towards all of the expenses made for the month."

    Bry "Thirty dollars!"

    

    Mal "You're seriously making us stay in the average eastern european household..."

    show mal angry

    show bry awkward

    extend "for thirty. {w}fucking. {w} dollars?!?!"

    Bry "..."

    Mal "I hate you. So much."
    
    $ persistent.main_menuimage = 3
    # This ends the game.

    return
