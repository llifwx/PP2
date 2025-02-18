import re

def insert_spaces(text):
    pattern = r'([a-z])([A-Z])'  
    modified_text = re.sub(pattern, r'\1 \2', text)  
    return modified_text

text = input("Enter a string: ")
print(insert_spaces(text))
