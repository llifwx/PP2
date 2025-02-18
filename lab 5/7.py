import re

def snake_to_camel(snake_str):
    words = snake_str.split('_')  
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:]) 
    return camel_case

text = input("Enter a snake_case string: ")
print(snake_to_camel(text))