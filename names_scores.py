# Problem 22
#
# Using names.txt, a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order. Then owrking out the
# alphabetical value for each name, multiply this value by its alphabetical
# position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is
# worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So COLIN
# would obtain a score of 938 x 53 - 49714.
#
# What is the total of all the name scores in the file?

import csv
import string
filename = "text files/p022_names.txt"

with open(filename) as file_object:
    reader = csv.reader(file_object)
    names = []
    for row in reader:
        names.append(row)

names = names.pop()

names.sort()

my_abc = { string.ascii_uppercase[char] : char+1
    for char in range(len(string.ascii_uppercase))}

answer = 0

for name in range(len(names)):
    name_sum = 0
    for letter in names[name]:
        name_sum += my_abc[letter]
    answer += name_sum*(name+1)

print(answer)
