
# 121CAT

3. Create a video of the app working with all of the additional features. Make the video small enough to render here or upload to a video service witha aviawable link.

4. Choose two snapshots of code that demonstrate the algorithm(s) used to implement the additional features. Explain the code in the screenshots.

## First Code Snapshot

def stamp(self, turtle):
        original_color = turtle.fillcolor()  
        new_color = rand.choice(colors)  
        turtle.fillcolor(new_color)  
        turtle.stamp() 
        turtle.fillcolor(original_color)  

## How does this work? 
This stamp() function temporarily changes the color of a turtle shapes, creates a visual stamp (copy) of it, and then changes back to the original color. First, I stored the current fill color by using the original_color to fill the turtle. Then, it selects a new random color from the colors list (that I created in the initialization part of the code) and applies that color. After that it uses turtle.stamp() to create a stamp of the turtle’s shape. Finally, the function resets the turtle’s fill color back to the original. This function got initiated in the update_score_for_spot and the update_score_for_box functions because it needed to stamp whenever a shape was clicked, which is when the update_score functions were activated aswell, so I put it into there. 


## Second Code Snapshot











## How does this work?



