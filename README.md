
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
This was the stamp function which left a copy of the shape (spot or box) every time that it got moved to another position. 



