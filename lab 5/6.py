import re

def replace_characters(text):
    pattern = r'[ ,.]'  
    replaced_text = re.sub(pattern, ":", text)
    return replaced_text

text = input("Enter a string: ")
print(replace_characters(text))