# Turtle Code-Along
In this introductory activity, use [turtle graphics](https://en.wikipedia.org/wiki/Turtle_graphics) to create a drawing in Python!

![](https://upload.wikimedia.org/wikipedia/commons/f/f9/Emoji_u1f422.svg)

## Getting Started
Setup using **repl.it** is fairly simple.

1. Go to the [TurtleStart](https://repl.it/@JosephMaxwell/TurtleStart#main.py) repl.it project
1. Fork the project, and make sure to log in!
1. In the code section, add the following line to _import_ everything from the **turtle** library:
    ```py
    from turtle import *
    ```
1. Click the green Run button, and notice that nothing happens yet
1. Make a new line under the `import`, and add the following code:
    ```py
    shelly = Turtle()
    ```
1. `shelly` is now a `Turtle` object - but Shelly needs a shape! Under that line, add the following code to give Shelly a shape:
    ```py
    shelly.shape("arrow")
1. Run the code again to see Shelly appear on the screen!
1. BONUS: Update the code so that instead of an "arrow" shape, the turtle looks like a turtle

### Code
```py
from turtle import *

shelly = Turtle()
shelly.shape("arrow")
```

## Adding Color
Make things a little more interesting by updating the colors.

1. Make a new line, and add code to change Shelly's color
    - HINT: this is a lot like how the `shape` was updated - just using `color` instead
1. On the next line, add the following code:
    ```py
    paper = shelly.getscreen()
    ```
1. Now, the `paper` variable stores the screen. Change its color using `bgcolor`
1. BONUS: Play around with the settings to create a pleasing (or terrible) color scheme!

### Code
```py
shelly.color("maroon")
paper = shelly.getscreen()
paper.bgcolor("gold")
```

### More Colors
Although there are many built-in colors, sometimes it is necessary to find a very specific color. In addition to using color names (like "red", "orange", etc), turtles can take color values in RGB format! The [RGB color model](https://en.wikipedia.org/wiki/RGB_color_model) is an additive color model in which red, green and blue light are added together in various ways to reproduce a broad array of colors. Basically, it is possible to create any digital color with a combination of red, green, and blue!

Each color (R, G, and B) can take a number from 0 to 255. This represents the amount of the color in the mix. For example, a color with a Red value of 255, a Green value of 0, and a Blue value of 0 would be red.

Try to guess how the following colors would look:
- Red 255, Green 0, Blue 255
- Red 255, Green 255, Blue 0
- Red 0, Green 0, Blue 255
- Red 255, Green 255, Blue 255
- Red 0, Green 0, Blue 0
- Red 255, Green 128, Blue 0

The combinations are almost endless! Google has a [built-in color picker](https://www.google.com/search?q=color+picker) that developers and designers can utilize to find the perfect color. It displays RGB colors in this format:
```
rgb(92, 144, 66)
```

To translate that into Python code, do the following:
```py
shelly.color(92, 144, 66)
```

This will set the color of the turtle to a dark green. The RGB method allows for much more specific colors, so developers can use precisely the color they need!

## Moving the Turtle
One of the most useful turtle abilities is the ability to move across the screen and draw like a pen! Create a blank line, and then add the following command on the next line:

```python
shelly.forward(50)
```

Click the Run button to see the turtle move across the screen! Specifically, it moves **forward** `50` pixels in the direction it is currently facing (90 degrees).

It is also possible to turn the turtle. Add the following command on the next line:
```python
shelly.right(90)
```

This command turns the turtle `90` degrees to the **right**. Previously the direction of the turtle was 90 degrees (pointing to the right), so after turning 90 degrees to the right, the turtle should face down (180 degrees).

Run the program again to see the turtle move to the right, then turn to face down!

### Drawing a Square
Add the following commands to the file, under the existing commands:
```python
shelly.forward(50)
shelly.right(90)
shelly.forward(50)
shelly.right(90)
```

Run the program to see what this code does. It should draw part of a square! How does that work? On a piece of paper, or on a whiteboard, try to draw the same square as the turtle:

1. Draw the top side from left to right
1. Turn the writing utensil and draw the right side from top to bottom
1. Turn the writing utensil and draw the bottom side from left to right

So, the turtle moves `50` pixels to the right, turns `90` degrees to face down, moves `50` pixels down, turns `90` degrees to face left, moves `50` pixels to the left, and then turns `90` degrees to face up!

### BONUS
Try to complete the square that Shelly is drawing.

## Another Turtle
Under the existing code, add code to make a new turtle:

```py
crush = Turtle()
crush.shape("turtle")
crush.color("white")
```

This new turtle will be completely separate from the other one. Instead of drawing a square, it will draw a circle.

Add the following code to draw a half circle:
```py
crush.circle(50, 180)
```

In the example, the radius of the circle will be `50`, and it will complete a `180` degree rotation. BONUS: instead of a half circle, draw a full circle!

### A New Starting Point
Currently, the two turtles are kind of on top of each other. Fix this by adding a new starting point for the `crush` turtle.

_Before_ the commands that make crush draw the circle, add the following command:
```python
crush.setpos(-100, 100)
```

Run the program to see what happens. Crush moves, but there is another issue now!

#### Removing the Extra Pen Marks
When Crush moves to the starting point, the pen draws an extra line! Instead of doing this, the program should lift up the pen before this movement.

When working with turtles, it is possible to control whether the pen is "up" or "down" (like real life drawing). _Before_ the `crush.setpos` command, add the following command:
```python
crush.penup()
```

This will allow Crush to move without drawing anything! Run the program to see what happens.

#### Putting the Pen Back Down
Oh no! After lifting up the pen, Crush no longer draws the triangle! Fix this by adding the following command _after_ the `crush.setpos` command:
```python
crush.pendown()
```

This way, Crush will pick up the pen when moving to the starting point, and then put it back down before moving in the triangular fashion. Run the program again to see it work properly!

## Other Possibilities
This only scratches the surface of turtle graphics capabilities. Try to play around with these commands, and check out the [documentation](https://docs.python.org/3/library/turtle.html) to see what else is possible!

## Final Code
```py
from turtle import *

shelly = Turtle()
shelly.shape("arrow")

shelly.color("gold")
paper = shelly.getscreen()
paper.bgcolor("maroon")

shelly.forward(50)
shelly.right(90)
shelly.forward(50)
shelly.right(90)
shelly.forward(50)
shelly.right(90)

crush = Turtle()
crush.shape("turtle")
crush.color("white")

crush.penup()
crush.setpos(-100, 100)
crush.pendown()

crush.circle(50, 180)
```

## Challenges
After the activity, start working on the [Turtle Challenges](TurtleChallenges.md).