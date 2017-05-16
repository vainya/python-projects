
# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

num = 217

def get_next(current):
    if current%2 ==0:
        return current/2
    else:
        return current*3+1


#print num
#print get_next(num)

# timer callback

def update():
    global num
    num = get_next(num)
    # Stop iterating after max_iterations
    if num == 1:
        timer.stop()
        print "Output is", num
    else:
         print num
        
        

# register event handlers

timer = simplegui.create_timer(1, update)
timer.start()