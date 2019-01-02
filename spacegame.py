#Creating our Map
WIDTH = 800
HEIGHT = 600
#Character Position
player_x = 600
player_y = 350

def draw():
    screen.blit(images.backdrop, (0,0))
    #changing the order of mars/ship will put the ship behind mars.
    screen.blit(images.mars, (50,50))
    screen.blit(images.astronaut, (player_x, player_y))
    screen.blit(images.ship, (130,150))

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