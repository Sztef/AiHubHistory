# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tea")
define m = Character("Men")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_school1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show tea1

    # These display lines of dialogue.

    t "Suck my toes"

    menu:

       "no":
          jump no


       "Alright":
          jump yes
    

    # This ends the game.

return


label no:

t "Whaaaaat (wha, wha wha with echo effect), you bih Ill make more Suno AI SONGS WRRRR"
play music toes_suno volume 0.95

hide tea1 with fade
show tea2

t "MADE ANOTHER SUNO SONG (MESSAGE FROM ME YES SUNO IS FUNNY)"



return

label yes:

t "Ok Let's go"

scene bg_school2 with fade
scene bg_dark with fade
play music sucking_toes volume 1

t "ohohohohoho"


