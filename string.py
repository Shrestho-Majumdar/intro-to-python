
#ASSIGNMENT FOR STRING:
text = "python programming"
#consider the given string and perform the folloiwng operations on the string:

#1. display python
substring = (text[0:6])
print(substring)

#2. display programming
substring = (text[7:18])
print(substring)

#3. find whether string "java" is in the string or not. if not then include it between python and programming
print("java" in text)
newtext = " python "+"java"+" programming "
print(newtext)

#4. find the length of the new string.
length = len(newtext)
print(length)

#5. count the number of words in the string.
words = newtext.split()
word_count = len(words)
print(f"word count:{word_count}")

#6. cpaitalize each word in the string.
capital = newtext.title()
print(capital)

#7. remove all the spaces in and print the string.
no_space = capital.strip()
print(no_space)

#8. print the frequencies of "A","P","R","M".
ALL_CAPITAL = no_space.upper()
print(ALL_CAPITAL)
frequency = ALL_CAPITAL.count("A")
print("frequency of A:",(frequency))
frequency = ALL_CAPITAL.count("P")
print("frequency of P:",(frequency))
frequency = ALL_CAPITAL.count("R")
print("frequency of R:",(frequency))
frequency = ALL_CAPITAL.count("M")
print("frequency of M:",(frequency))
