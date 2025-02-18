import re

def uppercase(text):
    pattern = r'\b[A-Z][a-z]+\b'  
    matches = re.findall(pattern, text)
    return matches if matches else ["No match found."]

text = input("Enter a string: ")
print(uppercase(text))
