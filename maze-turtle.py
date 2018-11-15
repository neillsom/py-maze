import turtle
import math

wn = turtle.Screen()
wn.bgcolor('black')
wn.title('Python Maze')
wn.setup(750,750)

# Register shapes / images
turtle.register_shape('./resources/player2-right.gif')
turtle.register_shape('./resources/player2-left.gif')
turtle.register_shape('./resources/booty.gif')
turtle.register_shape('./resources/texture-2.gif')

#Create Pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('./resources/player2-right.gif')
        self.color('white')
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('./resources/player2-right.gif')
        self.color('red')
        self.penup()
        self.speed(0)
        self.apple = 0

    # Player movements. Lots of repeated code. need to optimize
    def go_up(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() + 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_down(self):
        move_to_x = self.xcor()
        move_to_y = self.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_left(self):
        move_to_x = self.xcor() - 24
        move_to_y = self.ycor()

        self.shape('./resources/player2-left.gif')

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def go_right(self):
        move_to_x = self.xcor() + 24
        move_to_y = self.ycor()

        self.shape('./resources/player2-right.gif')

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    # code to register collisions
    def is_collision(self, other):
        a = self.xcor()-other.xcor()
        b = self.ycor()-other.ycor()
        # a² + b² = c² to calc distance
        playerDis = math.sqrt((a ** 2) + (b ** 2))

        if playerDis < 5: # pixels
            return True
        else:
            return False



class Booty(turtle.Turtle):
    def __init__(self, x, y): # screen_x and screen_y
        turtle.Turtle.__init__(self)
        self.shape('./resources/booty.gif')
        self.color('red')
        self.penup()
        self.speed(0)
        self.apple = 25
        self.goto(x, y)

    def destroy(self): # not able to actually destroy, just move off screen for now
        self.goto(1000,1000)
        self.hideturtle()

# Create levels list
levels = ['']

# look for existing library for maze gen
# or start with large field

# Define first level
level_1 = [

    'XXXXXXXXXXXXXXXXXXXXXXXXX',
    'X   XXXX    XXXXXXXXO XXX',
    'X @ XXXX    XXX       XXX',
    'X   XXXXXX              X',
    'X  XX  XXX       X  X   X',
    'X      XXXXXX  XXX  XX  X',
    'XXXXX  X  XXX  XXX  XX  X',
    'XXXXX  X  XXX  XXXXXX  XX',
    'XXXXX          XX  X   XX',
    'XXXXX          XX  X  XXX',
    'XX     XXXXXXXXXX  X  XXX',
    'XX     XXX  XXXXX  X    X',
    'XXXX  XX    X           X',
    'X      X    X         XXX',
    'X      XXX  X  XXXXXX  XX',
    'X  XXXXX    X  XXXXXX  XX',
    'X  XX       X   XX  XXXXX',
    'X  XX O  X  XX  XX      X',
    'X  XX  XXX  XX  XX      X',
    'X  XX  XXX  XX  XX  XXX X',
    'X  XX  X    XX      X   X',
    'X  XX  X   XXXXX    X O X',
    'X      XX      XX  XX   X',
    'X      XX      XX  XX  XX',
    'XXXXXXXXXXXXXXXXXXXXXX XX'
]

# Add a bootys list
bootys = []

# Add maze to mazes list
levels.append(level_1)

# Create level setup function
def create_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # get the character at eaxy x,y coordinate
            # note the order of y and x in next line
            character = level[y][x]
            # calculate the screen x,y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # check if it is an x
            if character == 'X':
                pen.goto(screen_x, screen_y)
                pen.shape('./resources/texture-2.gif')
                pen.stamp()
                # add coordinates to wall list
                walls.append((screen_x, screen_y)) # tuple coordinate pair

            if character == '@':
                player.goto(screen_x, screen_y)

            if character == 'O':
                bootys.append(Booty(screen_x, screen_y))


# Create class instances
pen = Pen()
player = Player()

walls = []

# Set up level
create_maze(levels[1])
# print (walls)

# Keyboard controls
turtle.listen()
turtle.onkey(player.go_left,'Left')
turtle.onkey(player.go_right,'Right')
turtle.onkey(player.go_up,'Up')
turtle.onkey(player.go_down,'Down')

# Screen updates: off
wn.tracer(0)

# Main game loop
while True:
    for booty in bootys: # will run for each booty
        if player.is_collision(booty):
            player.apple += booty.apple
            print ('🍎 : {}'.format(player.apple))
            booty.destroy()
            bootys.remove(booty)
    # Update window
    wn.update()
