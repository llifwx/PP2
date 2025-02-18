import re

def lowcase(text):
    pattern = r'\b[a-z]+_[a-z]+\b'
    matches = re.findall(pattern, text)
    return matches if matches else ["No match found."]

text = input("Enter a string: ")
print(lowcase(text)) 