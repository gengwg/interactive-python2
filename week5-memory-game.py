# An implementation of Memory game
# (c) gengwg [at] gmail com

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random

# cards
deck = []
# exposed lists. if True, expose card. Else Green rectangle.
exposed = []

# define event handlers
def new_game():
    """reinitiate game global variables"""
    global state, deck, exposed, click1, click2, turn
    state = 0
    # two global variables to store the index of each of the two cards
    # that were clicked in the previous turn.
    click1 = 0
    click2 = 0
    turn = 0
    deck = 2 * range(8)
    random.shuffle(deck)
    exposed = [False for _ in deck]
    label.set_text("Number of Tries: " + str(turn))


def mouseclick(pos):
    """handler of mouse click"""
    global state, click_index, click1, click2, turn
    click_index = pos[0] / 50
    if not exposed[click_index]:
        if state == 0:
            state = 1
            click1 = click_index
            exposed[click_index] = True
        elif state == 1:
            state = 2
            exposed[click_index] = True
            click1 = click_index
        else:
            state = 1
            turn += 1
            exposed[click_index] = True
            if deck[click1] != deck[click2]:
                exposed[click1] = False
                exposed[click2] = False
            click2 = click_index
            label.set_text("Number of Tries: " + str(turn))


def draw(canvas):
    """draw handler"""
    for i, num in enumerate(deck):
        if exposed[i]:
            canvas.draw_text(str(num), [50 * i + 25, 62], 48, "White")
        else:
            canvas.draw_polygon([(50 * i, 0), (50 * (i + 1), 0),
                                 (50 * (i + 1), 100), (50 * i, 100)],
                                2, 'White', 'Green')

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game, 200)

# register event handlers
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouseclick)

label = frame.add_label("", 200)
# get things rolling
new_game()
frame.start()

