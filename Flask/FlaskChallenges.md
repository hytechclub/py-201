# Flask Challenges
After completing the [code-along](FlaskCodeAlong.md), attempt the challenges below. **Note that students will be expected to present their websites, so complete the first challenge (new jokes) at minimum!**

## 1. New Jokes
Replace the existing `jokes` list with a new list; either write your own, or search for some [existing jokes](https://parade.com/1041830/marynliles/clean-jokes/)! Make sure the jokes are appropriate.

After updating the jokes, change up some of the styles. Open the **static/style.css** file, and change the following:

- background color
- text color
- font

## 2. Quotes
A website about jokes is nice, but it is a little restrictive. Update it so that it provides a random _quote_ in addition to a random joke. This way, there are a lot more options for what to show. Note that this will be extremely similar to the Joke page; for the purposes of this exercise, much of it can be copied and pasted.

### Python Code
Open the **main.py** file, and make the following changes:

1. Under the `jokes` list, create a new list named `quotes`
1. For now, add a couple of quotes to the list (more can be added later):  
    - "You miss 100% of the shots you don't take."
    - "The future ain't what it used to be."
1. Under the `joke` function, define a function named `quote`  
    - It should have no parameters
1. Above the `quote` function, add the `@app.route` line, pointing to `"/quote"`
1. In the body of the `quote` function, create a variable named `random_quote`
1. Set the `random_quote` variable to `choice(quotes)`
1. Under that, return a call to `render_template`  
    - Pass in `"quote.html"` and `quote=random_quote`
1. Check that the `quote` function matches the `joke` function for the most part

Note that this will not work just yet; there is currently no **quote.html** file.

### HTML Template Code
The next step is to add a **quote.html** file and update the **home.html** file.

1. In the **templates** folder, create a new file named **quote.html**
1. Copy the code from the **joke.html** file into the **quote.html** file
1. Change the `h1` text so that it says "Quote Page"
1. Change the `p` text so that it says "Here is a quote for you"
1. Change the {% raw %}`{{ joke }}`{% endraw %} to {% raw %}`{{ quote }}`{% endraw %} 
   - This is because a different value is passed to `render_template` in the Python
1. Change the first `a` text so that it says "Get another quote"
1. Open the **home.html** file
1. Under the existing `a` element, add another `<a></a>`
1. Set the `href` of the second `a` to point to `/quote`
1. Make the text of the second `a` say "Get a quote"

Run the program and verify that it is possible to go to the Quote Page!

### Find More Quotes
Now the fun part: find more quotes! These can be quotes from movies, books, songs, or whatever else. Update the `quotes` list in the **main.py** file so that it contains some updated quotes.

## 3. A Hello Page
Create another page - a "Hello" page - that greets the user based on a name passed in the URL. This is possible using [URL Converters](https://exploreflask.com/en/latest/views.html#built-in-converters). These can turn values from URLs into Python variables.

By the end of this challenge, the user should be go to a URL like "proj.name.repl.co/hello/**Joan**" and the page should say "Hello Joan!" It should work for any name passed in the URL.

### Python Code
First, change the code in the **main.py** file.

1. Under the existing route functions, define a new function named `hello`
1. Give the `hello` function one parameter: `username`
1. Above the function, add the `@app.route` decorator
1. For the URL, pass in `/hello/<username>`  
    - Note the `<>` around `username` - that means it will be the parameter!
1. In the body of the `hello` function, add a `return` statement
1. Return `render_template`, passing in `"hello.html"` and `name=username`
    - This will pass the URL `username` variable into the `"hello.html"` template

This will not work just yet, because there is no file named **hello.html**.

### HTML Template Code
Next, create a proper HTML template to render.

1. In the **templates** folder, create a file named **hello.html**
1. Open the file, and add basic boiler-plate HTML elements to it: `html`, `body`
1. Between the `<body>` and `</body>` add a `<h1></h1>`
1. Make the text say {% raw %}`Hello {{ name }}!`{% endraw %}
    - This will render the `name` passed in the Python code
1. Under the `h1`, add a `p` saying "I hope you enjoy the site"

Now the new route should work! It will not be linked from anywhere, but that should not be a problem.

### Testing the Hello Page
Testing the page is easiest when the site is opened in a new window:

![](https://i.imgur.com/TiUlhBV.png)

After that, append `/hello/Name` to see it say hello! Verify that it can say hello to any name provided in the URL.

## 4. Make Something New
Use Flask to create a completely new website! There are several options. If desired, take a look at [this tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates) to learn some more advanced template concepts, which will make it possible to do a lot more with Flask!

## _Optional Practice: Bug Fixing_
Find and fix all of the bugs in the programs below. Note that the projects may have multiple bugs - fix all of them!

- [Bug 1](https://replit.com/@JosephMaxwell/FlaskBug-1#main.py)
- [Bug 2](https://replit.com/@JosephMaxwell/FlaskBug-2#main.py)
- [Bug 3](https://replit.com/@JosephMaxwell/FlaskBug-3#main.py)
- [Bug 4](https://replit.com/@JosephMaxwell/FlaskBug-4#main.py)
