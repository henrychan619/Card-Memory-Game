#Python project: Card Memory Game

import simplegui
import random

list1 = []
for i in range(8):
    list1.append(i)
    
list2 = []
for i in range(8):
    list2.append(i)
    
list1.extend(list2)
random.shuffle(list1)

exposed = []
for a in range(8):
    exposed.append(a)

exposed2 = []
for b in range(8):
    exposed2.append(b)
    
exposed.extend(exposed2)

for c in range(16):
    exposed[c] = False

counter = 0


# helper function to initialize globals
def new_game():
    global list1, state, counter, exposed
    random.shuffle(list1)
    counter = 0
    for c in range(16):
        exposed[c] = False
    
    state = 0
    
# define event handlers
def mouseclick(pos):
    global list1
    global exposed
    global state
    global guess1
    global guess2, indice, indice2, counter
    if state == 0:
        indice = pos[0]//50
        if exposed[indice] == False:
            exposed[indice] = True
            guess1 = list1[indice]
            counter += 1
            state = 1
    elif state == 1:
            indice2 = pos[0]//50
            if exposed[indice2] == False:
                exposed[indice2] = True
                guess2 = list1[indice2]
                counter += 1
                state = 2
    elif state == 2:
        if guess2 != guess1:
            exposed[indice] = False
            exposed[indice2] = False
        elif guess2 == guess1:
            exposed[indice] = True
            exposed[indice2] = True
        indice = pos[0]//50
        if exposed[indice] == False:
            exposed[indice] = True
            guess1 = list1[indice]
            counter += 1
            state = 1
            
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list1
    global exposed, indice, indice2, counter
    for i in range(16):
        if exposed[i] == True:
            canvas.draw_text(str(list1[i]),(i*50+25,50),20,"White")
        elif exposed[i] == False:
            canvas.draw_line((25+(i*50),0),(25+(i*50),100),50,"Blue")
    label.set_text("Turn: " +str(counter))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turn = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling rollinginging
new_game()
frame.start()
