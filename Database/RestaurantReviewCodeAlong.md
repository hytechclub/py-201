# Restaurant Review Code-Along
In this activity, use [Repl.it's Database](https://docs.repl.it/misc/database) to create a console-based Restaurant Review application. The most interesting part of this program will be that the data stored in the application will persist across runs.

## Getting Started
There is a starter version of the app, but it is really just the facade with no functionality. It has all the "user interface" without the actual data; a `while` loop menu, and functions to retrieve information from the user and presumably create, read, update, and delete reviews. All that's missing is the actual database.

1. Go to the [starter Repl project](https://repl.it/@HylandOutreach/FakeYelpStart)
1. Click the "Fork" button to fork it
1. Run the application to see how it currently works

## A `reviews` Module
In order to keep things organized, create a separate [module](https://docs.python.org/3/tutorial/modules.html) for accessing the database.

1. Create a new file in the Repl project named **reviews.py**
1. Open the **reviews.py** file for editing
1. In the file, define a new function named `clear_all` (no parameters)
1. In the body of the `clear_all` function, simply put `print('clearing')` for now

### Using the Module
Now that the `reviews` module has been created, it will be possible to use it within the **main.py** file.

1. Open the **main.py** file for editing
1. At the top of the file, under `import os`, make a new line
1. Add the following code to import the `reviews` module:  
    ```py
    import reviews
    ```
1. Find the `clear_db` function definition in the **main.py** file
1. Find the comment that says `# Actually delete everything`
1. Under that, add the following code to call the `clear_all` function from the **reviews.py** file:  
    ```py
    reviews.clear_all()
    ```
1. Run the program, enter `0` as the command, and verify that the `clear_all` function runs

Now the **reviews.py** file has successfully been connected to the **main.py** file.

## Clearing the Database
One useful tool to employ during the database development process is a way to clear everything out of the database. This can remove any unwanted test data or poorly structured objects, and will help ensure the application works with a fresh environment.

1. At the top of the **reviews.py** file, add the code below to import the `replit.db` module:  
    ```py
    from replit import db
    ```
1. Find the `clear_all` function definition
1. In the body of the function, remove the `print` and create a `for` loop
1. For the `for` loop item variable, use `key`
1. For the `for` loop collection, use `db.keys()`  
    - This retrieves a collection of every single key in the DB
1. In the body of the `for` loop, add the following code to delete the object at the current key:  
    ```py
    del db[key]
    ```

The code in the **reviews.py** file should look something like this:
```py
from replit import db

def clear_all():
  for key in db.keys():
    del db[key]
```

There is currently no way to test this, because there is no way to add anything to the database! That will come later - next, it's time to think about the architecture of the database.

## Architecture
Before diving into the CRUD implementation, take a moment to consider the format of the data.

### Review Objects
Each **Review** object should have each of the following properties:
- The name of the restaurant
- A score for the  review
- The text for the review

Each review can be stored in a dictionary with keys for each property. For example:

```py
review = {
    'restaurant': 'Chipotle',
    'score': 8,
    'text': 'I ordered a burrito with only guacamole in it and it was delicious'
}
```

Those dictionaries would then be stored within the Repl.it database.

### Keys
Because the Repl.it database uses a simple key-value store, different types of data can be represented with _prefixes_. For example, each review object stored in the database could have a key that begins with `review_`. That way, it would be possible to find all review keys using `db.prefix`:

```py
review_keys = db.prefix("review_")
for key in review_keys:
    review = db[key]
    # do something with `review`
```

Each key must be unique, so the code needs a way to generate a different key for each new review.

### Review ID
Review objects should be identifiable based on an ID. Rather than having the user come up with this ID, the code can _auto-increment_ a numeric ID value.

The current value of the ID can be stored in the database with a key of `'next-id'`. For example, it could look like this.

**db**
```py
{
    'next-id': 0
}
```

Then, when a new review is created, it would increment:

**db**
```py
{
    'next-id': 1,
    'review_0': {
        'restaurant': 'Burger King',
        'score': 10,
        'text': 'I love the burger king'
    }
}
```

And so on:

**db**
```py
{
    'next-id': 2,
    'review_0': {
        'restaurant': 'Burger King',
        'score': 10,
        'text': 'I love the burger king'
    },
    'review_1': {
        'restaurant': 'The Cheesecake Factory',
        'score': 4,
        'text': 'I ate too much cheesecake'
    }
}
```

From there, if a user of the database wanted to access a review, all they would need is the numeric id. They could then create the db key based on that value.

```py
numeric_id = 1
db_key = 'review_{0}'.format(numeric_id)
review_1 = db[db_key]
```

Now that the structure of the database has been determined, it's time to start using it.

## [CREATE] Adding a Review
The first thing to do when working with the Repl.it database is add some data to it! Create a function that can add a new review to the database. The function should take in the various **Review** object properties as parameters. It should generate a new ID, increment the next ID, create a db key, create the dictionary object, and add the object to the db with the key.

### Function Definition - Setup
Start with the stubbed out form of the function definition.

1. Open the **reviews.py** file for editing
1. Under the `clear_all` function definition, make a new line
1. Define a new function named `add_review`  
  - It should take three parameters: `restaurant`, `score`, and `text`

The function should look something like this so far:

```py
def add_review(restaurant, score, text):
```

### Function Definition - Getting the ID
Next, the function should generate an ID for the new **Review** object. The trick here is that the database _might_ have an auto-incremented ID already running, but it might not. If it does, the next ID should be retrieved from the database. If it does not, the ID should be `0`.

1. In the body of the `add_review` function, declare a variable named `id_for_new_review`
1. Set the `id_for_new_review` variable to `0`
1. Under that, create an `if` statement
1. For the `if` condition, check if `'next_id'` is in `db.keys()`  
  - This will tell the code if there is already a `next_id` value
1. In the body of the `if`, set the `id_for_new_review` variable to `db['next_id']`  
  - This will grab the `next_id` value from the database
1. Outside of the `if` statement, set the `next_id` value in the database to `id_for_new_review + 1`  
  - This is the _auto-increment_ that occurs with each new object

The code for this part should look something like this:

```py
id_for_new_review = 0

if 'next_id' in db.keys():
  id_for_new_review = db['next_id']

db['next_id'] = id_for_new_review + 1
```

### Function Definition - Adding the Review Object
Now that an ID has been generated, the review can be added. First, create the db key based on the ID. Then, add a new dictionary to the db with the proper values, using the created key.

1. Still in the body of the `add_review` function, make a new line
1. Create a variable named `new_db_key`
1. Set `new_db_key` to equal `'review_{0}'.format(id_for_new_review)`  
  - This will append the new ID to the `'review_'` prefix for the key
1. Under that, set the `db[new_db_key]` value  
  - It should be a new dictionary with `restaurant`, `score`, and `text` properties

The code for this part should look something like this:

```py
new_db_key = 'review_{0}'.format(id_for_new_review)

db[new_db_key] = {
  'restaurant': restaurant,
  'score': score,
  'text': text
}
```

### Calling the Function
Now that the `add_review` function has been defined, it must be called appropriately.

1. Open the **main.py** file for editing
1. Find the `prompt_for_add_review` function
1. In the body of that function, find the comment that says `# Actually add the review`
1. Under that, call the `reviews.add_review` function
1. Pass in `restaurant`, `score`, and `text` as the arguments
1. Run the program, and verify that it is possible to add a review to the DB!

The code should look something like this:

```py
# Actually add the review
reviews.add_review(restaurant, score, text)
```

### Testing
After adding a review, refresh the page, and go to the Database tab in the Repl. There should be 2 keys in the DB now:

![](https://i.imgur.com/7HlRkVi.png)

While that verifies that _something_ was added to the database, the real way to test this code is by _reading_ from the database. That comes next!

## [READ] Getting Reviews
Now that the database presumably has a review to read, it's time to fill out the "View Reviews" functionality. Define a function that will loop through each review key, grab each review object, and return a list of all of them (including their respective IDs).

### Function Definition - Setup
Start with the basic function definition setup.

1. Open the **reviews.py** file for editing
1. At the bottom of the file, under the `add_review` function definition, make some space  
1. Define a new function named `get_reviews`
  - It should take no parameters
1. In the body of the `get_reviews` function, create a new variable named `all_reviews`
1. Set `all_reviews` to a new empty list (`[]`)

The code so far should look like this:

```py
def get_reviews():
  all_reviews = []
```

### Function Definition - For Loop
Next, loop through the reviews and add them to the list.

1. Under the `all_reviews` variable, still in the `get_reviews` body, create a `for` loop
1. For the `for` loop item name, use `key`
1. For the `for` loop collection, use `db.prefix('review_')`  
  - This will retrieve all keys in the DB that begin with `review_`
1. In the body of the `for` loop, create a variable named `review_dict`
1. Set `review_dict` to `db[key]`
  - This will grab the object with the current key
1. On the next line in the `for` loop body, reference the `'id'` key of `review_dict`
1. Set it equal to `key.replace('review_', '')`
  - This will be the ID by itself, without the `review_` prefix
1. On the next line in the `for` loop body, `append` the `review_dict` to the `all_reviews` list

The `for` loop code should look like this:

```py
for key in db.prefix('review_'):
  review_dict = db[key]
  review_dict['id'] = key.replace('review_', '')
  all_reviews.append(review_dict)
```

### Function Definition - Return
For the last part of the `get_reviews` definition, return the list. At the bottom of the `get_reviews` body (outside of the `for` loop), add `return all_reviews`.

The code for the function should look something like this:

```py
def get_reviews():
  all_reviews = []
  for key in db.prefix('review_'):
    review_dict = db[key]
    review_dict['id'] = key.replace('review_', '')
    all_reviews.append(review_dict)
  
  return all_reviews
```

### Calling the Function
Now that the function is ready, it must be called properly.

1. Open the **main.py** file for editing
1. Find the `print_reviews` function definition
1. In the body of `print_reviews`, find the comment that says `# Actually get the reviews`
1. Under that, replace the `[]` with a call to the `reviews.get_reviews` function
1. Run the code, and verify that it is possible to view any added reviews with the proper information!

The code to call the function should look something like this:

```py
# Actually get the reviews
review_list = reviews.get_reviews()
```

At this point, the app is actually fairly functional! It should be possible to add and view reviews. The next two parts complete the CRUD functionality - **U**pdating and **D**eleting.

## [UPDATE] Updating a Review
On a return visit to a previously reviewed restaurant, a user of the app may decide that they have a different opinion than their original review expressed. In this case, it would be nice if they could update their review. This will be possible because each review has a unique ID, and the database entry for a review can be updated based on new information.

Define a function to update a review. It should take in a review ID, a new score, and new review text. It should grab the proper review from the database (based on the ID provided). If the ID is invalid, the function should return false. Otherwise, it should re-set the database object with the new values, and return true.

### Function Definition - Setup
First, create the stub for the function.

1. Open the **reviews.py** file for editing
1. Make some space at the bottom of the file
1. There, define a new function named `update_review`  
  - It should take three parameters: `review_id`, `score`, and `text`

The function should look something like this so far:

```py
def update_review(review_id, score, text):
```

### Function Definition - Getting the Review Key
Next, make the function actually do something. The first thing to do is grab the existing review based on the `review_id` parameter.

1. In the body of the `update_review` function, create a variable named `update_db_key`
1. Set `update_db_key` to `'review_' + review_id`
  - This will be the key for the review with the given ID
1. Under that, still in the `update_review` body, create an `if` statement
1. For the `if` condition, check if `update_db_key not in db.keys()`  
  - This would mean a review with that ID does not exist
1. In the body of the `if`, return `False`
  - This indicates that the update failed
1. Outside of the `if` statement body, on the next line, create a new variable named `update_review`
1. Set `update_review` to `db[update_db_key]`
  - This will hold the review object the user wants to update

The code for this part should look something like this:

```py
update_db_key = 'review_' + review_id
if update_db_key not in db.keys():
  return False

update_review = db[update_db_key]
```

### Function Definition - Setting the New Review
Now that the review has been retrieved from the database, it's time to update it. Set the object values based on the parameters, and then set the db value.

1. On the next line, set the `'score'` of `update_review` to `score`
1. Under that, set the `'text'` of `'update_review'` to `text`
1. Next, set `db[update_db_key]` to `update_review`
  - This updates the value in the database
1. Finish out the function by returning `True`

The code for the function should look something like this:

```py
def update_review(review_id, score, text):
  update_db_key = 'review_' + review_id
  if update_db_key not in db.keys():
    return False

  update_review = db[update_db_key]
  update_review['score'] = score
  update_review['text'] = text

  db[update_db_key] = update_review
  return True
```

### Calling the Function
All that's left for updating is calling the function in the proper place.

1. Open the **main.py** file for editing
1. Find the `prompt_for_update_review` function definition
1. In the body of `prompt_for_update_review`, find the comment that says `# Actually update the review`
1. Under that, replace the `False` with a call to the `reviews.update_review` function  
  - Pass in the `update_id`, `score`, and `text`
1. Run the code, and verify that it is possible to update an existing review!

The code to call the function should look something like this:

```py
# Actually update the review
success = reviews.update_review(update_id, score, text)
```

At this point, there is only one part of CRUD remaining: **D**elete.

## [DELETE] Deleting a Review
If a user wants to delete a review, they should be able to provide the ID and the program should delete the review from the database.

### Function Definition
The function for deleting a review will be quite similar to the `update_review` function.

1. Open the **reviews.py** file for editing
1. At the bottom, define a new function named `delete_review`
  - This should take in `review_id` as a parameter
1. In the body of the function, make a new variable named `delete_db_key`
1. Set `delete_db_key` to `'review_' + review_id`
1. On the next line, create an `if` statement checking if the key is NOT in the database
  - This is similar to the `update_review` function
1. In the body of the `if`, return `False` to indicate failure
1. Under that, use `del db[delete_db_key]` to delete the value from the database
1. Under _that_, return `True` to indicate success

The code should look something like this:

```py
def delete_review(review_id):
  delete_db_key = 'review_' + review_id
  if delete_db_key not in db.keys():
    return False

  del db[delete_db_key]
  return True
```

### Calling the Function
Now all that's left is calling the `delete_review` function.

1. Open the **main.py** file for editing
1. Find the `prompt_for_delete_review` function
1. In the body of that function, find the comment that says `# Actually delete the review`
1. Under that, replace the `False` with a call to `reviews.delete_review`
  - Pass in `review_id` as an argument
1. Run the code, and verify that it is possible to delete a review!

The code to call the function should look something like this:

```py
# Actually delete the review
success = reviews.delete_review(delete_id)
```

And that's it! Now the app has complete CRUD functionality.

## Final Code - reviews.py File
The code in the **reviews.py** file should look something like this:

```py
from replit import db

def clear_all():
  for key in db.keys():
    del db[key]

def add_review(restaurant, score, text):
  id_for_new_review = 0

  if 'next_id' in db.keys():
    id_for_new_review = db['next_id']
  
  db['next_id'] = id_for_new_review + 1

  new_db_key = 'review_{0}'.format(id_for_new_review)

  db[new_db_key] = {
    'restaurant': restaurant,
    'score': score,
    'text': text
  }

def get_reviews():
  all_reviews = []
  for key in db.prefix('review_'):
    review_dict = db[key]
    review_dict['id'] = key.replace('review_', '')
    all_reviews.append(review_dict)
  
  return all_reviews

def update_review(review_id, score, text):
  update_db_key = 'review_' + review_id
  if update_db_key not in db.keys():
    return False

  update_review = db[update_db_key]
  update_review['score'] = score
  update_review['text'] = text

  db[update_db_key] = update_review
  return True

def delete_review(review_id):
  delete_db_key = 'review_' + review_id
  if delete_db_key not in db.keys():
    return False

  del db[delete_db_key]
  return True
```

## Next Steps
While this app may be quite simple, it demonstrates some of the key capabilities of the Repl.it database. Working from these fundamentals, it is possible to build almost anything. Databases can be incorporated into any type of app, be it a web server, a game, a discord bot, or anything else.

Feel free to experiment further with the database functionality. If desired, there are some guided [challenges](DatabaseChallenges.md) to complete as well.