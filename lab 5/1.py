import re

def match_string(text):
    pattern = r'^ab*$'
    if re.fullmatch(pattern, text):
        return "Match found!"
    else:
        return "No match found."

text = input("Enter a string: ")
print(match_string(text))