# Flask Basics Warm-up Activity
[Flask](https://flask.palletsprojects.com/en/1.1.x/foreword/) is a Python web framework - a tool for creating web applications with Python. Read through some of the basic concepts to become familiar with them.

## Flask Boiler-Plate and Repl.it
When creating a new Python project on [repl.it](https://repl.it), it is possible to load some Flask boiler-plate code. Running that code will spin up a webserver. Repl.it hosts the server and navigates to the website. It looks like this:

<iframe height="1000px" width="100%" src="https://repl.it/@JosephMaxwell/FlaskBoilerPlate?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

## Routing
When building a web app, it is important to determine which things happen at which URLs. This is called _routing_.

One of the most important parts of the boiler-plate code is the following _decorator_:

```py
@app.route('/')
```

Adding that line above a function will tell the Flask app that when the user goes to the root URL, the function below it should run.

To create another page, a developer would use a _different_ `@app.route` value. For example, take a look at the following code:

```py
@app.route('/about')
def about_page():
    return "Here is some information about the site"
```

That decorator means that if someone went to the base URL with `/about` at the end, it would run the `about_page` function and display the text returned.

There are some interesting ways to extend the routing capabilities, but for now, keep it simple: `@app.route` tells the app which functions map to which pages.

## HTML Templates
In the boiler-plate code, the app only displays raw text. This may be all that's necessary, but typically, it would make sense to render some HTML. That's where templates come in.

A _template_ is a file that contains static data (like HTML) as well as placeholders for dynamic data (more on that later). For now, focus on the static data part.

In a Repl project for a full-fledged Flask app, there will likely be a folder named **templates**. The name is very important, because that specific folder is where Flask looks for template files. For example, if there were a file named **home.html** in the **templates** folder, it could be rendered by the app.

### `render_template`
In order to use templates, it is necessary to import the `render_template` function from Flask. Like this:

```py
from flask import Flask, render_template
```

Then, that function can be used to render some HTML! Instead of returning regular text like "Hello world," the `render_template` function takes in a filename and returns the rendered HTML. For example:

```py
@app.route('/')
def home():
    return render_template("home.html")
```

The code above would cause the homepage (root url) to display the rendered contents of the **home.html** file (assuming it is in the **templates** folder)!

Templates make it much easier to work with HTML in Flask; instead of having to put a bunch of HTML within Python strings, it can be contained in HTML files.

## Passing Variables
One of the main capabilities of templates in Flask is the ability to dynamically render templates. This is possible by passing variables as [keyword arguments](https://treyhunner.com/2018/04/keyword-arguments-in-python/). This way, instead of creating many different functions and templates, it can be possible to create one of each and simply change up the variables passed.

### In the Python Code
On the Python side, passing a variable to a template looks like this:

```py
render_template("home.html", name="Elaine")
```

That second `name` argument in the call to the `render_template` function means that the value will be accessible from the template! This won't matter too much if it's a static value, but there is potential to make it more dynamic.

### In the HTML Template
On the HTML side, _using_ a variable in a template looks like this:

{% raw %}
```html
<p>Hello, {{ name }}!</p>
```
{% endraw %}

Enclosing something in double curly brackets, {% raw %}`{{`{% endraw %} and {% raw %}`}}`{% endraw %}, means that Flask will look for a dynamic value by that name. In the example from above, the finally-rendered HTML would look like this:

```html
<p>Hello, Elaine!</p>
```

The `render_template` function goes in and _replaces_ the {% raw %}`{{ name }}`{% endraw %} in the template with the _value_ of the `name` variable. That way, the same page can say hello to any number of different names!

## Summary
Here are some important notes to remember:

- **Flask** is a web development framework for Python
- Different pages can be **routed** to Python functions using the `@app.route` decorator
- HTML can be **rendered** from Python using the `render_template` function
- Variables can be **passed** to the template using keyword arguments
- Variables can be **referenced** within a template between {% raw %}`{{`{% endraw %} and {% raw %}`}}`{% endraw %}

Don't worry if this is a little overwhelming - there will be plenty of time to practice!