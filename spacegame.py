#Creating our Map
WIDTH = 800
HEIGHT = 600
#Character Position
player_x = 700
player_y = 50

top_left_x = 100
top_left_y = 150

DEMO_OBJECTS = [images.floor, images.pillar]

room_height = 7
room_width = 5

#y which list, x which list item
#room_map is used to remember items in the room that the player is currently in
room_map = [
    [1,1,1,1,1],
    [1,0,0,0,1], 
    [1,0,1,0,1],
    [1,0,0,0,1], 
    [1,0,0,0,1], 
    [1,0,0,0,1],
    [1,1,1,1,1]
]
#printing/looping over our map
# for y in range(7):
#     for x in range(5):
#         print(room_map[y][x], end='')
#     print()



# def draw():
#     screen.blit(images.backdrop, (0,0))
#     screen.blit(images.mars, (50,50))
#     screen.blit(images.astronaut, (player_x, player_y))
#     screen.blit(images.ship, (645,23))

def draw():
    for y in range(room_height):
        for x in range(room_width):
            image_to_draw = DEMO_OBJECTS[room_map[y][x]]
            screen.blit(image_to_draw,
            (top_left_x + (x*30),
            top_left_y + (y*30) - image_to_draw.get_height()))

def game_loop():
    global player_x, player_y
    if keyboard.right:
        player_x += 5
    elif keyboard.left:
        player_x -= 5
    elif keyboard.up:
        player_y -= 5
    elif keyboard.down:
        player_y += 5
#adjusting the time will change how fast/slow char moves.
clock.schedule_interval(game_loop, .01)