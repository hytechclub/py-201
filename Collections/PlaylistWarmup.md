# Playlist Warm-up Activity
The goal of this warm-up is to create a playlist program. This program will print a list of songs. This activity involves topics that have not been covered yet, so things may be unfamiliar - that's okay. Just try to follow the instructions as well as possible.

This activity should be completed in groups. **Each group will present their playlist at the end of the activity**. Here are the multiplayer Repl projects for the groups:

- Group 1: https://replit.com/join/uaborkiuzb-hylandoutreach
- Group 2: https://replit.com/join/msfvutocvf-hylandoutreach
- Group 3: https://replit.com/join/rzvofsiwbx-hylandoutreach
- Group 4: https://replit.com/join/njidlpvysl-hylandoutreach

Click on the link for your assigned group to begin.

## Part 1: Brainstorming Songs
The first thing to do is think of songs to add to the playlist! These could be any song from anywhere (as long as it is appropriate). Try to think of your favorite song(s) of all time. Feel free to include fake songs if desired. Each song should have a _title_ and an _artist_.

- Open the **songs.txt** file in the Repl project, and add songs there. Do not worry about the **main.py** file for now.
- **Every group member must contribute at least one song.**
- **There must be at least 5 songs total.**

## Part 2: Research
Before jumping into the code, take a look at some documentation. The code will use dictionaries and lists, two important collections in the Python world. Read through these articles as a group. One student should attempt to explain each topic to the rest of the group. Make sure to ask questions!

- [Python Lists](https://www.w3schools.com/python/python_lists.asp)
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp)

## Part 3: Replacing Songs in the Python Code
The next step is to get into the actual code! Open up the **main.py** file to take a look.

1. Run the code to see what it currently does
1. Notice how each title and artist appear in the code
1. Notice the placement of the curly brackets, colons, and commas
1. Find the existing three songs in the code
1. Replace each instance of "All Star" and "Smash Mouth" with titles/artists from the **songs.txt** file
1. Run the code, and verify that the three new songs appear!

## Part 4: Adding More Songs
Now the playlist should have some of the songs, but not all of them yet. Try to figure out how to add a couple more songs.

1. Find the final song in the code, ending with `},`
1. Under that, type in a new `{`
1. Under _that_, add the `"title": "",` and `"artist": "",`
1. Under _that_, add another `},`
1. Repeat the steps above once more
1. Make sure the titles and artists reflect songs from the **songs.txt** file
1. Run the code, and verify that all the songs appear!

## Part 5: Adding Color
One fun feature of Python is the ability to change the color of text in the console. This is possible using the **colorama** library, with the `Fore` object. Adding any `Fore` value in front of a printed string will turn the text that color. Update the code so that each song has its own color!

**Possible Colors**
```
Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE, Fore.RESET
```

### Updating the Songs
Add a color to each song in its data, along with the "title" and "artist" values. Make sure to note the commas, curly brackets, and colons.

1. For the first song, find the "title" and "artist"
1. Right under the "artist" line, _above_ the `},`, make a new line
1. Do something similar to the "artist" line, but use "color" instead
1. On the right side of the colon, add in `Fore.RED`  
    ```py
    {
        "title": "All Star",
        "artist": "Smash Mouth",
        "color": Fore.RED
    },
    ```
1. Update all of the other songs in the same way, choosing different colors

Try running the program. Nothing should have actually changed yet... 

### Using the Color
Now that each song has a color, make sure the color is used when the song is printed!

1. Find the `print` statement that prints out the song
1. Right inside the parenthesis, make some space
1. Add in `song["color"]`
    - This will access the color of the given song
1. After that, add a `+` so it connects to the rest of the song
    - Adding this will change the color for the text!

Run the program again, and verify that each song appears with its own color!

## Final Code
By the end of the activity, the code should look something like this:

```py
from colorama import Fore

print("Welcome to the Greatest Playlist Ever")

songs = [
	{
		"title": "All Star",
		"artist": "Smash Mouth",
		"color": Fore.RED
	},
	{
		"title": "All Star 2",
		"artist": "Smash Mouth",
		"color": Fore.CYAN
	},
	{
		"title": "All Star 3",
		"artist": "Smash Mouth",
		"color": Fore.GREEN
	},
	{
		"title": "All Star 4",
		"artist": "Smash Mouth",
		"color": Fore.YELLOW
	},
	{
		"title": "All Star 5",
		"artist": "Smash Mouth",
		"color": Fore.MAGENTA
	},
]

for song in songs:
	print(song["color"] + song["title"] + " by " + song["artist"])
```
