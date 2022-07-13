# whiteboard of the day
#` Remove vowels
# Write a function that will remove all vowels from a given string. The function should return a string.
# Example:
# Input: ‘Joel’
# Output: ‘Jl’


# def removeVowels(words):
#     newValue = list(words)
#     vowels = ['a', 'e', 'i', 'o', 'u']
#     for letter in newValue:
#         if letter in vowels:
#             del(letter)
#     return newValue

# print(removeVowels("ice cream"))

# answer to whiteboard - Brandt
def rem_vowel(str):
   vowels = ('a', 'e', 'i', 'o', 'u') 
   for x in str.lower():
       if x in vowels:
           str = str.replace(x, "")
   return str

print(rem_vowel('Joel'))

# answer to whiteboard - Shoha
def rV(string):
    output = ''
    for letter in string:
        if letter in {'a', 'e', 'i', 'o', 'u'}:
            continue
        else:
            output += letter
    return output

print(rV('Joel'))

# regex answer to whiteboard
import re
def removeVowel(string):
    pattern = re.compile('[^aeiou]')
    found = pattern.findall(string)
    print(found)
    return ''.join(found)

removeVowel("hellotheremynameisandrew")

# whiteboard answer # 4
def rem_vow(st):
    vowels = ('a', 'e', 'i', 'o', 'u')
    return str([x for x in st if x not in vowels])
print(rem_vow('Joel'))