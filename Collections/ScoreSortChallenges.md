# Sort By Score Challenges
After completing the [code-along](ScoreSortCodeAlong.md), attempt the challenges below.

## _Optional Practice: Bug Fixes_
View these buggy Repl projects and try to fix them. To make things easier, reference the completed code from the code-along, and compare it to the buggy code. Test each program and make sure that they all work properly!

- [Bug 1](https://replit.com/@HylandOutreach/ScoreSortBug-1)
- [Bug 2](https://replit.com/@HylandOutreach/ScoreSortBug-2)
- [Bug 3](https://replit.com/@HylandOutreach/ScoreSortBug-3)
- [Bug 4](https://replit.com/@HylandOutreach/ScoreSortBug-4)
  - Note: there are **3** bugs in the last one!

## 1. Add More Data
Now, getting back to the code-along code. The current list only has a few items, so sorting them isn't all that impressive. Add at least three more dictionary items to the `players` list.

1. Add a comma at the end of the _last item_ in the list
1. Create the structure for the new dictionary: `{}`
1. Within the new dictionary, add a `"name"` key with a new value
1. Within the new dictionary, add a `"score"` key with a new value
1. Repeat until there are at least three new items
1. Run the code, and verify that the sorting still works based on the score!

## 2. Multiple Scores
Often, a score will be an amalgamation of several scores. For example, the total score of a football game is the sum of the scores from each quarter. Track multiple scores for each dictionary item in the list.

1. Add a `"score2"` key to each item in the list
1. Give a value to each `"score2"` property
1. In the other part of the code, find the `find_min_idx` function definition
1. Find the `if` statement where two things are compared
1. Update the condition so that it takes both `"score"` and `"score2"` into account
  - It should check the `score` _plus_ the `score2` value
1. Find the part of the code that prints out the top players
1. Update it so it prints the total score instead of simply the score
  - Again, it should be `score` _plus_ `score2`
1. Run the program, and verify that the sorting works with the new scores!

## 3. Custom Players
>This challenge may be fairly challenging. Feel free to skip down to the next one if desired.

Right now, the program only uses [hard-coded](https://en.wikipedia.org/wiki/Hard_coding) players. This works for demonstrative purposes, but it would be more useful if the user of the program could add their own data. Update the code so this is possible!

1. Place the sorting code in a new function: `sort`
  - Take in the collection, and run the existing `while` code on it
1. At the bottom of the file, create a `while True` loop that repeats infinitely
1. In the body of the loop, ask the user what to do
1. Create an `if` for each command
1. If they want to add a player:
  - Ask them for player information
  - Create a new player dictionary
  - Add the new dictionary to the `players` list
1. If they want to see the players:
  - Sort the players list
  - Print out the players in the list
1. If they want to exit:
  - Use `break` to exit the loop

This should make it possible for users to add as many players as they would like, and see them sorted!

### BONUS: Multiple Sorting Methods
Often, when viewing data, it is possible to sort the data in multiple ways. Add in the ability for the program to sort the players by:

- Score (low to high)
- Name (alphabetical)
- Name (reverse alphabetical)

## 4. Rock Paper Scissors Redux
>This challenge could be somewhat challenging.

This challenge is totally separate from the score sorting program; start by making a new Repl project and go from there.

The goal is to create a Rock, Paper, Scissors game using a dictionary. It should be similar to the [Rock Paper Scissors](../BasicProgramming/RPSCodeAlong.md) code, but it will simplify things a bit.

### A Dictionary of Victories
The old way of doing Rock Paper Scissors involved several `if` statements. Those worked, but there seemed to be a lot of repetitive code. By using a dictionary, the code will be much more dynamic.

Here's the idea: create **one** dictionary object where the keys represent a possible move, and the value represents the move that that move beats. Like this:

```
1. key: Rock, value: Scissors (rock beats scissors)
2. key: Paper, value: Rock (paper beats rock)
3. key: Scissors, value: Paper (scissors beats paper)
```

That's all the information needed to determine the winner of a match!

1. At the top of the file, create a new variable named `victories`
1. Set the `victories` variable equal to a new dictionary: `{}`
1. Add a key of `"R"` to the dictionary with a value of `"S"`
1. Add keys of `"P"` and `"S"` with the proper values

Now the code contains the dictionary determining which move beats which.

### A Battle Function
The next step is to use the `victories` dictionary to determine the winner between two competitors. This should happen in a function named `battle`.

1. Under the `victories` dictionary, define a new function named `battle`
    - `def` keyword, space
    - function name (`battle`)
    - parentheses
    - Parameter 1: `player`
    - Parameter 2: `computer`
1. In the indented body of the `battle` function, create an `if` statement
1. For the `if` condition, check if `player` and `computer` are equal
1. If they are, print out `"Tie"`
1. Outside of the `if` statement, create an `elif` statement
1. For the `elif`, check if the value for the `victories` dictionary with a key of `player` is equal to `computer`
1. If it is, print out `"Player Wins"`
1. Outside of that `if`, create an `else`
1. In the else, print out `"Computer Wins"`

Run the code to make sure it works - but it shouldn't do anything yet!

### Testing
Under the definition of the `battle` function, call the `battle` function with a few test inputs. Make sure that every possible outcome can be achieved.

For example, it could be called in this manner:

```py
battle("P", "S")
```

The code above should cause the program to print out `Computer Wins`, because paper loses to scissors.

## 5. Another Sorting Algorithm
>This challenge is quite challenging.

Try to implement a _different_ sorting algorithm to sort the list of `players`! There is a lot of code available online to help. The biggest challenge is adapting the code to work for the specific solution. Here are some ideas:

- [Insertion Sort](https://www.geeksforgeeks.org/insertion-sort/)
- [Bubble Sort](https://www.geeksforgeeks.org/bubble-sort/)

### More Challenging
These two algorithms are a little more challenging to implement - they require using [recursion](https://en.wikipedia.org/wiki/Recursion).

- [Merge Sort](https://www.geeksforgeeks.org/merge-sort/)
- [QuickSort](https://www.geeksforgeeks.org/quick-sort/)
