# HTML Review Warm-up Activity
Complete the activity below to review some HTML and CSS concepts.

## Getting Started
1. Open the [starter Repl project](https://replit.com/@HylandOutreach/WebScrapingWarmUp)
1. Fork the project, making sure to be logged in
1. Run the code to see how it works so far

## Updating the HTML
Update the content on the page by changing some HTML.

1. Find the "footer" code in the HTML - it says "Thank you for visiting."
1. Update the text so that it ends with an exclamation point instead
1. Find the paragraph with all the information about crochet
1. Under the existing paragraph, there is an empty `<p></p>`
1. Within the `<p>` and `</p>`, copy and paste the following text:  
    ```
    Knitted textiles survive from as early as the 11th century CE,
    but the first substantive evidence of crocheted fabric emerges
    in Europe during the 19th century. Earlier work identified as
    crochet was commonly made by nålebinding, a different looped
    yarn technique.
    ```
1. Find the `img` elements in the code - within the `div`
1. Make a space under the final `img` tag
1. Add in another image using this HTML code:  
    ```html
    <img src="https://m.media-amazon.com/images/I/81tM2sqAdkL._CR0,137,1283,1283_UX256.jpg">
    ```
1. Run the project again and see the changes!
    - The footer should have an exclamation point
    - A second paragraph of information should appear
    - A third image should appear

## Updating the CSS
Update the styles on the page by changing some CSS. First, notice the existing rulesets within the `<style></style>` element at the top of the page:

```css
#footer { } /* the div that contains the footer text */
#footer p { } /* the paragraph within the footer div */
```

In CSS, elements can be selected by `id` with `#`, or by `class` with `.`. From there, child elements can be selected by adding a space and the element name. None of this is terribly important for web scraping, but some of the concepts will be helpful to understand.

1. Under the existing rulesets within the `<style></style>` element, create a new line
1. Create a new ruleset to select all `p` elements within the `<div id="content>`  
    - Possible with `#content p {}`
1. In the ruleset, set the `font-size` property to `20px`
1. Under that ruleset, create another new line
1. Create a new ruleset to select the `<div class="images">` element
    - Possible with `.images {}`
1. In the ruleset, set the `text-align` property to `center`
1. Under that ruleset, create another new line
1. Create a new ruleset to select all of the `img` elements within the `<div class="images">` element
    - Possible with `.images img {}`
1. In the ruleset, set the `width` property to `32%`
1. Run the project again and see the changes!
    - The paragraph text should be larger
    - The images should stay centered
    - The images should also resize with the page width

## Final Code
```html
<html>
    <style>
        #footer {
            background: #444;
            padding: 5px;
        }

        #footer p {
            color: white;
            font-size: 12px;
            text-align: center;
        }

        #content p {
            font-size: 20px;
        }

        .images {
            text-align: center;
        }

        .images img {
            width: 32%;
        }
    </style>
    <body>
        <p>
            <i>Note: This page is under construction</i>
            <img src="https://i.imgur.com/EHfcXx1.png">
        </p>
        <div id="content">
            <h1>Crochet</h1>
            <p>Crochet is a process of creating textiles by using a crochet hook to interlock loops of yarn, thread, or strands of other materials. The name is derived from the French term <i>crochet</i>, meaning “small hook.” Hooks can be made from a variety of materials, such as metal, wood, bamboo, or plastic. The key difference between crochet and knitting, beyond the implements used for their production, is that each stitch in crochet is completed before the next one is begun, while knitting keeps many stitches open at a time. Some variant forms of crochet, such as Tunisian crochet and broomstick lace, do keep multiple crochet stitches open at a time.</p>
            <p>Knitted textiles survive from as early as the 11th century CE, but the first substantive evidence of crocheted fabric emerges in Europe during the 19th century. Earlier work identified as crochet was commonly made by nålebinding, a different looped yarn technique.</p>
            <div class="images">
                <img src="https://static-s.aa-cdn.net/img/ios/1138327741/aed1f8a204eebe433d78c548870bcfad?v=1">
                <img src="https://pbs.twimg.com/profile_images/732212337181085696/06UJSCL3.jpg">
                <img src="https://m.media-amazon.com/images/I/81tM2sqAdkL._CR0,137,1283,1283_UX256.jpg">
            </div>
        </div>
        <div id="footer">
            <p>Thank you for visiting!</p>
        </div>
    </body>
</html>
```
