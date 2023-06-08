#
#Upper case the first letter of sentence.
#capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)


# if first letter number 
txt = "36 is my age."
x = txt.capitalize()
print (x)

#casefold():all characters convert to lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#count from position 10 to 24:
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple", 10, 24)
print(x)

#encode()
#UTF-8 encode the string:
txt = "My name is St�le"
x = txt.encode()
print(x)

"""

The encode():{} encodes the string,
using the specified encoding.
If no encoding is specified,UTF-8 will be used.

"""

#endwith(): True/False
#The endswith() method returns True if the string ends with the specified value, otherwise False.

txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) #True

txt = "Hello, welcome to my world"
x = txt.endswith("d")
print(x) #True


#find():return index
#Where in the text is the word "welcome"?:
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) # 7

#index()
txt = "Hello,  welcome to my world."
x = txt.index("welcome")
print(x) # 8

#find in a range 
txt = "hellow,welcome to my world."
x = txt.find("e", 5, 10) #search 'e'
print(x)


"""

The find(),finds the first occurrence of the specified value.

- returns -1 if the value is not found.

- is almost the same as the index() method, 
the only difference is that the index() method raises an error if the value is not found. 
"""




# difference find() and index(),if not found anything.
txt = "Hello, welcome to my world."
print(txt.find("q")) # return -1
#(txt.index("q")) # error দিবে।


"""
The format() method formats the specified value(s) and insert them inside the string's placeholder.

The placeholder is defined using curly brackets: {}. Read more about the placeholders in the Placeholder section below.

The format() method returns the formatted string.

format নিয়ে আলাদা একটা সেকশন হবে,অনেককিছু আছে।
"""

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


"""
isalnum():
Returns True if all characters in the string are alphanumeric

isalpha():
Returns True if all characters in the string are in the alphabet

isdecimal():
Returns True if all characters in the string are decimals

isdigit():
Returns True if all characters in the string are digits

isidentifier():
Returns True if the string is an identifier

islower():
Returns True if all characters in the string are lower case

isnumeric():
Returns True if all characters in the string are numeric

isprintable():
Returns True if all characters in the string are printable

isspace():
Returns True if all characters in the string are whitespaces

istitle():
Returns True if the string follows the rules of a title

isupper():
Returns True if all characters in the string are upper case

"""

"""
The join(), takes all items in an iterable 
  and joins them into one string.
-A string must be specified as the separator.
-Join all items in a tuple into a string, using a hash character as separator:

"""

myTuple = ("John", "Peter", "Vicky")
separator="!"
x = separator.join(myTuple)

print(x)


#Returns a left justified version of the string

txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")
#In the result, there are actually 14 whitespaces to the right of the word banana.


#Using the letter "k" as the padding character:
txt = "banana"
x = txt.ljust(15, "k")
print(x)


#upper()
#Symbols and Numbers are ignored.
txt = "Hello my friends"
x = txt.upper()
print(x)

#lower()
txt = "Hello my FRIENDS"
x = txt.lower()
print(x)


#title()
#Converts the first character of each word to upper case
txt = "Welcome to my world"
x = txt.title()
print(x)

#Note that the first letter after a non-alphabet letter is converted into a upper case letter:
txt = "hello b2bb2 and 33gggg"
x = txt.title()
print(x)


#The partition() searches for a specified string,
#and splits the string into a tuple containing three elements.

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)

# it not found
txt = "I could eat bananas all day"
x = txt.partition("apples")
print(x)

#Splits the string at the specified separator, and returns a list
#The split() method splits a string into a list.
#Split a string into a list where each word is a list item
txt = "welcome to the jungle"
x = txt.split()
print(x) #string into list

# split by comma(,)
txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

# split by #
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)



#replace():
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#Replace all occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "babababa")
print(x)


#Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "Hahaha", 2)
print(x)








    