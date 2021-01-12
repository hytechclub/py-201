# Sort By Score
In this activity, create a program that can sort some players by their score. The sport/game/event in which they participate is up to you! These could be tennis players, basketball players, chess players, Super Smash Bros Melee players, or anything at all. The important thing is that they must have some numeric "score" attached to them.

## Setting Up
1. Go to [repl.it](https://repl.it)
1. Log in
1. Create a new Python Repl project named "Score Sort"

## Creating the Players (Dictionaries)
The first step is to create a few players for the program. Think of some specific people who could be players, or just make people up! Ultimately, each player should have a "name" property and a "score" property.

1. At the top of the **main.py** file, create a `player1` variable
1. Set `player1` to equal a new [dictionary](https://www.w3schools.com/python/python_dictionaries.asp)
1. Add a `"name"` key, and set it to some value (e.g. `"Alice Kostas"`)
1. Add a `"score"` key, and set it to some value (e.g. `510`)
1. Repeat the steps above to create a `player2` dictionary
1. Repeat the steps above to create a `player3` dictionary
1. Add code at the bottom to print out each created player dictionary
1. Run the program, and verify that data for the three players appears!

### Code
```py
player1 = {
    "name": "Alice Kostas",
    "score": 510
}

player2 = {
    "name": "Justin Blake",
    "score": 400
}

player3 = {
    "name": "Gregoria Alonzo",
    "score": 390
}

print(player1)
print(player2)
print(player3)
```

## Creating the List
Now all the data is there, but it is not connected in any way. With this amount of data, it would be easy to simply look at the scores and put the players in order by hand. However, if there were ten or twenty or a thousand players, that would be unfeasible. So how can this data be stored? Using a [list](https://www.w3schools.com/python/python_lists.asp) of course!

1. Above the `player1` variable, create a new variable named `players`
1. Set the `players` variable equal to a new list
1. Move the data from each player variable into the list
    - Remove the variable name and equals sign
    - Place the dictionary within the square brackets for the list
    - Add a comma after the closing curly bracket
1. Remove the existing `print` statements
1. Create a _new_ `print` statement that prints out the `players` variable
1. Run the code, and verify that all the players appear!

```py
players = [
	{
		"name": "Alice Kostas",
		"score": 510
	},

	{
		"name": "Justin Blake",
		"score": 400
	},

	{
		"name": "Gregoria Alonzo",
		"score": 390
	},
]

print(players)
```

## Using Selection Sort
Now that the dataset exists, it's time to sort it! It may seem trivial with only three objects, but the sorting should work regardless of how many objects there are.

### Algorithm Steps
Before diving into the code, refer back to the steps of the Selection Sort algorithm:

1. Find the smallest value index in the list
1. Swap that value with the current element
1. Repeat with the rest of the list

And the pseudocode:
```
For all elements:
  Get remaining list

  Find min element in list

  Swap current with min
```

In this case, it is actually desirable to find the _maximum_ value instead of the minimum. The algorithm won't change too much though. Ultimately, it should work something like this:

```
Loop through each element in the list:
  Find the index for the maximum value in the list starting at the current element
  Swap the current element for the maximum value found
```

This visual demonstration may be helpful:

![](https://i.stack.imgur.com/mGSJZ.gif)

Don't worry if this seems confusing. It takes a while to understand list sorting - just know that this will work!

### Turning Pseudocode into Python Code
Now it's time to actually implement the algorithm. For this part, it will be assumed that some magical functions exist; they don't exist yet, but they will later!

1. Under the `players` list, create a `while` loop structure
    - Make a new `i` variable set to `0`
    - Create a `while` loop checking if `i` is less then the length of `players`
    - In the indented body of the loop, set `i` to itself plus `1`
1. In the body of the `while` loop, above the increment, create a `max_idx` variable
1. Set the variable to the result of a call to `find_max_idx`
1. Consider the arguments needed for the `find_max_idx` function
    - The goal is to find the maximum value index between the current position and the end
    - Need to pass the `players` list
    - Need to pass the current index
1. Under that in the `while`, call the currently non-existent `swap` function
    - The goal is to swap the max value with the current position
    - Need to pass the `players` list
    - Need to pass the current position `i`
    - Need to pass the new value `max_idx`

Try to think through what's happening in the algorithm and the code.

- While loop, starting at the beginning of the list, going through the end
- For each position, find the maximum between the current position and the end of the list
- Swap the maximum with the current position
- Now, the list up to the current position will be sorted

### Code
```py
i = 0
while i < len(players):
	max_idx = find_max_idx(players, i)
	swap(players, i, max_idx)

	i=i+1
```

The code won't work just yet... the `find_max_idx` and `swap` functions still need to be defined!

## Finding the Maximum
Finding the maximum value in a list is actually another algorithm. Here are the steps:

```
Set the current max index to the starting element
For each element in the remainder of the list:
    If the element is greater than the element at the current max:
        Set the current max index to the current position

Return the max after searching the whole list
```

Now turn that into Python code!

### The `find_max_idx` function
1. Above the `while` structure, define a function named `find_max_idx`
    - Parameter 1: `collection` (the list)
    - Parameter 2: `starting_pos` (the current position in the list)
1. In the indented body of the function, create a variable named `max_idx`
1. Set `max_idx` to the `starting_pos` to begin
    - All other elements will be compared to this
1. Under that, create a `pos` variable set to `starting_pos+1`
    - This will track the position in the list
1. Create a `while` loop
1. For the `while` condition, check if `pos` is less than the collection length
1. In the indented body of the `while` loop, create a variable `current_player`
1. Set `current_player` to the value in the `collections` list at `pos`
1. Under that, create a variable `max_player`
1. Set `max_player` to the value in the `collections` list at `max_idx`
1. Under that, create an `if` statement
1. For the condition, check if the `current_player` score is greater than the `max_player` score
1. If it is, set the `max_idx` variable to `pos`
1. After the `if` statement (not indented), increment the value of `pos` by `1`
1. After the `while` loop, return `max_idx`
    - This will have the maximum value index from the whole list

### Final Code
```py
def find_max_idx(collection, starting_pos):
	max_idx = starting_pos

	pos = starting_pos+1
	while pos < len(collection):
		current_player = collection[pos]
		max_player = collection[max_idx]
		if current_player["score"] > max_player["score"]:
			max_idx = pos
		pos=pos+1

	return max_idx
```

The code still won't run just yet... the `swap` function still needs to be defined.

## Swapping the Values
Swapping two values in a list is a little simpler. At first thought, it might seem like a developer could just say something like:

```
list[index1] = list[index2]
list[index2] = list[index1]
```

The problem, however, is that once one element is changed, its value disappears! Using a temporary variable to store that value is one solution to this problem. Use it to define the `swap` function.

1. Under the `find_max_idx` function, define a new function named `swap`
    - Parameter 1: `collection` (the list)
    - Parameter 2: `i` (the first index for the swap)
    - Parameter 3: `j` (the second index for the swap)
1. In the indented body of the function, create a `tmp` variable
1. Set the `tmp` variable to the element in `collection` at position `i`
1. Now that the old value stored, set `collection[i]` to `collection[j]`
1. Finally, set `collection[j]` to the stored `tmp` value
1. Run the program, and verify that it does not error!

```py
def swap(collection, i, j):
	tmp = collection[i]
	collection[i] = collection[j]
	collection[j] = tmp
```

Now, all of the functions have been defined. It's time to print out the results of the sorted list!

## Printing the Results
To print the results, use a `for` loop.

1. Find the very bottom of the **main.py** file
1. Use a `print` statement to display a header saying "-Top Players-"
1. Under that, create a `for` loop structure
    - `for` keyword
    - Element variable: `p`
    - `in` keyword
    - Collection: `players`
1. In the indented body of the `for` loop, create a variable named `name`
1. Set the `name` variable to the `"name"` of the current element `p`
    - `p["name"]`
1. Under that (still indented), create a variable named `score`
1. Set the `score` variable to the `"score"` of the current element `p`, wrapped in a `str()`
    - `str(p["score"])`
1. Under the `score` variable, create a `print` statement
1. In the `print`, print the `name` and the `score`, added together with `": "` in the middle

```py
print("-Top Players-")
for p in players:
    name = p["name"]
    score = str(p["score"])
    print(name + ": " + score)
```

Run the code, and verify that the top players appear, printed nicely! Try changing around the values a bit to make sure the sorting actually works.

## Final Code
```py
players = [
	{
		"name": "Alice Kostas",
		"score": 510
	},

	{
		"name": "Justin Blake",
		"score": 400
	},

	{
		"name": "Gregoria Alonzo",
		"score": 390
	},
]

def find_max_idx(collection, starting_pos):
	max_idx = starting_pos

	pos = starting_pos+1
	while pos < len(collection):
		current_player = collection[pos]
		max_player = collection[max_idx]
		if current_player["score"] > max_player["score"]:
			max_idx = pos
		pos=pos+1

	return max_idx

def swap(collection, i, j):
	tmp = collection[i]
	collection[i] = collection[j]
	collection[j] = tmp

i = 0
while i < len(players):
	max_idx = find_max_idx(players, i)
	swap(players, i, max_idx)

	i=i+1

print("-Top Players-")
for p in players:
	name = p["name"]
	score = str(p["score"])
	print(name + ": " + score)
```

## Challenges
After the activity, start working on the [Score Sort Challenges](ScoreSortChallenges.md).