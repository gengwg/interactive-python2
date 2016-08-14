# Demonstration of a magnifier on a map

try:
        import simplegui
except ImportError:
        import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = MAP_WIDTH // SCALE
CAN_HEIGHT = MAP_HEIGHT // SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 120
mag_pos = [CAN_WIDTH // 2, CAN_HEIGHT // 2]


# Event handlers
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    mag_pos = list(pos)

# Draw map and magnified region
def draw(canvas):
    # Draw map first
    canvas.draw_image(image,
            # source center at map center, source width and height
            [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT],
            # dest center at canvas center, dest width and height
            [CAN_WIDTH // 2, CAN_HEIGHT // 2], [CAN_WIDTH, CAN_HEIGHT])

    # Draw magnifier
    map_center = [SCALE * _ for _ in mag_pos]
    # find the good position
    #map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
    # use same size for map and mag
    map_rectangle = [MAG_SIZE, MAG_SIZE]
    mag_center = mag_pos
    mag_rectangle = [MAG_SIZE, MAG_SIZE]
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)

# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier", CAN_WIDTH, CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)

# Start frame
frame.start()

