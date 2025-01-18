#example1
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#example2
a = "Hello"
print(a)

#example3
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#example4
a = "Hello, World!"
print(a[1])

#example5
for x in "banana":
  print(x)

#example6
a = "Hello, World!"
print(len(a))

#example7
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#example8
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")