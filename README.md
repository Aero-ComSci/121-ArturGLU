
# 121CAT

## Video Link: 


## Additional Features

### First Code Snapshot

![Screenshot 2024-10-25 145113](https://github.com/user-attachments/assets/5275bd5c-3ac7-4eab-9ff2-1d66ca4cafd3)

![Screenshot 2024-10-25 145049](https://github.com/user-attachments/assets/edb8517e-fbe9-4191-bf6f-74f1c9863180)

### How does this work? 
The `stamp()` function temporarily changes the color of a turtle shape, creates a visual stamp (copy) of it, and then changes back to the original color. First, I stored the current fill color by using the `original_color` to fill the turtle. Then, it selects a new random color from the `colors` list (that I created in the initialization part of the code) and applies that color. After that, it uses `turtle.stamp()` to create a stamp of the turtle’s shape. Finally, the function resets the turtle’s fill color back to the original. 

This function got initiated in the `update_score_for_spot` and the `update_score_for_box` functions because it needed to stamp whenever a shape was clicked, which is when the update_score functions were activated as well, so I put it into there. This function is cool because not only does it add difficulty to the game by overwhelming the user with all the additional colorful shapes, but it also creates a cool image by the time the timer runs out (assuming that you clicked the shapes many times).

### Second Code Snapshot

![Screenshot 2024-10-25 145124](https://github.com/user-attachments/assets/705db23b-194e-4b74-aa98-b43adb3d0774)

![Screenshot 2024-10-25 145056](https://github.com/user-attachments/assets/1aa95e00-4906-4d47-92f7-90cf2d5ac441)

### How does this work?
The `change_size()` function modifies the size of the shape every time it gets clicked by randomly selecting a new size from the `sizes` list (which was added earlier in the initialization of the code). The sizes range from as small as 0.5, all the way to 3, the size that it begins with. It uses `turtle.shapesize(new_size)` to apply this new size to the turtle. 

This function is cool because it adds variability and more difficulty to the game as the turtles can appear larger or smaller with each interaction, and smaller turtles are harder to click.




