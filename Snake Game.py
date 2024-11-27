import turtle
import time
import random

colors = ["red", "blue", "grey", "purple"]
delay = 0.1



#set up screen
wn = turtle.Screen()
wn.title("Snake Game by @Gary")
wn.bgcolor("green")
wn.setup(width=720, height=720)
wn.tracer(0) #turns off screen updates




#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


#Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


segments = []


#functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 40)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 40)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 40)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 40)
        
def go_up():
    head.direction = "up"
    
def go_down():
    head.direction = "down"
    
def go_left():
    head.direction = "left"
    
def go_right():
    head.direction = "right"
    
#keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
        
        
#Main game loop
while True:
    wn.update()
    
    #check for xollision with the border
    if head.xcor()>350 or head.xcor()<-350 or head.ycor()>350 or head.ycor()<-350:
        time.sleep(.05)
        head.goto(0, 0)
        head.direction = "stop"
        
        #hide the segments
        for segment in segments:
            segment.goto(10000, 10000)
            
        #clear the segments list
        segments.clear()
            
            
    
    
    
    #check for collision with the food
    if head.distance(food) < 40:
        #move food to random spot on screen
        x = random.randint(-325,325)
        y = random.randint(-325,325)
        food.goto(x,y)
    
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(random.choice(colors))
        new_segment.penup()
        segments.append(new_segment)
        
    #move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
        #move segment zero to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        
        
    move()      
    
    time.sleep(delay)
    
wn.mainloop()

