
  
## Dungeon Maze: Python Game
Dungeon Maze is a Python 3 application built using the turtle graphics library. Using keyboard keys, the player can navigate through the dungeon, collect apples, and exit to safety. Creating the player board was achieved by utilizing the Pen class from Turtle graphics, effectively drawing a space of 750x750px. Premade graphics were imported from Unity Engine free assets and assigned to classes respectively.

## Project Links
- [Video Demo](https://www.youtube.com/watch?v=OIvnrZcaZ5k&feature=youtu.be)
- [Code repository](https://github.com/neillsom/py-maze) 

## Screenshots
Dungeon maze:
![Dungeon maze](https://github.com/neillsom/py-maze/raw/master/resources/py-maze.jpg?raw=true "Dungeon maze")


## Tech / Frameworks used
<b>Built with</b>
- Python3
- Turtle graphics

## Code Examples
#### Create level setup function
```python
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
```

#### Code to register collisions
```python
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
```

## License
MIT License
Copyright (c) 2018 Neill Somerville

#### http://neillsomerville.com