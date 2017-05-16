# Rock-paper-scissors-lizard-Spock 

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random

# helper functions
# converts number to a name using if/elif/else  
def number_to_name(number):
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "Spock"
    elif number == 2:
        number = "paper"
    elif number == 3:
        number = "lizard"
    elif number == 4:
        number = "scissors"
    else:
        number = "Please use a number from 1-4."
    return number

    
def name_to_number(name):
    
    if name == "rock":
        name = 0
    elif name == "Spock":
        name = 1
    elif name == "paper":
        name = 2
    elif name == "lizard": 
        name = 3
    elif name == "scissors":
        name = 4
    else:
        name = "Please choose rock, paper, scissors, lizard, or spock."
    return name


def rpsls(name): 
    
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # compute difference of player_number and comp_number modulo five
    game_results =(comp_number - player_number) % 5
    
     # use if/elif/else to determine winner
    if game_results == 0:
        message = "Player and computer tie!"
    elif game_results == 1 or game_results == 2:
       message = "Computer wins!"
    elif game_results == 3 or game_results == 4:
        message = "Player wins!"
    
        
    # convert comp_number to name using number_to_name
    number_to_name(comp_number)
    
    print "Player chooses", number_to_name(player_number)
    
    print "Computer chooses", number_to_name(comp_number)
    
    print message
    
    print ""
    
    
    return name
    
   

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


