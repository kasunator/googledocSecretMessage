# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:37:46 2025

@author: KBeddewela
<table ..  marks the start of table
</table> marks end of table, 8 bytes long

</tr> marks endof row
</td> marks end of column 

"""
import requests as rq

short_doc = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
long_doc = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"

response = rq.get(short_doc)
response_str = str(response.content, 'UTF-8') 
#print(response.content)
#print(type(response_str))
""" starting and end of the table is marked by <table  .. </table>"""
start_index_table = response_str.find("<table")
end_index_table = response_str.find("</table>")
#print(start_index_table)
#print(end_index_table)
response_str = response_str[start_index_table: end_index_table + 8 ] # i.e </table> is 9 bytes long
#print(response_str)

""" Now lets remove the table header , by finding the first row which is the header
and then removing it
"""
header_end_idx = response_str.find("</tr>")
response_str = response_str[header_end_idx + len("</tr>") : len(response_str) ]
print(response_str)