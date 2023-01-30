# Rock, Paper, Scissors
Follow the instructions below to create a simple Rock Paper Scissors game in Python!

## Setting Up
Set up by creating a new Replit project.

1. Go to [Replit](https://replit.com)
1. Log in
1. Create a new Python Repl project named "Rock Paper Scissors"

## Player Input
The first step is to welcome the player to the game, and ask which move they would like to make.

1. Use a `print` statement to say "Welcome to Rock Paper Scissors!"
1. On the next line, use `input` to ask the user for a move - "Enter R, P, or S: "
1. Store the result of the `input` in a new variable named `player_move`

The code should look something like this:

```py
print("Welcome to Rock Paper Scissors!")

player_move = input("Enter R, P, or S: ")
```

## Computer Choice
Now the player has made a move, it's time to choose a move for the computer! The computer's move should be chosen _randomly_. Using a Python library, it will be possible to generate a random choice from a set of options ("R", "P", and "S").

1. At the top of the file, use `import random` to import the **random** library into the program
    - This provides a `random` object with a `choice` function
1. Under where the `player_move` is selected, create a new variable named `computer_move`
1. Set the `computer_move` variable to be `random.choice("RPS")`
    - This will choose either "R", "P", or "S" at random

The code should look something like this:

```py
import random

print("Welcome to Rock Paper Scissors!")
player_move = input("Enter R, P, or S: ")

computer_move = random.choice("RPS")
```

## Basic Battling
Now the player has a move, and the computer has a move... but which will win? Take a look at this table for a refresher on the rules of Rock Paper Scissors:

![](https://i.imgur.com/XeUU0KK.png)

In total, there are **9** possible outcomes. That's quite a lot, so instead of trying to code all 9, start with that first row.

There are three options:

- Player chooses **rock**, Computer chooses **rock** → **tie**
- Player chooses **rock**, Computer chooses **paper** → **loss**
- Player chooses **rock**, Computer chooses **scissors** → **win**

These all start the same: player chooses rock. That is the first _condition_ for each of these outcomes. In the code, under the `computer_move` line, create an `if` statement that checks if the player chose rock:

```py
if player_move == "R":
```

And what should happen if the player chooses rock? Well, it depends on what the computer chose!

### Rock v. Rock
Say the computer chose rock as well. That would be the next _condition_, still within the scope of this first condition:

```py
if player_move == "R":
    if computer_move == "R":
```

Now, in the block within the _second_ condition, it is known that the player chose rock, AND the computer chose rock. And what should happen in that case? It will be a tie! Print out a message saying as much.

```py
if player_move == "R":
    if computer_move == "R":
        print("Rock v. Rock: Tie")
```

Run the program, enter "R", and see what happens. It should only print something if the computer chooses rock.

### Rock v. Paper
Add code to handle the case when the computer chooses paper (after the player chose rock). This should be within the block of `player_move == "R"`, _under_ the `computer_move == "R"` statement.

1. Add an `elif` checking if the computer chose paper (indented 1 level)
1. Within that new `elif` block, create a `print` statement (indented 2 levels)
1. Add the result - "Rock v. Paper: Computer Wins"

### Rock v. Scissors
Add code to handle the case when the computer chooses scissors (after the player chose rock). This should, again, be within the block of `player_move == "R"`, _under_ the `computer_move == "R"` statement.

1. Add an `elif` checking if the computer chose scissors (indented 1 level)
1. Within that new `elif` block, create a `print` statement (indented 2 levels)
1. Add the result - "Rock v. Scissors: Player Wins"
   
### Testing the Code
At this point, the `if` statement should look something like this:

```py
if player_move == "R":
	if computer_move == "R":
		print("Rock v. Rock: Tie")
	elif computer_move == "P":
		print("Rock v. Paper: Computer Wins")
	elif computer_move == "S":
		print("Rock v. Scissors: Player Wins")
```

Run the program, and make sure that all outcomes are possible to reach. They should occur with approximately equal frequency.

## A Battling Function
So far, the program is working, but it is becoming a little unwieldy. Before adding in the other outcomes, define a function to handle the battling outcomes to clear up the main game code.

1. Right under the `import random` statement, create some space in the code
1. Define a new function named `battle`
    - The function should take in a `player` parameter (for the player's move)
    - The function should also take in a `computer` parameter (for the computer's move)
1. Copy the big `if` statement, and paste it into the _body_ of the `battle` function
    - Make sure it is indented one extra level under the definition line
1. Change `computer_move` and `player_move` to `computer` and `player` (respectively)

The function definition should look like this:
```py
def battle(player, computer):
    if player == "R":
        if computer == "R":
            print("Rock v. Rock: Tie")
        elif computer == "P":
            print("Rock v. Paper: Computer Wins")
        elif computer == "S":
            print("Rock v. Scissors: Player Wins")
```

Now, all that's left is to _call_ the `battle` function! Call it at the bottom of the file, passing in the `player_move` and `computer_move` values.

```py
battle(player_move, computer_move)
```

Run the code, and verify that it behaves in the same way. This was an example of [refactoring](https://en.wikipedia.org/wiki/Code_refactoring); the code changed, but the functionality stayed the same.

## All Battle Results
The next step is to modify the `battle` function to include all possible results. There are **6** remaining results to add:

- Player chooses **Paper**:
  - Computer chooses **Rock**: Win
  - Computer chooses **Paper**: Tie
  - Computer chooses **Scissors**: Loss
- Player chooses **Scissors**:
  - Computer chooses **Rock**: Loss
  - Computer chooses **Paper**: Win
  - Computer chooses **Scissors**: Tie

Handle each outcome in the `battle` function.

1. Under the `if`, add an `elif` checking if the player selected paper
1. Indented one additional level, check the three computer options
1. Print the result for each outcome
1. Under the player paper `elif`, check if the player selected scissors
1. Again indented one level under, check the three computer options
1. Print the results for each outcome

The code added code should look something like this:

```py
elif player == "P":
    if computer == "R":
        print("Paper v. Rock: Player Wins")
    elif computer == "P":
        print("Paper v. Paper: Tie")
    elif computer == "S":
        print("Paper v. Scissors: Computer Wins")
elif player == "S":
    if computer == "R":
        print("Scissors v. Rock: Computer Wins")
    elif computer == "P":
        print("Scissors v. Paper: Player Wins")
    elif computer == "S":
        print("Scissors v. Scissors: Tie")
```

Run the program a few more times, and test out the different paths! Try to reach every outcome.

## Game Loop
Now the game is complete, but it would be nice if rematches were a little easier. Create a game loop that will allow the player to play again as often as desired.

1. Above the "Welcome" message, create a new variable named `playing`
1. Set the `playing` variable to equal `"y"`
1. Under that, create a `while` loop that will continue as long as `playing` is equal to `"y"`
1. Indent the main game code, so that it is within the `while` loop code block
1. Find the bottom of the `while` loop block, still within the same scope
1. Create an `input` statement asking "Would you like to play again (y/n)? "
1. Set the `playing` variable to be the result of the `input`

The code should look something like this:

```py
playing = "y"
while playing == "y":
	print("Welcome to Rock Paper Scissors!")

	player_move = input("Enter R, P, or S: ")
	computer_move = random.choice("RPS")

	battle(player_move, computer_move)

	playing = input("Would you like to play again (y/n)? ")
```

Run the program, and make sure it is possible to play multiple times!

## Final Code
```py
import random

def battle(player, computer):
	if player == "R":
		if computer == "R":
			print("Rock v. Rock: Tie")
		elif computer == "P":
			print("Rock v. Paper: Computer Wins")
		elif computer == "S":
			print("Rock v. Scissors: Player Wins")
	elif player == "P":
		if computer == "R":
			print("Paper v. Rock: Player Wins")
		elif computer == "P":
			print("Paper v. Paper: Tie")
		elif computer == "S":
			print("Paper v. Scissors: Computer Wins")
	elif player == "S":
		if computer == "R":
			print("Scissors v. Rock: Computer Wins")
		elif computer == "P":
			print("Scissors v. Paper: Player Wins")
		elif computer == "S":
			print("Scissors v. Scissors: Tie")

playing = "y"
while playing == "y":
	print("Welcome to Rock Paper Scissors!")

	player_move = input("Enter R, P, or S: ")
	computer_move = random.choice("RPS")

	battle(player_move, computer_move)

	playing = input("Would you like to play again (y/n)? ")
```

## Challenges
After the activity, start working on the [Rock Paper Scissors Challenges](RPSChallenges.md).
