#example1
txt = "We are the so-called \"Vikings\" from the north."

#example2
txt = 'It\'s alright.'
print(txt) 

#example3
txt = "This will insert one \\ (backslash)."
print(txt) 

#example4
txt = "Hello\nWorld!"
print(txt) 

#example5
txt = "Hello\rWorld!"
print(txt) 

#example6
txt = "Hello\tWorld!"
print(txt) 

#example7
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) 

#example8
#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 

#example9
#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 