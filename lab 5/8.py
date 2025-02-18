import re

def split_at_uppercase(text):
    pattern = r'(?=[A-Z])'  
    return re.split(pattern, text)

text = input("Enter a string: ")
print(split_at_uppercase(text))
