name = "John"
greeting = 'Hello!'
multi_line = '''This is a 
multi-line string.'''

# Indexing
word = "Python"
print(word[0])  # Output: 'P'
print(word[2])  # Output: 't'

# Concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Output: 'John Doe'

# Repetition
exclamation = "Wow! " * 3  # Output: 'Wow! Wow! Wow!'

# Length
name = "Python"
print(len(name))  # Output: 6

# Substrings
language = "Python"
print(language[0:3])  # Output: 'Pyt'
print(language[3:])   # Output: 'hon'
print(language[-1])   # Output: 'n' (negative indexing)

# Lower/Upper case
message = "Hello, World!"
print(message.upper())  # Output: 'HELLO, WORLD!'
print(message.lower())  # Output: 'hello, world!'

# Remove Whitespace start & end
text = "  Python  "
print(text.strip())  # Output: 'Python'

# Replace part of string
message = "Hello, World!"
print(message.replace("World", "Python"))  # Output: 'Hello, Python!'

# Split a string into a list.
sentence = "Python is fun"
words = sentence.split()  # Output: ['Python', 'is', 'fun']

# Join elements of a list into a string.
words = ['Python', 'is', 'fun']
sentence = " ".join(words)  # Output: 'Python is fun'

#Check if a string starts or ends with a specific substring.
filename = "report.pdf"
print(filename.endswith(".pdf"))  # Output: True

# string formatting
name = "John"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  # Output: 'My name is John and I am 30 years old.'

name = "John"
age = 30
print(f"My name is {name} and I am {age} years old.")  # Output: 'My name is John and I am 30 years old.'

# Immutable: can't be changed
text = "hello"
# text[0] = "H"  # Error: strings are immutable!
text = "H" + text[1:]  # This works because it creates a new string

# Concatenation in loops
result = ""    
result += "a"

# The same thing would be
result = result + "a"

#Final Challenge: Build a text-based name generator that combines random first and last names using string manipulation.
first_names = ["Christian", "Dylan", "Travis", "Katelyn"]
last_names = ["Sachs", "Katina", "Peck", "Mehner"]
# n = len(first_names)
# full_names  = []
# for i in range(0,n-1):
#     full_names.append(first_names[i] +" " +  last_names[i])
#     i += 1
# print(full_names)
import random
print(random.choice(first_names) + " " + random.choice(last_names))