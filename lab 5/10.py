import re

def camel_to_snake(text):
    pattern = r'([a-z])([A-Z])'  
    snake_case = re.sub(pattern, r'\1_\2', text).lower()  

text = input("Enter a camelCase or PascalCase string: ")
print(camel_to_snake(text))
