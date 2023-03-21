# Rock Paper Scissors Challenges
After completing the [code-along](RPSCodeAlong.md), attempt the challenges below.

## _Optional Practice: Bug Fixes_
View these buggy Repl projects and try to fix them. Test the program and make sure that all outcomes are reachable.

- [Bug 1](https://replit.com/@HylandOutreach/RPSBug-1)
- [Bug 2](https://replit.com/@HylandOutreach/RPSBug-2)
- [Bug 3](https://replit.com/@HylandOutreach/RPSBug-3)
- [Bug 4](https://replit.com/@HylandOutreach/RPSBug-4)

## 1. Nicer Printing
While the program should be functional after the code-along, it does not have the best user experience. Update the code to make it a little easier to read for the user.

1. Add an empty `print` statement under the "Welcome" message to make a new line under it
1. Add another empty `print` statement above the final `input` in the `while` block
1. Add another empty `print` statement at the _bottom_ of the `while` block
1. Add `print` statements above and below the `battle` output, adding a "box" using dashes

Run the program, and make sure it is a little more usable!

### BONUS: ASCII Art
[ASCII art](https://en.wikipedia.org/wiki/ASCII_art) is a graphic design technique that creates images from text characters. Utilize some ASCII art to make the program more exciting!

In Python, it is possible to create [multiline strings](https://www.w3schools.com/python/gloss_python_multi_line_strings.asp), which can make ASCII art much easier. Instead of using a single double quote ( `"` ) to start and end a string, use _three_ double quotes ( `"""` ).

For example, this code:

```py
value = """this is a 
multiline
string"""
print(value)
```

will print this:

```
this is a 
multiline
string
```

An example of art for Rock Paper Scissors can be found here: https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe

## 2. Handling Invalid Input
At the moment, the program works if the user enters "R", "P", or "S". However, if the player enters anything else, no message is displayed. Make some updates so that this is properly handled.

1. In the `battle` function, find the bottom of the block
1. At the same level as the first `if`, add an `else:` clause
1. In the `else` block, print a message saying "Invalid Selection"

Run the program, and verify that invalid input sees a proper response!

### BONUS: Boxify Valid Battle
As it is, the "Invalid Selection" will display in the same "box" as the battle statement. Update the code so that the "box" dashes only appear for a legitimate battle.

## 3. Tracking Score
This challenge is a little more difficult. One nice feature for the program would be the ability to track a player's wins across multiple games.

1. Find the `battle` function definition
1. Find each `print` statement where the player wins
1. Under each of those statements, with the same indentation level, add `return True`
    - This `True` indicates that the player won the battle
1. For each other `print` statement, add `return False` directly beneath
1. Above the `while` loop, create a new variable named `score`
1. Set the value of the `score` variable to `0`
1. Within the `while` loop, find the `battle` function _call_
1. Set the _result_ of the `battle` call to a new variable: `won`
1. Under the `battle` call, create an `if` statement
1. Make the `if` statement check if `won` is `True`
1. In the block of the `if` statement, increment the value of `score` by `1`
1. Under the `if` statement (outside the indented block), create a `print`
1. Make the `print` statement print out the `score` variable
    - `print("Score: " + str(score))`

Run the program again, and verify that the score goes up with every victory!

## 4. More Moves
This challenge may be quite difficult. One variation of the game adds two additional move options: Spock and Lizard. This version was invented by [Sam Kass and Karen Bryla](http://www.samkass.com/theories/RPSSL.html), and later popularized by the CBS sitcom The Big Bang Theory.

The outcomes are as follows:

![](https://i.imgur.com/jLxotXL.png)

It adds this additional logic:

- **Rock** vs. **Spock** - **L**
- **Rock** vs. **Lizard** - **W**
- **Paper** vs. **Spock** - **W**
- **Paper** vs. **Lizard** - **L**
- **Scissors** vs. **Spock** - **L**
- **Scissors** vs. **Lizard** - **W**

Update the program so that it can handle these additional cases.

## 5. Hangman, Tic Tac Toe, or Something Else
Create a completely different console game using the same programming concepts from the Rock Paper Scissors game. Add some ASCII Art to make it fun.
