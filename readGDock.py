# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:37:46 2025

@author: KBeddewela
<table ..  marks the start of table
</table> marks end of table, 8 bytes long

</tr> marks endof row
</td> marks end of column 
</span> is the delimeter just after data from each column


by oberving the given output and the example table
we can see that
 x goes from left to right 
 y goes from bottom to top
 
i.e. the (0,0) orgin is at the bottom left of the console/screen
"""
import requests as rq

short_doc = "https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub"
long_doc = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"


def extract_data(input_string ):
    val_idx = input_string.find("</span>")
    col1_val = input_string[val_idx -1 : val_idx]
    #print("col val:" + col1_val )
    return col1_val


def extract_data_from_row(row_string):
    col_end_idx = row_string.find("</td>")
    i = 0 
    while col_end_idx != -1:
        col_str = row_string[ : col_end_idx + len("</td>")]
        row_string = row_string[col_end_idx + len("</td>") : ]
        #print("col:" + col_str)
        if i == 0:
            x = extract_data(col_str)
        elif  i == 1:
            y = extract_data(col_str)
        else :
            z =extract_data(col_str)
        i = i+1
        extract_data(col_str)
        col_end_idx = row_string.find("</td>")
    return (x,y,z)        


def extract_rows_from_table(table_string):
    row_end_idx = table_string.find("</tr>")
    data_tuples = []
    while row_end_idx != -1:
        #print("row index:" + str(row_end_idx))
        #print(table_string)
        row_str = table_string[: row_end_idx + len("</tr>") ]
        table_string = table_string[row_end_idx  + len("</tr>") : ]
        #print("row:" + row_str)
        x, y, z = extract_data_from_row(row_str)
        #print("data:" + str(x) +":" + str(y) + ":" + str(z) )
        data_tuples.append((x ,y, z)) #append the data to list
        row_end_idx = table_string.find("</tr>")  
    return data_tuples
    
def find_largest_x(tuple_list):
    largest = 0
    for item in tuple_list:
        int_item = int(item[0]) 
        if largest < int_item:
            largest = int_item
    
    return largest

def find_largest_y(tuple_list):
    largest = 0
    for item in tuple_list:
        int_item = int(item[2]) 
        if largest < int_item:
            largest = int_item
    
    return largest

def check_if_table_has_entry(tuple_list, x , y):
    for item in tuple_list:
        if int(item[2]) == y and int(item[0]) == x:
            entry = item[1]
            #print("match : " + str(x) +":"+ str(y) + ":" + item[1])
            return entry
    return " "
  
  
def build_string_from_list( tuple_list , largest_x , largest_y):
    #build_string = ""
    line_string = ""
    for j in range(largest_y, -1, -1 ):
        for i in range(largest_x + 1):
            line_string +=check_if_table_has_entry(tuple_list, i, j)
        line_string += "\n" #insert \n every end of i, i.e. x line

        #print(line_string)
        
    return line_string



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
#print(response_str)
"""
row_end_idx = response_str.find("</tr>")
row_str = response_str[: row_end_idx + len("</tr>")  ]
print(row_str)
response_str = response_str[row_end_idx  + len("</tr>"): ]
print(response_str) """


"""
row_end_idx = response_str.find("</tr>")
while row_end_idx != -1:
    row_str = response_str[: row_end_idx + len("</tr>") ]
    response_str = response_str[row_end_idx  + len("</tr>") : ]
    print("row:" + row_str)
    #col_end_idx = response_str.find("</td>")
    col_end_idx = row_str.find("</td>")
    while col_end_idx != -1:
        col_str = row_str[ : col_end_idx + len("</td>")]
        row_str = row_str[col_end_idx + len("</td>") : ]
        print("col:" + col_str)
        extract_data(col_str)
        col_end_idx = row_str.find("</td>")
        
    row_end_idx = response_str.find("</tr>")  
"""
data_list = extract_rows_from_table(response_str)
largest_x = find_largest_x(data_list)
largest_y = find_largest_y(data_list)
#print(str(largest_x))   
#print(str(largest_y)) 
output = build_string_from_list(data_list, largest_x, largest_y)
print(output)

    
    
    
    