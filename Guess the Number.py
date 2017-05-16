# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simpleguitk as simplegui
import random
import math


# initialize global variables used in your code
number_of_guesses = 0
range_of_number = 100



# helper function to start and restart the game
def new_game():
   global number_of_guesses
   global secret_number
   global range_of_number
    
   secret_number = random.randrange(0,range_of_number)
    
         
   if range_of_number == 100:
             number_of_guesses = int(math.ceil
                                (math.log(100 -0+ 1,2)))
     
   elif range_of_number == 1000:
        number_of_guesses = int(math.ceil(math.log
                                                  (1000 - 0 +1,2)))
   else:
        print "You did not enter a number in the correct range"
        
        
   print "New game. Range is from 0 to", range_of_number
   print "Number of remaining guesses is", number_of_guesses
   print "\n"
                                              
        
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global range_of_number
    range_of_number = 100
    new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    
    global range_of_number
    range_of_number = 1000
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global number_of_guesses
    global secret_number
    
    print "Guess was", guess
    number_of_guesses -= 1
    print "Number of remaining guesses is", number_of_guesses
    
    if number_of_guesses == 0 and int(guess) != secret_number:
        print "You ran out of guesses. The number was", secret_number
        print "\n"
        new_game()
    elif number_of_guesses == 0 and int(guess) == secret_number:
        print "You guessed correctly."
        print "\n"
        new_game()
    elif int(guess) == secret_number:
        print "You guessed correctly."
        print "\n"
        new_game()
    elif int(guess) > secret_number:
        print "Lower!"
        print "\n"
    else:
        print "Higher!"
        print "\n"
        
    
# create frame

f = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements

f.add_button('Range is [0, 100)', range100, 200)
f.add_button('Range is [0, 1000)', range1000, 200)
f.add_input('Enter a guess', input_guess, 200)

# call new_game and start frame
new_game()
f.start()

# always remember to check your completed program against the grading rubric
