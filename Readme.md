You are given a Google Doc that contains a list of Unicode characters and their positions in a 2D grid. Your task is to write a function that takes in the URL for such a Google Doc as an argument, retrieves and parses the data in the document, and prints the grid of characters. When printed in a fixed-width font, the characters in the grid will form a graphic showing a sequence of uppercase letters, which is the secret message.

The document specifies the Unicode characters in the grid, along with the x- and y-coordinates of each character.

The minimum possible value of these coordinates is 0. There is no maximum possible value, so the grid can be arbitrarily large.

Any positions in the grid that do not have a specified character should be filled with a space character.

You may use external libraries.

You may write helper functions, but there should be one function that:

Takes in one argument, which is a string containing the URL for the Google Doc with the input data, AND

When called, prints the grid of characters specified by the input data, displaying a graphic of correctly oriented uppercase letters.

use this link as an example:
https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub

and the corresponding output should be the following
█▀▀▀
█▀▀ 
█   



To verify that your code works, please run your function with this URL as its argument:

https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub

What is the secret message encoded by this document? Your answer should only contain uppercase letters.


I wrote a string parser functions that extracts the table information from the data returned by the URL. 
By observing the URL content in source code mode in the browser I found that <tr ...> </tr> are used as markups for the table rows. 
And <td.. > </td> marks the data columns(cells) with in each row. 
We can exactly  extract data within the cell by extracting the string between > and </span> markers.
 After passing the data and extracting the table we found the largest coordinates of the message. 
 By observing the  given smaller example I found that x axis advances from left to right and the y axis advances form bottom to top. i.e. the origin (0,0) 
is at the bottom left of the console after everything is printed. Using the  available table data corresponding characters were inserted into the correct string location.

