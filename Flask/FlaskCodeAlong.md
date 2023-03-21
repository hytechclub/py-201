# Random Joke Website
In this activity, create a Flask Web Server that serves a random joke website. The goal is for the user to be able to see a random joke every time the joke page loads.

## Setting Up
Luckily, there is code for a basic Flask app built into Replit through an example.

1. Go to [Replit](https://replit.com)
1. Log in
1. Create a new Python Repl project named "Random Joke Website"
1. At the top of the **main.py** file, click on the "examples" link  
    ![](https://i.imgur.com/LL0KY6R.png)
1. From there, select the "Server (Flask)" option  
    ![](https://i.imgur.com/k0x5xlB.png)
1. Run the program to see the boiler-plate Flask app render!

### The Code So Far
The boiler-plate code should look like this:

```py
from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)
```

There aren't many lines, but they may be a little confusing. Here's a quick breakdown of what each line does:

```py
from flask import Flask # imports the Flask library
app = Flask('app') # initializes the Flask app variable

@app.route('/') # sets a route for the app - the root
def hello_world(): # defines a function to handle that route
    return 'Hello, World!' # returns text to display

app.run(host='0.0.0.0', port=8080) # runs the app locally
```

## Rendering HTML
Currently, the homepage has some simple text. However, it is possible to update that text to display HTML instead!

Update the `hello_world` function so that it returns `<h1>Hello, World!</h1>`. Run the program to see the HTML render!

### Creating an HTML File
This is working, but it would be difficult to write an entire HTML document in Python. Luckily, the `Flask` library has the ability to render full HTML files too. The first step is to create one.

1. On the left side of the Replit page, click the "Add folder" icon  
    ![](https://i.imgur.com/8xPcA41.png)
1. Enter "templates" for the folder name, and press **Enter**  
    ![](https://i.imgur.com/gxAoC8N.png)
1. Click the three dots by the "templates" folder, and then the "Add file" button  
    ![](https://i.imgur.com/Oh396ma.png)
1. Enter "home.html" for the name of the file

Now there should be a **templates** folder, and a file named **home.html** within that folder. The name of the folder is important; make sure it is **templates**.

Next, open up the **home.html** file, and add the following code:

**templates/home.html**
```html
<html>
	<body>
        <h1>Welcome to my Website</h1>
        <p>This is one of the greatest websites of all time.</p>
	</body>
</html>
```

This is a simple page, but it is much easier to have the code in a file instead of in a string!

### Using the HTML File
The next step is using the HTML file in the Flask app.

1. Open the **main.py** file
1. At the top of the file, find the `from flask` line
1. At the end of the line, add `, render_template`  
    ```py
    from flask import Flask, render_template
    ```
1. Find the `hello_world` function, and rename it `home`
1. In the body of the `home` function, remove the current `return`
1. In its place, call the `render_template` function, passing in `"home.html"`
1. Return the result of the function call
1. Stop the server and run it again to see the updated home page!

**main.py**
```py
from flask import Flask, render_template
app = Flask('app')

@app.route('/')
def home():
    return render_template("home.html")

app.run(host='0.0.0.0', port=8080)
```

## Adding Another Page
Adding additional pages to the web server will be very similar to creating the first page. This second page will have a joke for the user.

### A New HTML File
The first step is creating a new HTML file. Add a file named **joke.html** to the **templates** folder. Note that the file _must_ be within the proper folder; otherwise it will not work. Once the file has been created, add the following HTML code:

**templates/joke.html**
```html
<html>
    <body>
        <h1>Joke Page</h1>
        <p>Here is a joke for you:</p>
        <blockquote>
            How do you tell when you're out of invisible ink?
        </blockquote>
        <p><a href="/">Go back home</a></p>
    </body>
</html>
```

### A New Route Function
The next step is to create a new route function for the joke page.

1. In the **main.py** file, define a new function named `joke`
1. In the body of the `joke` function, call the `render_template` function
1. In the call, pass in `"joke.html"` as the parameter
1. Return the result of the call
1. On the line above the function definition, add an `@app.route`
1. For the route argument, use `'/joke'`
    - This means the page will be available at **{examplename.name}.repl.co/joke**

Run the project, and notice that the homepage still appears. That's what's supposed to be happening. What's missing is that the homepage has no link to the new page!

### Updating the home.html File
Open up the **templates/home.html** file, and find the `<p></p>`. Right underneath it, add the following HTML:

**templates/home.html**
```html
<a href="/joke">Get a Joke</a>
```

With that, a link to the joke page should appear! Try running the project again. Verify that it is possible to click the link and go to the joke page!

## A Random Joke
Now comes the fun part. The website so far is not bad, but it would be a lot better if there were more jokes! Update the server so that, instead of only displaying one joke, it displays a random joke every time the joke page loads.

### Setup
Python has a built-in **random** library to help with all things random. At the top of the **main.py** file, right under the other `import`, add the following line:

```py
from random import choice
```

That will import the `choice` function, which can [choose a random item from a list](https://docs.python.org/3/library/random.html#random.choice). It is extremely helpful for this situation. All that's missing is a list!

To save time, copy the following `jokes` list into the **main.py** file (under the `app` variable):

```py
jokes = [
    "I saw a bank that said '24 Hour Banking,' but I don't have that much time.",
    "I went to a general store. They wouldn't let me buy anything specifically.",
    "A computer once beat me at chess, but it was no match for me at kick boxing.",
    "How do you tell when you’re out of invisible ink?",
    "Saying 'I'm sorry' is the same as saying 'I apologize.' Except at a funeral.",
    "I went into a clothes store and a lady came up to me and said 'if you need anything, I'm Jill'. I never met anyone with a conditional identity before.",
    "I find that a duck's opinion of me is very much influenced over whether or not I have bread.",
    "I haven't slept for 10 days... because that would be too long.",
    "I'm against picketing, but I don't know how to show it."
]
```

The program should pick a random joke from the list.

### Creating the Random Joke
The next step is to actually use the `jokes` list!

1. Find the `joke` function
1. Make a new line at the top of the body of the function
1. In the body, create a variable named `random_joke`
1. Set the variable to equal a call to the `choice` function
    - Pass in the `jokes` list as the variable
1. In the call to `render_template`, add a comma after the first argument
1. Add `joke=random_joke` to pass in the `random_joke` to the template
    - This is an example of a [keyword argument](https://www.w3schools.com/python/gloss_python_function_keyword_arguments.asp)

```py
@app.route('/joke')
def joke():
    random_joke = choice(jokes)
    return render_template("joke.html", joke=random_joke)
```

Now the **joke.html** template will have access to the random joke!

### Displaying the Random Joke
Now that the joke is properly passed to the template, it will be possible to display it in the HTML.

1. Open the **templates/joke.html** file
1. Find the existing joke text
1. Replace the text with {% raw %}`{{ joke }}`{% endraw %}
    - Because the `joke` argument was passed in `render_template`, this will contain a joke!
1. Under the `<blockquote></blockquote>`, create a `<p></p>` element
1. Within the `<p>` and `</p>`, create an `<a></a>` element
1. Set the `href` attribute of the `a` to `"?"`
    - This will cause a refresh when the link is clicked
1. Within the `a`, add the text "Get another joke"

**templates/joke.html**
{% raw %}
```html
<blockquote>
    {{ joke }}
</blockquote>
<p><a href="?">Get another joke</a></p>
```
{% endraw %}

Run the project again and test it out! It should generate a random joke every time the joke page loads.

## Adding Some Style
The last step is to use CSS to add some style to the site! This isn't strictly necessary, but it can make the user experience much more engaging.

### CSS File
First, create a CSS file in the proper place.

1. Create a folder named **static**
1. Within that folder, create a file named **style.css**

Add the following code to the file:

**static/style.css**
```css
body {
	font-family: sans-serif;
	background-color: darkgreen;
	color: gold;
}

a {
	color: white;
	text-decoration: none;
}

a:hover {
	font-weight: bold;
}

blockquote {
	border: 1px dotted gold;
	padding: 10px;
	width: 300px;
}
```

### HTML Files
Now, the HTML files must be updated to point to the **static/style.css** file.

Add the following code to the **home.html** and **joke.html** files (within the `<html></html>`, above the `<body>`):
```html
<head>
    <link rel="stylesheet" href="static/style.css">
</head>
```

### Seeing the Website
Sometimes, Replit has issues with static CSS files. This is because they can be cached, which means they don't always refresh with changes.

To help with this, open the Repl project in another tab:
![](https://i.imgur.com/L3KNb5f.png)

From there, it should be possible to press **Ctrl**+**F5** to clear the cache and refresh the page. Verify that the pages are nicely styled!

## Final Code
Review the final code for each file. Make sure to note the folder structure of the project. There is also a [Repl project](hhttps://replit.com/@HylandOutreach/FlaskCodeAlongSimplified) containing the complete web app.

**main.py**
```py
from flask import Flask, render_template
from random import choice
app = Flask('app')

jokes = [
    "I saw a bank that said '24 Hour Banking,' but I don't have that much time.",
    "I went to a general store. They wouldn't let me buy anything specifically.",
    "A computer once beat me at chess, but it was no match for me at kick boxing.",
    "How do you tell when you’re out of invisible ink?",
    "Saying 'I'm sorry' is the same as saying 'I apologize.' Except at a funeral.",
    "I went into a clothes store and a lady came up to me and said 'if you need anything, I'm Jill'. I never met anyone with a conditional identity before.",
    "I find that a duck's opinion of me is very much influenced over whether or not I have bread.",
    "I haven't slept for 10 days... because that would be too long.",
    "I'm against picketing, but I don't know how to show it."
]

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/joke')
def joke():
    random_joke = choice(jokes)
    return render_template("joke.html", joke=random_joke)

app.run(host='0.0.0.0', port=8080)
```

**templates/home.html**
```html
<html>
    <head>
        <link rel="stylesheet" href="static/style.css">
    </head>
    <body>
        <h1>Welcome to my Website</h1>
        <p>This is one of the greatest websites of all time.</p>
        <a href="/joke">Get a Joke</a>
    </body>
</html>
```

**templates/joke.html**
{% raw %}
```html
<html>
    <head>
        <link rel="stylesheet" href="static/style.css">
    </head>
    <body>
        <h1>Joke Page</h1>
        <p>Here is a joke for you:</p>
        <blockquote>
            {{ joke }}
        </blockquote>
        <p><a href="?">Get another joke</a></p>
        <p><a href="/">Go back home</a></p>
    </body>
</html>
```
{% endraw %}

**static/style.css**
```css
body {
	font-family: sans-serif;
	background-color: darkgreen;
	color: gold;
}

a {
	color: white;
	text-decoration: none;
}

a:hover {
	font-weight: bold;
}

blockquote {
	border: 1px dotted gold;
	padding: 10px;
	width: 300px;
}
```

## Challenges
After the activity, start working on the [Flask Challenges](FlaskChallenges.md).
