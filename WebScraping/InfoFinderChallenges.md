# Info Finder Challenges
After completing the [code-along](InfoFinderCodeAlong.md), attempt the challenges below.

## _Optional Practice: Bug Fixing_
Find and fix all of the bugs in the programs below. Note that the projects may have multiple bugs - fix all of them!

- [Bug 1](https://replit.com/@HylandOutreach/WSBug-1)
- [Bug 2](https://replit.com/@HylandOutreach/WSBug-2)
- [Bug 3](https://replit.com/@HylandOutreach/WSBug-3)
- [Bug 4](https://replit.com/@HylandOutreach/WSBug-4)

## 1. All Paragraphs
Get back into the Info Finder code. Update it so that instead of simply displaying the first paragraph, it displays all of them.

### Updating the Function
1. Find the `get_information` function in the code
1. In the body of the function, find the `for paragraph in paragraphs` loop
1. Above the loop, create a new variable named `para_texts`
1. Set the variable equal to a new empty list: `[]`
    - This will hold the text from each paragraph
1. In the body of the loop, find the `if clean_text:` statement
1. In the body of the `if`, remove the `return` statement
1. In its place, add `clean_text` to the `para_texts` list
1. Outside of the `for` loop, remove the `return "No Info..."` statement
1. In its place, return the `para_texts` list

The program won't work just yet... it will be necessary to update the call to the `get_information` function.

### Updating the Call
1. Find where the `get_information` function is _called_
1. Change the variable to be named `info_paras`
1. Create a new `for` loop to loop through each paragraph text
1. For each text, wrap it in a call to the `fill` function and print it
1. Above the loop, create an `if` statement
1. For the condition, check if `len(info_paras)` is `0`
1. If it is, print a message saying "No Information Found"

Run the program and verify that all the paragraphs appear!

### BONUS: Custom Number of Paragraphs
Instead of simply printing out all of the paragraphs, ask the user how many to print! In the `for` loop body, after printing each paragraph, ask the user if they would like to continue. If they choose not to continue, `break` out of the loop.

## 2. Printing a Table of Contents
In addition to finding the paragraphs of information on each page, find the table of contents information.

1. In the `get_information` function, find the `html_document` variable
1. Under that variable, create a variable named `toc_search`
1. Set the `toc_search` variable to be a new dictionary: `{}`
1. In the `toc_search` dictionary, add a key of `"id"` with a value of `"toc"`
1. Under that, create a variable named `toc`
1. Set the `toc` variable to equal a call to `html_document.find`
1. For the `find` call, pass in `"div"` for the element type as the first parameter
1. For the second parameter, pass in the `toc_search` variable
1. Under that, create a variable named `toc_text`
1. Set the `toc_text` variable to equal `toc.get_text()`
    - This will return the text content for the table of contents
1. Finally, print out the `toc_text` variable

Run the code, enter a search term, and verify that the table of contents text appears!

## 3. Philosophy Game
>This challenge will be quite challenging.

One interesting thing about Wikipedia articles is that if you click on the first non-parenthesized, non-italicized link on the page, and repeat the process, it will almost always lead to the Philosophy page. Check out [this article](https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy) for more information. There is also this video about the subject:

<iframe width="100%" height="450px" src="https://www.youtube.com/embed/Q2DdmEBXTpo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Recreate the philosophy game using a Python script! The program should work as follows:

- Ask the user for a page to visit
- Load the page using requests/BeautifulSoup
- Find the first link on the page
  - Avoid references to the same page, and citation links
  - For an extra challenge, avoid parenthetical links as well
- Load the page at the new URL
- Repeat the process!

Note that "Philosophy" may be unreachable if parenthetical links are included. It will still be interesting to see where the journey goes though!

## 4. Scraping Another Webpage
>This challenge could be challenging depending on the website.

Experiment with different websites! Try to extract data from an interesting place. Try to make it dynamic; create programs that ask the user what to do. Theoretically, any website could be scraped; it's all about looking at the HTML and figuring out how to grab the information.
