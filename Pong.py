# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = HEIGHT/2
paddle2_pos = HEIGHT/2
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-random.randrange(60, 180)/60 , random.randrange(120, 240)/60]
score_1 = 0
score_2 = 0
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos[] and ball_vel[0]for x and [1] for y for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as list
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    ball_vel[1] = -random.randrange(60, 180)/60
    
    if direction == RIGHT:
        ball_vel[0] = random.randrange(120, 240)/60
        
    elif direction == LEFT:
        ball_vel[0] = -random.randrange(120, 240)/60
            
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score_1, score_2  # these are ints
    
    score_1 = 0 
    score_2 = 0  
    paddle1_pos = HEIGHT/2
    paddle2_pos = HEIGHT/2
    paddle1_vel = 0
    paddle2_vel = 0  
    spawn_ball(random.randrange(0,2))

def draw(c):
    global score_1, score_2, paddle1_pos, paddle2_pos, ball_pos, ball_vel 
    global paddle1_vel, paddle2_vel
    
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball and calculate and increment scores
    
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[1] < BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    if ball_pos[0] - BALL_RADIUS < PAD_WIDTH:
        if ball_pos[1] in range(paddle1_pos, paddle1_pos + PAD_HEIGHT + BALL_RADIUS):
            ball_vel[0] = 1.1 * -ball_vel[0]
        else:
            score_2 += 1
            spawn_ball(RIGHT)
    
    if ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
        if ball_pos[1] in range(paddle2_pos, paddle2_pos + PAD_HEIGHT + BALL_RADIUS):
            ball_vel[0] = 1.1 * -ball_vel[0]
        else:
            score_1 += 1
            spawn_ball(LEFT)
            
     #draw ball draw the ball on the canvas
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
   
    if paddle1_pos + paddle1_vel >= HALF_PAD_HEIGHT -40 and paddle1_pos + paddle1_vel <= HEIGHT - 30 - HALF_PAD_HEIGHT :
         paddle1_pos += paddle1_vel
    
    if paddle2_pos + paddle2_vel >= HALF_PAD_HEIGHT -40 and paddle2_pos + paddle2_vel <= HEIGHT -30 - HALF_PAD_HEIGHT:
         paddle2_pos += paddle2_vel

   
    # draw paddles 
    c.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], 8, 'White')
    c.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos],[WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], 8, "White")
    
  
    
    c.draw_text(str(score_1), (170, 50), 36, "White")
    c.draw_text(str(score_2), (400, 50), 36, "White")

    #vel PAD_WIDTH horizontal and -PAD_WIDTH
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -8
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 8
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 8
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -8    
    
def keyup(key):
    global paddle1_vel, paddle2_vel
     
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
new_game()
frame.start()
