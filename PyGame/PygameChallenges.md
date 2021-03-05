# Pygame Challenges
Work on the challenges below, or come up with something entirely different! Use the [Top-down Code-Along gmae](TopDownCodeAlong.md) as a starting point.

## Starter Challenges
Start by working on these challenges to practice using Pygame.

### 1. Change the Starting Position for the Main Character
Update the `x` and `y` coordinate of the main character sprite so that it starts in a different place. This can be changed in the definition of the `main_sprite` dictionary.

### 2. Change the Key Position
Update the `x` and `y` coordinate of the key so that it starts in a different place. This can be changed in the definition of the `key_sprite` dictionary.

For an added challenge to the player, make the key appear somewhere off the screen!

### 3. Change the Background Color
Create a new color tuple and set the background to another color. This will be similar to `WHITE = (255, 255, 255)`, but with the new color and RGB values.

### 4. Create New Assets
Using [piskel](http://piskelapp.com), MS paint, or any other drawing tool, create new assets for the **main character**, **door**, and **key**. These assets should all have a width and height of 32 pixels - otherwise, they may not appear properly.

Once the new images have been created, add the files to the Repl project, and update the code to properly use them.

### 5. Change the Window Size
Update the window size to make it a little bigger. Do not update the `TILE_SIZE` unless the sizes of the assets have also been updated.

Move the sprites on the screen to appropriate locations on the new map.

### 6. Add Another Key
Instead of making the player collect only one key before victory, make them collect another as well!

1. Create a new sprite dictionary for the second key: `key2_sprite`
    - Reuse the same image as the first key if desired
1. Create a new game state variable to track the second key: `got_key2`
1. Allow the player to pick up the second key
    - Make it disappear when it is collected
1. Make it so the player only wins if they have collected both keys

## Advanced Challenges
These challenges are fairly advanced, and not much guidance is provided. Feel free to use the internet, or ask the instructors for help.

### 1. Add an Enemy
Create a new enemy sprite. Update the code so that the game will end if the player overlaps with the enemy.

### 2. Add a Power-up
Create a new power-up sprite. This should be something the player can pick up. Update the code so that if the player has picked up the power-up, they can defeat the enemy. Add logic so that the player can only win the game after defeating the enemy.

### 3. Add an Opening Message
Create another state for the game to represent the time before play has begun. In that time, display a message with some basic information about the game. Move onto the 'Playing' state once the player presses Enter.

### 4. Add Walls
Add some new sprites to represent walls in the game. The player should not be able to walk through these walls. This can create a maze to make the game a little more challenging.

Note that there are several ways to add walls, and some of them will be more maintainable than others. Try to think about the program design before diving into the challenge.

## Beyond
If desired, try to recreate the 1989 tile-based classic: [Chip's Challenge](https://en.wikipedia.org/wiki/Chip%27s_Challenge).

Watch this video to check out the gameplay:

<iframe width="100%" height="450px" src="https://www.youtube.com/embed/pcdMh1M7QLI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

This game shows more of what is possible with a very simple set of features. Creating stories and puzzles does not require fancy 3D graphics - a game like Chip's Challenge still holds up to this day. Use it as inspiration to develop a game in the same style.

### More Tutorials
Visit [this page](http://inventwithpython.com/pygame/) to see some additional tutorials. That site walks through the re-creation of several classic games.

### Other Games
There are hundreds of games that have been created with Pygame. Take a look at [this page](https://www.pygame.org/tags/all) to see a few of them.