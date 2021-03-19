# Database Challenges
After completing the [code-along](RestaurantReviewCodeAlong.md), attempt the challenges below. These exercises will reinforce the database skills from the code-along.

After working on the challenges for a while, feel free to start working on the [final project](../FinalProject/StudentDesc.md).

## Challenge 1: Adding a 'Date of Visit' Property to Review Objects
In this challenge, add a new piece of data to store with each Restaurant Review object: the date that the reviewer visited the restaurant. For the purposes of this exercise, the date will be stored as a simple string.

### Part A: Updating the `add_review` Function
First, update the `add_review` function so that it can handle the new "date of visit" value.

1. Open the **reviews.py** file for editing
1. Find the `add_review` function
1. Add a parameter to the function: `date_of_visit`
1. Find the new dictionary that is added to the database with `db[new_db_key]`
1. Add a new key to the dictionary: `'date_of_visit'`
1. Set the value for the `'date_of_visit'` key to be the `date_of_visit` parameter

Run the program, and try adding a new review. At this point, it should fail - the _call_ to the `add_review` function does not have the proper arguments!

### Part B: Updating the `prompt_for_add_review` Function
Now that the `add_review` function can handle the new property, make sure the user is asked for it as well.

1. Open the **main.py** file for editing
1. Find the `prompt_for_add_review` function
1. Under the `text` variable, create a new variable named `date_of_visit`
1. Set the `date_of_visit` variable to an `input` asking what date the user visited the restaurant
1. Pass the `date_of_visit` variable into the `add_review` function call

Run the program again, and now try adding a new review. It should work! The `date_of_visit` value should be stored in the database. But it is currently not possible to see the information anywhere.

### Part C: Updating the `print_reviews` Function
Next, make sure the user can actually see each review date when they view all reviews.

1. Open the **main.py** file for editing
1. Find the `print_reviews` function
1. Find the `for` loop that loops through `review_list`
1. Make a new line under the line that prints out the score for the `review`
1. On that line, print out the date of visit for the review, e.g.: `Date of Visit: Oct 10, 2010`

Run the program once more, print all reviews, and verify that it is possible to see the date of visit for each new review!

## Challenge 2: Adding a Command to Print Certain Restaurant Reviews
In this challenge, add a command to the application that allows the user to select a certain restaurant, and see reviews _only_ for that restaurant. Note that there are several different ways to accomplish this, so feel free to do whatever works.

### Part A: Defining the Function
First, define a new function that will execute the command.

1. Open the **main.py** file for editing
1. Under the `print_reviews` function definition, define a new function named `print_reviews_for_restaurant`
1. In the body of the `print_reviews_for_restaurant` function, add `os.system('clear')` to clear the console
1. Next, create a variable named `restaurant_filter`
1. Set `restaurant_filter` to an `input` asking which restaurant to find reviews for
1. Under that, get the reviews by using `reviews.get_reviews()`
    - Store the result in a variable named `reviews`
1. Under that, create a `for` loop that loops through each `review` in `reviews`
1. In the body of the `for` loop, check if the `'restaurant'` for the `review` matches `restaurant_filter`
    - If it does, print out the review
    - If it does not, do nothing

Now the function is defined, but it will not do anything until it is called.

### Part B: Adding the Command
Next, add a command in the `while True` loop to handle printing reviews for a certain restaurant.

1. At the bottom of the menu, print out `[1] View Reviews for Restaurant`
1. Create an `elif` that checks if the user entered `1`
1. If they did, call the `print_reviews_for_restaurant` function

Run the program, and verify that it is possible to see all reviews for only one restaurant!

### (BONUS) Part C: Refactoring
Try to figure out a different way to create this functionality. Currently, some code is being repeated that prints out each restaurant. See if it is possible to make this work better.

## Challenge 3: Handling Improper Scores
Currently, it is possible to enter any score for a review. It should only be possible to enter a **number** between `0` and `10`. Fix the code to prevent the user from entering a score outside of those boundaries.

1. Open the **main.py** file for editing
1. Find the `prompt_for_add_review` function
1. Find where the `score` variable is set in the function
1. Under that, create an `if` statement checking if `score` is outside the range of `0` and `10`
1. If it is, print a message saying "ERROR" and `return`
1. Make a similar change to the `prompt_for_update_review` function

Run the program, and verify that it is impossible to enter a score that is greater than `10`, or less than `0`.

### (BONUS) No Non-numeric Input
Currently, if the user enters something other than a number for the score, the program crashes. Fix it so that the error is handled more gracefully. This may require some research.

## (BONUS) Challenge 4: Sorting the Reviews
In the current version of the app, the reviews are not printed in any particular order. Figure out how to sort them in a couple different ways:

- Alphabetically by restaurant name
- Chronologically by date of visit
- Ranked by score

The program should ask the user how to sort the reviews before printing them.

## (BONUS) Challenge 5: Adding Authentication
At this point, any person who enters the application will be able to add a review. Fix it so that a user must be logged in to add reviews. There are several ways to do this, but here is some guidance:

- Add a `user` property to each object in the database
- Store a list of users in the database
- Allow users to create an account
- Only allow users to edit their own reviews
- Create a log-in mechanism where users enter their name and a password
- Allow a user to see their own reviews

Feel free to learn more about authentication before diving into this challenge.

## Beyond
There are infinite possibilities with the Repl.it DB. Try to build a completely new application, possibly a Flask web app, a Pygame game, or a Discord bot, that uses a database. This can also lead directly into the [final project](../FinalProject/StudentDesc.md).