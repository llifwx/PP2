import re

def match_string(text):
    pattern = r'\ba+[a-z]+[b]+\b'
    if re.fullmatch(pattern, text):
        return text
    else:
        return "No match found."

text = input("Enter a string: ")
print(match_string(text))