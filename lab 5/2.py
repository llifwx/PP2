import re

def match_string(text):
    pattern = r'^ab{2,3}$'
    if re.fullmatch (pattern, text):
        return "Match found!"
    else:
        return "No match found."
    
text = input("Enter a string: ")
print(match_string(text))