
print("")
print("==============Exams===================================")

def demystify(l1_string):
    return l1_string.replace('l', 'a').replace('1', 'b')
print(demystify("lll111l1l1l1111lll"))
print(demystify("111l1l11l11lll1lll1lll11111ll11l1ll1l111"))


    
print("")
print("==============Exams===================================")

def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    return count

result = count_vowels("aaassseefffgggiiijjjoOOkkkuuuu")
print(result)
result1 = count_vowels("aovvouOucvicIIOveeOIclOeuvvauouuvciOIsle")
print(result1)

print("")
print("===============Exams==================================")


print("")
print("=================================================")
"""
Template - Function that swaps and capitalizes first and last names
"""


def name_swap(name_string):
    """
    Given the string name string of the form "first last", return 
    the string "Last First" where both names are now capitalized
    """
    
    # Enter code here
    (first, last) = name_string.split(" ")
    return last.capitalize() + " " + first.capitalize()

    
# Tests

print(name_swap("joe warren"))
print(name_swap("scott rixner"))
print(name_swap("john greiner"))


# Output

#Warren Joe
#Rixner Scott
#Greiner John
print("")
print("=================================================")

print("")
print("=================================================")
"""
Template - Function that checks whether a string can be converted to an integer
"""


def make_int(int_string):
    """
    Given the string int_string, return the associated integer if all 
    digits are decimal digits.  Other return -1.
    """
    
    # enter code here
    if int_string.isdigit():
        return int(int_string)
    else:
        return -1
        
    
# Tests

print(make_int("123"))
print(make_int("00123"))
print(make_int("1.23"))
print(make_int("-123"))


# Output

#123
#123
#-1
#-1
print("")
print("=================================================")



print("")
print("=================================================")
"""
Template - Function that uses format to create a nametag
"""


def make_nametag(first_name, topic):
    """
    Given two strings first_name and topic,
    return a string of the form ""Hi! My name 
    is XXX. This lecture covers YYY." where
    XXX and YYY are first_name and topic.
    """
    
    # enter code here
    template = "Hi! My name is {0}. This lecture covers {1}."
    return template.format(first_name, topic)

    
# Tests

print(make_nametag("Scott", "Python"))
print(make_nametag("Joe", "games"))
print(make_nametag("John", "programming tips"))


# Output

#Hi! My name is Scott. This lecture covers Python.
#Hi! My name is Joe. This lecture covers games.
#Hi! My name is John. This lecture covers programming tips.
print("")
print("=================================================")

print("")
print("=================================================")
"""
Template - Function that tests for substring
"""


def is_substring(example_string, test_string):
    """
    Function that returns True if test_string
    is a substring of example_string and False otherwise
    """

    # enter one line of code for substring test here
    return test_string in example_string
    

# Tests

example_string = "It's just a flesh wound."

print(is_substring(example_string, "just"))
print(is_substring(example_string, "flesh wound"))
print(is_substring(example_string, "piddog"))
print(is_substring(example_string, "it's"))
print(is_substring(example_string, "It's"))

# Output

#True
#True
#False
#False
#True
print("")
print("=================================================")

print("")
print("=================================================")
"""
Template - Echo a string multiple times to the console
"""

def echo(call, repeats):
    """
    Echo the string call to the console repeats number of time
    Each echo should be on a separate line
    """
    # pass
    answer = call + ('\n' + call) * (repeats - 1)
    print(answer)


# Tests
echo("Hello", 5)
echo("Goodbye", 3)

# Output
#Hello
#Hello
#Hello
#Hello
#Hello
#Goodbye
#Goodbye
#Goodbye

print("")
print("=================================================")

print("")
print("=================================================")
"""
Template - Another example of slice selection for lists
"""

# Create a string formed by selecting the first three characters of example_string
# plus the last three characters of example_string
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[: 3] + example_string [-3 : ]
print(solution_string)

# Output should be 
#It's just a flesh wound
#It'und
print("")
print("=================================================")

print("")
print("=================================================")
"""
Solution - Slice selection for lists
"""

# Create a string formed by selecting all but the first and last letters of example_string
example_string = "It's just a flesh wound"
print(example_string)

# Note that negative indices select characters from the end of the string
solution_string = example_string[1 : -1]
print(solution_string)

# Output should be 
#It's just a flesh wound
#t's just a flesh woun
print("")
print("=================================================")


print("")
print("=================================================")
"""
Template - Item selection for lists
"""

# Create a string formed by selecting the first and last letters of example_string
example_string = "It's just a flesh wound"
print(example_string)

solution_string = example_string[0] + example_string[-1]
print(solution_string)

# Output should be 
#It's just a flesh wound
#Id

print("")
print("=================================================")


print("")
print("=================================================")
"""
Template - String examples
"""

# Fix the four string definitions below.

string1 = "It's just a flesh wound"
string2 = "It's just a flesh wound"
string3 = "It's just a flesh wound"
string4 = """It's just a flesh wound"""

print(string1)
print(string2)
print(string3)
print(string4)
print("")
print("=================================================")


print("")
print("=================================================")
num = 3.283663293
output = "{0:>10.3f} {0:.2f}".format(num)
print(output)
print("=================================================")
print("")

print("")
print("=================================================")
name1 = "Pierre"
age1 = 7
name2 = "May"
age2 = 13

line1 = "{0:^7} {1:>3}".format(name1, age1)
line2 = "{0:^7} {1:>3}".format(name2, age2)
print(line1)
print(line2)
print("=================================================")

print("")



print("=================================================")

mood1 = "happy"
mood2 = "sad"
sentence1 = "I feel {0}, do you feel {0}?  Or are you {1}? I'm not sure if we should be {0}.".format(mood1, mood2)
print(sentence1)

print("=================================================")




print("=================================================")

country = "France"
capital = "Paris"
sentence = "The capital of {} is {}.".format(country, capital)
print(sentence)
print("=================================================")



"""
Slicing strings.
"""

word = "everything"

# Selecting substrings
print(word[1:5])
print(word[5:9])

# Open ended slices
print(word[5:])
print(word[:4])

# Using negative indices
print(word[-3:])
print(word[2:-3])

# Indexing past the end
print(word[8:20])
print("$" + word[22:29] + "^ Is it out of range?")

# Empty slicesm, both are not make-sense to python. 
print(word[6:6])
print(word[4:2])







print("=================================================")
print("======Third program===")
print("=================================================")





"""
String searching examples.
"""

sentence = "When I tell you pick up the " + \
           "left rock, it will be the " + \
           "right one, and then only " + \
           "the right rock will be left."

print(sentence)

# Finding strings within strings
print("Finding lefts")
firstleft = sentence.find("left")
print(firstleft, sentence[firstleft])
lastleft = sentence.rfind("left")
print(lastleft, sentence[lastleft])


print("")
print("Finding rights")
firstright = sentence.index("right")
print(firstright, sentence[firstright])
lastright = sentence.rindex("right")
print(lastright, sentence[lastright])

print("")
print("Finding Rixner")
firstrixner1 = sentence.find("Rixner")
print(firstrixner1)
firstrixner2 = sentence.find("Rao")
print(firstrixner2)

# Counting strings within strings
print("")
print("Counting substrings")
print("Number of lefts:", sentence.count("left"))
print("Number of apples:", sentence.count("balu"))

# Checking start/ends
print("")
print(sentence.startswith("When"))
print(sentence.endswith("The end."))

print("=================================================")
print("======Third program===")
print("=================================================")













print("=================================================")
print("======Second program===")
print("=================================================")





"""
String indexing examples.
"""

phrase = "Python is great!"

# first character
print(phrase[0])

# fourth character
fourth = phrase[3]
print(fourth)
print(type(phrase))
print(type(fourth))

# length of string
phraselen = len(phrase)
print(phraselen)

# last character
print(phrase[phraselen - 1])
print(phrase[-1])

# thirteenth from last (fourth) character
print(phrase[-13])

# Out of bounds
#print(phrase[phraselen])
print(phrase[-16])

# Indices
string = "abcde"
#character   a  b  c  d  e
#pos index   0  1  2  3  4
#neg index  -5 -4 -3 -2 -1
print(string[-1])
print(string[4])


print("======Third program===")




print("===================First==============================")


"""
Simple string literal examples.
"""

# Strings are enclosed in quotes
name = 'Scott Rixner'
university = "Rice"

print(name)
print(university)

# Multiline strings use triple quotes
address = '''Rice University
Houston, TX
'''

# First Fig by Edna St. Vincent Millay
poem = """My candle burns at both ends;
  It will not last the night;
But ah, my foes, and oh, my friends---
  It gives a lovely light!
"""

print("")

print("Address")
print("=======")
print(address)

print("First Fig")
print("=========")
print(poem)


# Characters
chars = "abc'DEF*&$"
print(chars)
chars2 = '\t"abc"\ndef\''
print(chars2)

# String "arithmetic"
print("Concatenating strings")
name_and_uni = name + " " + university
print(name_and_uni)

print("")
print("")
print("Repeating strings")
lots_o_rice = university * 4
print(lots_o_rice)

# Using str
num = 3.87
strnum = str(num)
print("number: " + strnum)
#print("number: " + num)
