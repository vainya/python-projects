# implementation of card game - Memory

import simplegui
import random

WIDTH = 50
HEIGHT = 100

card_list = [0,1,2,3,4,5,6,7] + [0,1,2,3,4,5,6,7]
exposed = [False]*16
state = 0
moves = 0
first_card = 0
second_card = 0

# helper function to initialize globals
def new_game():
    global exposed, card_list, state, moves
    exposed = [False]*16
    random.shuffle(card_list)
    state = 0
    moves = 0
    label.set_text("Turns = " + str(moves))
    
    
    
     
# define event handlers
def mouseclick(pos):
    global moves, state, first_card, second_card, idx
    # add game state logic here
    idx = pos[0]// WIDTH
    if exposed[idx] == False:
        exposed[idx] = True
        if state == 0:
            state = 1
            first_card = idx
        elif state == 1:
            second_card = idx
            state = 2
            moves += 1
        else:
            if card_list[first_card] != card_list[second_card]:
                exposed[first_card] = False
                exposed[second_card] = False
                first_card = idx
            elif card_list[first_card] == card_list[second_card]:
                first_card = idx
            state = 1
        label.set_text("Turns = " + str(moves))
       
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for c in range(0 , len(card_list)):
        
        if exposed[c]== True:
            
            canvas.draw_text(str(card_list[c]), 
                             (WIDTH*c, 70), 80, 'White')
        elif exposed[c] == False:
            canvas.draw_polygon([(WIDTH*c,0), 
                                 (WIDTH*(c+1), 0), (WIDTH*(c+1), 100),
                                 (WIDTH*c,100)],3,"Red","Green")
     
    
    


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric