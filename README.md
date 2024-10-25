
# 121CAT

# Additional Features

## First Code Snapshot

def stamp(self, turtle):
        original_color = turtle.fillcolor()  
        new_color = rand.choice(colors)  
        turtle.fillcolor(new_color)  
        turtle.stamp() 
        turtle.fillcolor(original_color)  

## How does this work? 
This stamp() function temporarily changes the color of a turtle shapes, creates a visual stamp (copy) of it, and then changes back to the original color. First, I stored the current fill color by using the original_color to fill the turtle. Then, it selects a new random color from the colors list (that I created in the initialization part of the code) and applies that color. After that, it uses turtle.stamp() to create a stamp of the turtle’s shape. Finally, the function resets the turtle’s fill color back to the original. This function got initiated in the update_score_for_spot and the update_score_for_box functions because it needed to stamp whenever a shape was clicked, which is when the update_score functions were activated as well, so I put it into there. This function is cool because not only does it add difficulty to the game by overwhelming the user with all the additional colorful shapes, but it also creates a cool image by the time the timer runs out (assuming that you clicked the shapes many times).


## Second Code Snapshot

def change_size(self, turtle):
        new_size = rand.choice(sizes) 
        turtle.shapesize(new_size)  


## How does this work?
This change_size() function modifies the size of the shape every time it gets clicked by randomly selecting a new size from the sizes list (which was added earlier in initialization of the code). The sizes range from as small as 0.5, all the way to 3, the size that it begins with. It uses turtle.shapesize(new_size) to apply this new size to the turtle. This function is cool because it adds variability and more difficulty to the game as the turtles can appear larger or smaller with each interaction, and smaller turtles are harder to click. 



