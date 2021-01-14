# Information Finder
In this activity, create a program that uses Wikipedia to find information. The goal is for the user to enter a search term, and then show the first paragraph of the Wikipedia article for that subject.

## Setting Up
1. Go to [repl.it](https://repl.it)
1. Log in
1. Create a new Python Repl project named "Info Finder"

## Basic Loop
Before figuring out how to use Wikipedia, create the basic loop for the program.

1. At the top of the **main.py** file, create a `while True` loop
1. In the indented body of the `while` loop, use `print` to show a welcome message
1. Under that, create a variable named `search`
1. Set the `search` variable to the result of an `input` asking for a search term
1. Under that, create a variable named `keep_going`
1. Set the `keep_going` variable to the result of an `input` asking if the user would like to continue (y/n)
1. Under that, create an `if` statement checking if `keep_going` is NOT equal to `"y"`
1. In the body of the `if`, print a "Goodbye" message and `break`

Run the program, and verify that the loop can continue as long as the user wants!

```py
while True:
    print("Welcome to text-based Wikipedia!\n")
    search = input("Enter a search term: ")

    keep_going = input("\nWould you like to enter another term (y/n)? ")
    print("")

    if keep_going != "y":
        print("Goodbye!")
        break
```

## Info Function
Next, build out the structure for a `get_information` function. This function will not do anything yet, but eventually it will.

### Defining the Function
First, define the function.

1. Above the `while` loop, define a new function named `get_information`
1. Give one parameter to the `get_information` function: `search_term`
1. In the body of the `get_information` function, simply return `"No information found"` for now

```py
def get_information(search_term):	
    return "No information found"
```

### Calling the Function
Next, call the function in the code.

1. Find the line between the `search` and `keep_going` variable initializations in the `while` loop body
1. At that spot, create a variable named `information`
1. Set the variable to the result of a call to the `get_information` function
1. Pass in `search` as the argument to the function
1. Under that, use `print` to show a message saying "Here's what I found:"
1. Under _that_, print out the `information` variable

```py
information = get_information(search)
print("\nHere's what I found:")
print(information)
```

Run the program, and verify that the "No information found" message properly appears - that means the function is being called!

## Requesting the HTML
Now it's time to go grab some information from the web. At the very top of the **main.py** file, add the following code to import the `requests` library:

```py
import requests
```

More information about this library is available [here](https://www.w3schools.com/python/module_requests.asp).

### Retrieving Information Manually
As a human being, it's not too hard to go to Wikipedia and find some information. Giving that ability to a computer program is a little less straightforward, but it is certainly possible!

As a human, it would make sense to go to [Wikipedia](https://wikipedia.org) and type something into the search bar. For example, typing in "Apple" would lead to this page:

<iframe src="https://en.wikipedia.org/wiki/Apple" width="100%" height="450px"></iframe>

Behind the scenes, that actually sends the web browser to this url: https://en.wikipedia.org/w/index.php?search=apple

In fact, anything can be appended to the end of that URL in order to find the corresponding Wikipedia page! This will be extremely helpful for the Info Finder.

### Retrieving Information in Python
Using the **requests** library, it is possible to pull down all of the HTML code from a URL. Update the `get_information` function so that it prints out some raw HTML (for now).

1. Find the `get_information` function, and make a new line at the _top_ of the body
1. Create a variable named `url`
1. Set `url` to this string: `"https://en.wikipedia.org/w/index.php?search="`
1. At the end of the line, add `+ search_term` to add on the search term from the user
    - This way, the URL will always reflect what the user hopes to find
1. Under that, create a variable named `response`
1. Set the `response` variable to `requests.get(url)`
    - Here, the `requests.get` function is able to retrieve the info from the web
1. Under that, create a variable named `html_text`
1. Set the `html_text` variable to equal `response.text`
    - This gets the raw HTML from the response
1. Under that, use `print` to print the `html_text` variable
1. Run the program, enter a search term, and verify that a mess of HTML appears!

```py
url = "https://en.wikipedia.org/w/index.php?search=" + search_term

response = requests.get(url)
html_text = response.text
print(html_text)
```

## Beautiful Soup
Now the program has a bunch of HTML, but it's not very readable. It's time to parse it using [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), a Python library designed to help extract information from HTML text!

Right under the first `import` statement in the code, add the following line:

```py
from bs4 import BeautifulSoup
```

Before jumping into the code, think about what is necessary to find in the HTML.

### Looking at the HTML
Every Wikipedia page is a little different, so it's important to make sure the HTML parsing solution works for all (or at least the majority) of them. Take a look at some of the HTML for a page.

1. Open a separate browser window
1. Go to the [Wikipedia page for Apple](https://en.wikipedia.org/wiki/Apple)
1. Right click somewhere on the first paragraph
1. Select "Inspect" to open Developer Tools
1. Try to find the first paragraph text in the HTML
    - It may be a little jumbled, but the text should be there
1. Notice that the text is within a `p` element
1. Notice that that `p` element is within a `div` element
1. Notice that the `div` element has a `class` attribute of `mw-parser-output`
1. Notice that the important `p` is not the first `p` within that `div`

All of this investigation should help when writing the code.

### Parsing the HTML in Python
Now it's time to get into the code!

1. Find the spot in the `find_information` function where `html_text` is printed
1. Remove that line as it is no longer necessary
1. In its place, create a new variable named `html_document`
1. Set the `html_document` variable to the result of a call to the `BeautifulSoup` function
    - Pass in `html_text` as the first parameter
    - Pass in `"html.parser"` (in quotes) as the second parameter
1. Create a new variable named `search_criteria`
    - Consider what the program needs to find first
1. Set the `search_criteria` variable to a new dictionary
1. Add a key of `"class"` to the dictionary, with a value of `"mw-parser-output"`
    - This will be able to find the appropriate `div` in the HTML
1. Under that, create a variable named `content_div`
1. Set the `content_div` variable to `html_document.find("div", search_criteria)`
    - This searches the `html_document` for `div` elements with a `class` of `mw-parser-output`
1. Under that, create a new variable named `paragraphs`
1. Set the `paragraphs` variable to `content_div.find_all("p")`
    - This will be all of the `p` elements within the `div`

```py
html_document = BeautifulSoup(html_text, "html.parser")

search_criteria = {
    "class": "mw-parser-output"
}

content_div = html_document.find("div", search_criteria)
paragraphs = content_div.find_all("p")
```

## The Right Paragraph
Now all the possible paragraphs have been found, but only the first non-empty one is needed. Loop through the paragraphs, and `return` the text for the first non-empty one!

1. Under the `paragraphs` variable, create a `for` loop
1. Loop through each `paragraph` in `paragraphs`
1. In the indented body of the `for` loop, create a variable named `p_text`
1. Set the `p_text` variable to `paragraph.get_text()`
    - This will hold the raw text for the paragraph
1. Under that, create a variable named `clean_text`
1. Set the `clean_text` variable to `p_text.strip()`
    - This will remove any whitespace from the text
1. Under that, still within the `for` body, create an `if` statement
1. For the condition of the `if`, simply put `clean_text`
    - This will be `True` for all non-empty string values
1. In the indented body of the `if`: `return clean_text`
1. Run the code, enter a search term, and verify that the first paragraph appears!

```py
for paragraph in paragraphs:
    p_text = paragraph.get_text()
    clean_text = p_text.strip()
    
    if clean_text:
        return clean_text
```

## Nice Printing
There is one last thing to make the program a little nicer to use. Currently, the text will break a new line in the middle of a word. This is not ideal! Luckily, there is another Python library to handle it. At the top of the file, along with the other `import`s, add the following:

```py
from textwrap import fill
```

The `fill` function will add newline characters in between strings so that they print out a little nicer. More information can be found [here](https://docs.python.org/3/library/textwrap.html#textwrap.fill).

Find the part of the code where the `information` variable is printed, and replace it with this:

```py
print(fill(information))
```

Run the program again, and verify that all information printed looks nicer!

## Final Code
```py
import requests
from bs4 import BeautifulSoup
from textwrap import fill

def get_information(search_term):
    url = "https://en.wikipedia.org/w/index.php?search=" + search_term

    response = requests.get(url)
    html_text = response.text
    html_document = BeautifulSoup(html_text, "html.parser")

    search_criteria = {
        "class": "mw-parser-output"
    }

    content_div = html_document.find("div", search_criteria)
    paragraphs = content_div.find_all("p")

    for paragraph in paragraphs:
        p_text = paragraph.get_text()
        clean_text = p_text.strip()
        
        if clean_text:
            return clean_text

    return "No information found"

while True:
    print("Welcome to text-based Wikipedia!\n")
    search = input("Enter a search term: ")

    information = get_information(search)
    print("\nHere's what I found:")
    print(fill(information))

    keep_going = input("\nWould you like to enter another term (y/n)? ")
    print("")

    if keep_going != "y":
        print("Goodbye!")
        break
```

## Challenges
After the activity, start working on the [Info Finder Challenges](InfoFinderChallenges.md).