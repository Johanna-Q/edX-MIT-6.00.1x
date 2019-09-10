# Problem 3 description: 
# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print:
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

# Solution: 
longest = ''
temp = ''
for char in s:
    if temp == '':
        temp = char
    elif temp[-1] <= char:
        temp = temp + char
    elif temp[-1] > char:
        if len(longest) < len(temp):
            longest = temp
            temp = char
        else:
            temp = char
if len(temp) > len(longest):
    longest = temp
print ('Longest substring in alphabetical order is: ' + longest)
