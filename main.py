import string
from cs50 import get_string, get_int

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

def ceasar_cipher(word, key):
    encrypted = ""
    for char in word:
        if char.islower():
            encrypted = encrypted + lowercase[lowercase.find(char) + key % len(lowercase)]
        elif char.isupper():
            encrypted = encrypted + uppercase[uppercase.find(char) + key % len(uppercase)]
        else:
            encrypted = encrypted + char
    return encrypted

def reverse(word):
    word = list(word)
    reversedword = ""
    word.reverse()
    for char in word:
        reversedword = reversedword + char
    return reversedword

wordI = get_string("String: ")
keyI = get_int("Key: ")
print(reverse(ceasar_cipher(wordI, keyI)))
print(ceasar_cipher(wordI, keyI))