import turtle as t
import random as rand

score = 0

t.bgcolor("lightblue")

font_setup = ("Arial", 20, "normal")

timer = 5
counter_interval = 1000   
timer_up = False

colors = ["blue", "red", "green", "yellow", "purple", "orange"]

#-----game configuration----
class Game: 
    def __init__(self):
        self.spot = t.Turtle()
        self.spot.shape("circle")
        self.spot.shapesize(3)
        self.spot.fillcolor("blue")  
        self.spot.penup()
        self.spot.goto(-100, 0)

        self.box = t.Turtle()
        self.box.shape("square")
        self.box.shapesize(3)
        self.box.fillcolor("green") 
        self.box.penup()
        self.box.goto(100, 0)

        self.spot.onclick(self.update_score_for_spot)
        self.box.onclick(self.update_score_for_box)

        self.score_writer = t.Turtle()
        self.score_writer.penup()
        self.score_writer.goto(0, 300)

        self.counter = t.Turtle()
        self.counter.penup()
        self.counter.goto(-300, 300)

        self.countdown()

    def change_color_and_stamp(self, turtle):
        original_color = turtle.fillcolor()  
        new_color = rand.choice(colors)  
        turtle.fillcolor(new_color)  
        turtle.stamp() 
        turtle.fillcolor(original_color)  

    #-----game functions-----
    def countdown(self):
        global timer, timer_up
        self.counter.clear()
        if timer <= 0:
            self.counter.write("Time's Up", font=font_setup)
            timer_up = True
            self.end_game()  
        else:
            self.counter.write("Timer: " + str(timer), font=font_setup)
            timer -= 1
            t.ontimer(self.countdown, counter_interval)

    def change_position(self, turtle):
        new_xpos = rand.randint(-200, 200)
        new_ypos = rand.randint(-200, 200)
        turtle.goto(new_xpos, new_ypos)

    def update_score_for_spot(self, x, y):
        global score, timer_up
        if timer_up:
            return  
        score += 1
        print("Score:", score)
        self.change_color_and_stamp(self.spot) 
        self.change_position(self.spot)  
        self.score_writer.clear()
        self.score_writer.write(score, font=font_setup)

    def update_score_for_box(self, x, y):
        global score, timer_up
        if timer_up:
            return  
        score += 1
        print("Score:", score)
        self.change_color_and_stamp(self.box)  #
        self.change_position(self.box) 
        self.score_writer.clear()
        self.score_writer.write(score, font=font_setup)

    def end_game(self):
        self.spot.hideturtle() 
        self.box.hideturtle()   
        self.score_writer.clear()
        self.score_writer.goto(0, 0)
        self.score_writer.write(f"Final Score: {score}", align="center", font=font_setup)

#-----events----------------
def main():
    global wn
    wn = t.Screen()
    game = Game()
    wn.mainloop()

main()
