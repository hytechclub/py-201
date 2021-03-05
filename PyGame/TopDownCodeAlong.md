# Building a Top-Down Game with Pygame
In this activity, build a rudimentary top-down game using [Pygame](https://www.pygame.org/). In the game, the main character will have to pick up a key to open a door. While this game may be quite simple, it should illustrate some what's possible with Pygame.

## Setting Up
Get ready to go with a starter project.

1. Go to this [Starter Repl Project](https://repl.it/@HylandOutreach/Top-Down-Game#main.py)
1. Click the "Fork" button
1. Log into Repl if necessary
1. Open the **main.py** file

Nothing should happen just yet.

## Pygame Hello World
To kick things off, start writing some basic Pygame code. At the very top of the file, add the first necessary command:

```py
import pygame
```

This will allow the program to use the `pygame` library.

### Constants
>Note that [Python does not actually have constants](https://stackoverflow.com/a/2682752), but developers can still treat variables as constants

Under the `import` statement, it's time to create some basic game "constants." The top-down game will be [tile-based](https://en.wikipedia.org/wiki/Tile-based_video_game); rather than working pixel-by-pixel, everything will be placed on a tile map. All coordinates in the game will be based on their _tile location_, not their pixel location. Set the `TILE_SIZE`, `WIN_WIDTH`, and `WIN_HEIGHT` variables like so:

```py
TILE_SIZE = 32
WIN_WIDTH = TILE_SIZE * 10
WIN_HEIGHT = TILE_SIZE * 10
```

The existing image assets are 32x32 pixels, so the tile size must be 32. The window width and height should be set based on the tile size.

In addition to the size values, create a variable for the color white:

```py
WHITE = (255, 255, 255)
```

This will be used to fill the background of the game. It is declared as a [tuple](https://www.w3schools.com/python/python_tuples.asp) with three values: one for Red, one for Green, and one for Blue ([RGB](https://en.wikipedia.org/wiki/RGB_color_model)). Feel free to update the color if desired.

### Creating the Window
Now that some constants have been defined, it's time to create the window! The first thing to do is call [`init` function](https://www.pygame.org/docs/ref/pygame.html#pygame.init) from the `pygame` library:

```py
pygame.init()
```

This initializes all imported pygame modules. Next, it will be necessary to set up the surface on which the game will be played. On the next line, create a new variable named `display_surface`, and set it like so:

```py
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
```

It calls the `pygame.display.set_mode` function, and passes in the window width and height as a two-element tuple. The `display_surface` variable will be used to draw things to the screen.

Now that the window has a size, it needs a caption. On the next line, add the following command:

```py
pygame.display.set_caption('Top Down')
```

This will set the window's title. Feel free to change the name from `Top Down` to anything else.

### The Game Loop
Now some initial values are set, and the window has been configured. All that's left to make it display is to create the [game loop](https://gameprogrammingpatterns.com/game-loop.html). This will be a simple `while True` that renders and updates the game.

Start with the `while` loop structure:

```py
while True:
```

In the _body_ of the loop, call the `display_surface.fill` function and pass in the `WHITE` variable as an argument:

```py
display_surface.fill(WHITE)
```

Under that, still in the body of the loop, make a couple of new lines and call the `pygame.display.update` function:

```py
pygame.display.update()
```

This loop will constantly keep the background filled white, and continuously display the window.

```py
while True:
  display_surface.fill(WHITE)

  pygame.display.update()
```

### Structural Note
A lot of the code in the **main.py** file will be spread out in different places. Rather than writing code from the top of the file to the bottom, some parts will make sense to place at the top and some will make more sense at the bottom. Generally, the `while` game loop will always be at the bottom of the file, while variable declarations, configuration, and function definitions will happen toward the top.

## Main Character Sprite
In most games, the most important piece is the main character - the player needs to have something to control. Start by creating a main character sprite and drawing it to the screen.

### The `main_sprite` Dictionary
Sprites can be represented as Dictionaries, with all important information grouped together.

1. Above the `while` loop, create a new variable named `main_sprite`
1. Set the `main_sprite` variable to a new dictionary
1. Add a key of `'img'` to the dictionary
1. Set the `'img'` value to `pygame.image.load('main.png')`
    - This will load in the **main.png** file as an image
1. Add a key of `'x'` and set it to `4`
1. Add a key of `'y'` and set it to `9`
    - These coordinates will by _tile coordinates_ rather than pixel coordinates

The dictionary should look something like this:

```py
main_sprite = {
  'img': pygame.image.load('main.png'),
  'x': 4,
  'y': 9
}
```

### Drawing the `main_sprite`
Now that the data is there for the main sprite, it's time to draw it. This will take place within the `while` game loop, so start by finding the body of the loop - make a new line _under_ the `display_surface.fill` and _above_ the `pygame.display.update`, and follow the steps below.

1. Create a new variable named `main_pos`
1. Set the `main_pos` variable to a new tuple (using parentheses)
1. For the first value of the tuple, set it to `main_sprite['x']*TILE_SIZE`
    - This will translate the `x` _tile coordinate_ to its _pixel coordinate_
1. For the second value of the tuple, set it to `main_sprite['y']*TILE_SIZE`
    - This is the same thing but for the `y` coordinate
1. Under the `main_pos` variable, call the `display_surface.blit` function
    - For the first argument, pass in `main_sprite['img']`
    - For the second argument, pass in `main_pos`
1. Run the program, and verify that the main sprite appears in the game!

The new code within the body of the `while` loop should look something like this:

```py
main_pos = (main_sprite['x']*TILE_SIZE, main_sprite['y']*TILE_SIZE)
display_surface.blit(main_sprite['img'], main_pos)
```

## Door Sprite
Ultimately, the goal of the game will be for the main character to reach a **door**. Add a door sprite to make that possible!

### The `door_sprite` Dictionary
The `door_sprite` dictionary will be very similar to the `main_sprite`, just with a different name, a different image, and different coordinates.

1. Under the `main_sprite` variable, create a new variable named `door_sprite`
1. Set the `door_sprite` variable to a new dictionary
1. Add a key of `'img'` to the dictionary
1. Set the `'img'` value to `pygame.image.load('door.png')`
1. Add a key of `'x'` and set it to `4`
1. Add a key of `'y'` and set it to `0`

The dictionary should look something like this:

```py
door_sprite = {
  'img': pygame.image.load('door.png'),
  'x': 4,
  'y': 0
}
```

### Defining the `draw_sprite` Function
Similar to the `main_sprite`, it will be necessary to draw the `door_sprite` to the screen. However, rather than copying the code, this would be a good place to define a new function. The function should do what the drawing code does for the `main_sprite`, but more generalized.

In the **main.py** file, _under_ the constants and _above_ the initialization code, make some new lines. Then, follow the steps below.

1. Define a new function named `draw_sprite`
    - It should take in one parameter - `sprite`
1. In the body of the `draw_sprite` function, declare a new variable named `position`
1. Set the `position` variable to a new tuple
1. Set the first value of the tuple to `sprite['x']*TILE_SIZE`
1. Set the second value of the tuple to `sprite['y']*TILE_SIZE`
1. Under the `position` variable, call the `display_surface.blit` function
    - Pass in `sprite['img']` as the first argument
    - Pass in `position` as the second argument

The function code should look something like this: 

```py
def draw_sprite(sprite):
  position = (sprite['x']*TILE_SIZE, sprite['y']*TILE_SIZE)
  display_surface.blit(sprite['img'], position)
```

### Calling the `draw_sprite` Function
The function has been defined, but it will not do anything until it is called! In the body of the `while` game loop, call the `draw_sprite` function for both the `main_sprite` and the `door_sprite`. Remove the code that previously drew the `main_sprite`. Run the program, and verify that the door appears in the game!

The code should look something like this:

```py
draw_sprite(main_sprite)
draw_sprite(door_sprite)
```

## Movement
Now the door is there, and the main character is there, but the main character needs a way to reach the door. The game should handle input from the user, so that if they press any of the arrow keys, the player will move in the proper direction.

At the top of the file, right under the `import`, add the following command:

```py
from pygame.locals import *
```

This will allow the code to leverage the event constants for key presses. It imports the following constants (among others):

```py
KEYDOWN # General Key-down event

K_LEFT # Left Key press
K_RIGHT # Right Key press
K_UP # Up Key press
K_DOWN # Down Key press
```

### Defining the `move_sprite` Function
Before handling the input itself, create a way to update the position of a sprite based on a key press. Find the `draw_sprite` function definition, and make some space beneath it for the new function.

1. Define a new function named `move_sprite`
    - It should take two parameters - `sprite` and `event_key`
1. In the body of the `move_sprite` function, add an `if` statement
1. For the `if` condition, check if `event_key == K_LEFT`
    - This indicates that the left key has been pressed
1. In the body of the `if` statement, add `sprite['x'] -= 1`
    - This will change the `x` coordinate by -1, moving the sprite left
1. Create `elif` statements for each additional key
    - `K_RIGHT` - increment `x` coordinate by 1
    - `K_UP` - decrement `y` coordinate by 1
    - `K_DOWN` - increment `y` coordinate by 1

The code for the `move_sprite` function definition should look something like this:

```py
def move_sprite(sprite, event_key):
  if event_key == K_LEFT:
    sprite['x'] -= 1
  elif event_key == K_RIGHT:
    sprite['x'] += 1
  elif event_key == K_UP:
    sprite['y'] -= 1
  elif event_key == K_DOWN:
    sprite['y'] += 1
```

### Getting the Input Event
Now the program can move a sprite, but it needs to know when a key is pressed. Find the body of the `while` game loop, and make some space under the `draw_sprite` function calls. Then, follow the steps below to loop through all events, figure out if a key is pressed, and call the `move_sprite` function if necessary.

1. Create a `for` loop
    - For the item, name it `event`
    - For the collection, use `pygame.event.get()`
1. In the body of the `for` loop, create an `if` statement
1. In the `if` condition, check if `event.type == KEYDOWN`
1. In the body of the `if` statement, call the `move_sprite` function
    - Pass in `main_sprite` as the first argument
    - Pass in `event.key` as the second argument
1. Run the program, and verify that it is possible to move the main character with arrow keys!

The additional code within the `while` game loop body should look something like this:

```py
for event in pygame.event.get():
  if event.type == KEYDOWN:
    move_sprite(main_sprite, event.key)
```

## Victory
Now it is possible to move the main character to the door, but - nothing happens. Update the code so that, when the main character overlaps with the door, the game ends in victory!

### A New Color
When the game ends in victory, the background should change to green. Add a new `GREEN` constant to represent this color as a three-value tuple, right under the `WHITE` variable declaration:

```py
GREEN = (0, 255, 0)
```

### A Font Setup
When the game ends, it will also be necessary to display a message. To do this, the code needs a font. Under the existing initialization code, make some space, and add the following code:

```py
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)
```

These two lines initialize the font library, and create a new `font` variable with the given font and size.

### The `overlap` Function
The program also needs a way to tell if two sprites overlap - if one is on top of the other. Define a new function to check for this.

1. Under the `move_sprite` function definition, make some space
1. Define a new function named `overlap`
    - It should take in two parameters - `sprite1` and `sprite2`
1. In the body of the `overlap` function, create a new variable named `x_overlap`
1. Set the `x_overlap` variable to `sprite1['x'] == sprite2['x']`
    - This checks if both sprites have the same `x` coordinate
1. Set the `y_overlap` variable to `sprite1['y'] == sprite2['y']`
    - This checks if both sprites have the same `y` coordinate
1. Add a `return` statement, and return `x_overlap and y_overlap`
    - This checks that they are on the exact same tile

The code for the `overlap` function should look something like this:

```py
def overlap(sprite1, sprite2):
  x_overlap = sprite1['x'] == sprite2['x']
  y_overlap = sprite1['y'] == sprite2['y']
  return x_overlap and y_overlap
```

### The `draw_end_text` Function
The program also needs a way to display the final message when the game ends. Define a new function that makes this possible.

1. Under the `overlap` function definition, make some space
1. Define a new function named `draw_end_text`
    - It should take in two parameters - `text` and `bg_color`
1. In the body of the `draw_end_text` function, call the `display_surface.fill` function
    - Pass in the `bg_color` parameter
1. Under that, create a new variable named `text_surface`
1. Set the `text_surface` variable to `font.render(text, False, (0, 0, 0))`
    - This creates the text with the font and passed in message
1. On the next line, call the `display_surface.blit` function
    - Pass in `text_surface` as the first argument
    - Pass in `(120, 140)` for the second argument (this is the location on the screen)

The code for the `draw_end_text` function should look something like this:

```py
def draw_end_text(text, bg_color):
  display_surface.fill(bg_color)
  text_surface = font.render(text, False, (0, 0, 0))
  display_surface.blit(text_surface, (120, 140))
```

### The `game_status` Variable
One other thing that is typically important in a game is **state**. So far, this game should have two states: `'Playing'` and `'Win'`. Create the `game_status` variable, set it appropriately, and change the game output based on the value.

1. Right above the `while` loop, create a new variable named `game_status`
    - Set it to `'Playing'`
1. In the body of the `while` loop, above the `for` loop, create an `if` statement
1. In the condition for the `if`, check if `game_status == 'Win'`
1. In the body of the `if`, call the `draw_end_text` function
    - Pass in `'You Win'` as the first argument
    - Pass in `GREEN` as the second argument
1. Under the `for` loop, create an `if` statement
1. In the condition for the `if`, call the `overlap` function
    - Pass in `main_sprite` as the first argument
    - Pass in `door_sprite` as the second argument
1. In the body of the `if`, set the `game_status` variable to `'Win'`
1. Run the code, and verify that it is possible to win the game upon reaching the door!

The code for the `while` loop should look something like this:

```py
game_status = 'Playing'

while True:
  display_surface.fill(WHITE)
  
  draw_sprite(main_sprite)
  draw_sprite(door_sprite)

  if game_status == 'Win':
    draw_end_text('You Win', GREEN)

  for event in pygame.event.get():
    if event.type == KEYDOWN:
      move_sprite(main_sprite, event.key)

  if overlap(main_sprite, door_sprite):
    game_status = 'Win'

  pygame.display.update()
```

## Defeat
Now it is possible to win, but the game is pretty boring. The player should not be able to simply walk right through the door. Update the game so that if they try to walk through the door without a key, they lose.

### Checking for Defeat
If the `game_status` is `'Lose'`, the game should change the background to red, and display "You Died" text.

1. Under the `GREEN` variable declaration, create a new variable named `RED`
1. Set the `RED` variable to `(255, 0, 0)`
1. In the body of the `while` loop, find the `if game_status == 'Win'` statement
1. Under that, add an `elif` clause
1. In the condition for the `elif`, check if `game_status == 'Lose'`
1. In the body of the `elif`, call the `draw_end_text` function
    - Pass in `'You Died'` as the first argument
    - Pass in `RED` as the second argument

### Setting the `game_status`
Next, properly set the `game_status` variable based on whether the player has a key or not.

1. Above the `game_status` variable declaration, create a new variable named `got_key`
1. Set the `got_key` variable to `False`
1. In the body of the `while` loop, find the `if overlap(main_sprite, door_sprite)` statement
1. In the body of that `if`, remove the existing code
1. Create a new `if` in the body of the `if` statement
1. For the `if` condition, check for `got_key`
1. In the body of the `if got_key:` statement, set the `game_status` to `'Win'`
1. Create an `else` on the `if got_key:` statement
1. In the body of that `else`, set the `game_status` to `'Lose'`
1. Run the program, and verify that the game ends in defeat if the player reaches the door!

The code for the `while` loop should look something like this:

```py
got_key = False
game_status = 'Playing'

while True:
  display_surface.fill(WHITE)

  draw_sprite(main_sprite)
  draw_sprite(door_sprite)

  if game_status == 'Win':
    draw_end_text('You Win', GREEN)
  elif game_status == 'Lose':
    draw_end_text('You Died', RED)

  for event in pygame.event.get():
    if event.type == KEYDOWN and game_status == 'Playing':
      move_sprite(main_sprite, event.key)

  if overlap(main_sprite, door_sprite):
    if got_key:
      game_status = 'Win'
    else:
      game_status = 'Lose'

  pygame.display.update()
```

## The Key
Now it is possible to lose the game, but it is no longer possible to win it! The main character should be able to pick up a key before going through the door. Create a new key sprite, and let the player pick it up.

### The `key_sprite` Dictionary
Creating the `key_sprite` dictionary will be very similar to creating the other sprite dictionaries.

1. Under the `door_sprite` variable, create a new variable named `key_sprite`
1. Set the `key_sprite` variable to a new dictionary
1. Add a key of `'img'` to the dictionary
1. Set the `'img'` value to `pygame.image.load('key.png')`
1. Add a key of `'x'` and set it to `2`
1. Add a key of `'y'` and set it to `7`

The dictionary should look something like this:

```py
key_sprite = {
  'img': pygame.image.load('key.png'),
  'x': 2,
  'y': 7
}
```

### Showing the Key
Drawing the `key_sprite` will be very similar to drawing the other sprites as well. Luckily, the `draw_sprite` function handles that entirely.

1. Find the calls to `draw_sprite` within the `while` loop body
1. Make a couple new lines
1. Call the `draw_sprite` function again
1. Pass in `key_sprite` as the argument
1. Run the program, and verify that the sprite appears!

The code should look something like this:

```py
draw_sprite(key_sprite)
```

### Picking Up the Key
Next, the player should be able to pick up the key. This should happen if the main character sprite _overlaps_ with the key sprite. When that happens, the `got_key` variable should be set to `True`.

1. Find the existing  `if overlap` call within the `while` loop body
1. Under that, create another `if` statement
1. In the condition for the `if`, call the `overlap` function
    - Pass in `main_sprite` as the first argument
    - Pass in `key_sprite` as the second argument
1. In the body of the `if`, set the `got_key` variable to `True`
1. Run the program, and verify that it is possible to pick up the key, open the door, and win the game!

The code should look something like this:

```py
if overlap(main_sprite, key_sprite):
  got_key = True
```

### Making the Key Disappear
There is one last issue with the game; when the player "picks up" the key, it does not disappear. This is fixable with another `if` statement.

1. Find the `draw_sprite(key_sprite)` call in the `while` loop body
1. Remove that line, and add an `if` instead
1. In the condition for the `if`, check if `not got_key`
    - This means the body will only execute if `got_key` is `False`
1. In the body of the `if`, call the `draw_sprite` function
    - Pass in `key_sprite` as the argument
1. Run the program again, and verify that the key disappears when it should!

The code should look something like this:

```py
if not got_key:
  draw_sprite(key_sprite)
```

## Final Code
The final code for the game should look something like this:

```py
import pygame
from pygame.locals import *

TILE_SIZE = 32
WIN_WIDTH = TILE_SIZE * 10
WIN_HEIGHT = TILE_SIZE * 10

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def draw_sprite(sprite):
  position = (sprite['x']*TILE_SIZE, sprite['y']*TILE_SIZE)
  display_surface.blit(sprite['img'], position)

def move_sprite(sprite, event_key):
  if event_key == K_LEFT:
    sprite['x'] -= 1
  elif event_key == K_RIGHT:
    sprite['x'] += 1
  elif event_key == K_UP:
    sprite['y'] -= 1
  elif event_key == K_DOWN:
    sprite['y'] += 1

def overlap(sprite1, sprite2):
  x_overlap = sprite1['x'] == sprite2['x']
  y_overlap = sprite1['y'] == sprite2['y']
  return x_overlap and y_overlap

def draw_end_text(text, bg_color):
  display_surface.fill(bg_color)
  text_surface = font.render(text, False, (0, 0, 0))
  display_surface.blit(text_surface, (120, 140))

pygame.init()
display_surface = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Game')

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 30)

main_sprite = {
  'img': pygame.image.load('main.png'),
  'x': 4,
  'y': 9
}

door_sprite = {
  'img': pygame.image.load('door.png'),
  'x': 4,
  'y': 0
}

key_sprite = {
  'img': pygame.image.load('key.png'),
  'x': 2,
  'y': 7
}

got_key = False
game_status = 'Playing'

while True:
  display_surface.fill(WHITE)

  draw_sprite(main_sprite)
  draw_sprite(door_sprite)

  if not got_key:
    draw_sprite(key_sprite)

  if game_status == 'Win':
    draw_end_text('You Win', GREEN)
  elif game_status == 'Lose':
    draw_end_text('You Died', RED)

  for event in pygame.event.get():
    if event.type == KEYDOWN and game_status == 'Playing':
      move_sprite(main_sprite, event.key)

  if overlap(main_sprite, key_sprite):
    got_key = True

  if overlap(main_sprite, door_sprite):
    if got_key:
      game_status = 'Win'
    else:
      game_status = 'Lose'

  pygame.display.update()
```

## Next Steps
While this game is certainly simple, it does demonstrate some key features of the Pygame library. Using these features, it should be possible to create a much more interesting game! Visit the [Challenges page](PygameChallenges.md) for some ideas, or get creative and make anything else.