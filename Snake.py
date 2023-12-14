import turtle, random

class Game:
    '''
    Purpose: 
        Implementing the game
    Instance variables: 
        player: A Snake object representing the snake controlled by the player
        food: A Food object for the snake to eat
        speed: the speed of the snake, the larger the number is, the slower the snake is
    Methods:
        gameloop: if the game is ongoing, move the snake continuosly, if the game is over, 
                    stop the snake and print 'Game Over' on the screen
        speed1: set the instance variable speed to a value of 200
        speed2: set the speed instance variable to a value of 100
        speed3: set the speed instance variable to a value of 1000
        reset: if the game is over, clear the screen and reset the game if called
    '''

    def __init__(self):
        #Setup 700x700 pixel window
        turtle.setup(700, 700)

        #Bottom left of screen is (-40, -40), top right is (640, 640)
        turtle.setworldcoordinates(-40, -40, 640, 640)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)

        #Draw the board as a square from (0,0) to (600,600)
        for i in range(4):
            turtle.forward(600)
            turtle.left(90)
        
        self.player = Snake(315 ,315, 'green')
        self.food = Food('Red')
        self.speed = 200
        self.gameloop()
        turtle.onkeypress(self.player.go_down, 'Down')
        turtle.onkeypress(self.player.go_up, 'Up')
        turtle.onkeypress(self.player.go_right, 'Right')
        turtle.onkeypress(self.player.go_left, 'Left')
        turtle.onkeypress(self.speed1, '1')
        turtle.onkeypress(self.speed2, '2')
        turtle.onkeypress(self.speed3, '3')
        turtle.onkeypress(self.reset,'r')
        turtle.listen()
        turtle.mainloop()

    def gameloop(self):
        if self.player.game_over() == False:
            self.player.move(self.food)
            turtle.ontimer(self.gameloop, self.speed)
        else:
            turtle.penup()
            turtle.setpos(300,300)
            turtle.write('Game Over',align='center', font=('Arial',50,'normal'))
    def speed1(self):
        self.speed = 200
    def speed2(self):
        self.speed = 100
    def speed3(self):
        self.speed = 1000
    def reset(self):
        if self.player.game_over() == True:
            turtle.clearscreen()
            turtle.reset()
            Game()
        
class Snake:
    '''
    Purpose:
        Representing the snake
    Instance variables:
        x/y: the x/y position
        vx/vy: the x/y velocity
        color: the color of the snake
        segments: a list of Snake object representing every segment of the snake
    Method:
        grow:
            To add a segment to the snake
        move:
            move the snake, if running in to food, add a segment to the snake
        go_down:
            change the moving direction of the snake to going down
        go_up:
            change the moving direction of the snake to going up
        go_right:
            change the moving direction of the snake to going right
        go_left:
            change the moving direction of the snake to going left
        game_over:
            check if the snake has run into the bound or itself
    '''
    def __init__(self, x, y, color):
        self.x = x 
        self.y = y
        self.vx = 30
        self.vy = 0
        self.color = color
        self.segments = []
        self.grow()
    def grow(self):
        head = turtle.Turtle()
        head.speed(0)
        head.fillcolor(self.color)
        head.shape("square")
        head.shapesize(1.5, 1.5)
        head.penup()
        head.setpos(self.x,self.y)
        self.segments.append(head)
    def move(self,food):
        self.x += self.vx
        self.y += self.vy
        if self.x == food.x and self.y == food.y:
            food.move()
            self.grow()
        else:
            for i in range(len(self.segments)-1):
                self.segments[i].setpos(self.segments[i+1].xcor(),self.segments[i+1].ycor())
            self.segments[-1].setpos(self.x,self.y)
    def go_down(self):
        self.vx = 0
        self.vy = -30
    def go_up(self):
        self.vx = 0
        self.vy = 30
    def go_right(self):
        self.vx = 30
        self.vy = 0
    def go_left(self):
        self.vx = -30
        self.vy = 0
    def game_over(self):
        clash = False
        for j in range(len(self.segments)-1):
            if self.segments[-1].xcor() == self.segments[j].xcor() and self.segments[-1].ycor() == self.segments[j].ycor():
                clash = True
        if self.x < 0 or self.x > 600 or self.y < 0 or self.y > 600 or clash == True:
            return True
        else:
            return False

class Food:
    '''
    Purpose:
        Representing the food
    Instance variables:
        color: the color of the food
        pellet: a turtle object representing the food
    Method:
        move: randomly move the food to a spot in the screen
    '''
    def __init__(self,color):
        self.color = color
        food = turtle.Turtle()
        food.speed(0)
        food.fillcolor(self.color)
        food.shape("circle")
        food.shapesize(1.5, 1.5)
        food.penup()
        self.pellet = food
        self.move()
    def move(self):
        self.x = 15 + 30*random.randint(0,19)
        self.y = 15 + 30*random.randint(0,19)
        self.pellet.setpos(self.x,self.y)
        
    

Game()

