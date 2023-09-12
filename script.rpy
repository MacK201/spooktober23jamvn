# The script of the game goes in this file.

#state variables - help us control which ending player gets and different results of conditionals
#based on player's choices

#because we are going to have multiple tasks with similar attributes, gonna deviate a bit from
#renpy syntax and use oop stuff (specifically classes)

#i'm more familiar with classes and their methods and this will make it a lot easier for me 
#to update things during the main gameplay loop
define time = 0
define mentalHealth = 100

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Celia")
define co = Character("Coworker")
define v = Character("Nightmare Glitch")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "How could you Celia?"
    
    "{size=+2}How could you Celia?"

    "{size=+10}How could you Celia?"

    "{size=+15}HOW COULD YOU CELIA?!"

    "{size=+10}{b}CELIA!{/b}"

    "Celia turns her head and her vision refocuses. It looks like a glitch on a screen. She sees a glimpse of a monster and screams."

    v "CELIA!"

    #blurry coworker image here and then fade into HQ image?

    "Celia's vision refocuses once more and sees one of her coworkers."

    co "Celia, get it together! {i}Your{/i} butt's not on the chopping block, you know."

    co "And please don't forget about those BIRA training module tasks, I need you to have them done as fast as you can." 

    "Celia nods at her and returns to her computer."   

    return
