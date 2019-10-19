# Problem 42

import string

def word_value(word):
    """
    Returns the sum of each letter in a word based on its place in the alphabet
    """
    scores = {string.ascii_uppercase[char] : char+1
        for char in range(len(string.ascii_uppercase))}
    scr = 0
    for letter in word:
        scr += scores[letter]
    return scr

stop = 28   # Longest word in list is 14char.  Max triangle number would be 
            # 14*26 = 364. 27th term is the first greater than 364.
my_tri_num = [(n**2 + n)//2 for n in range(1,stop)]
tri_words = 0
filename = 'text files/p042_words.txt'
with open(filename) as file_object:
    contents = file_object.read()
words = contents.split(',')
for word in words:
    wv = word_value(word.replace('"','')) # strips double quotes
    if wv in my_tri_num:
        tri_words += 1
print(tri_words)