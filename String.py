
#can use double or single quotes:

print("Hello")
print('Hello')

#multiline string with three double quote
a = """
   sakib
   tamim
   ridhoy
   """
print(a)


#multiline string with three single quote
a = '''
 sakib
 tamim
 Ridhoy
 '''
print(a)


a = "Hello"
print(a)

#strings are array
"""
Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.
"""


a = "Hello, World!"
print(a[1])


#Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x) 

#string_length: len()
a = "Hello, World!"
print(len(a))


#check string:
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("free" in txt)


#check if not
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")


txt = "The best things in life are free!"
print("expensive" not in txt)












