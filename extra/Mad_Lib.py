#!/usr/bin/python3

def verify_word(word):
    if word.isalpha() and len(word.split()) == 1:
        return True
    else:
        print("You made a mistake")
        return False

print("Welcome to Mad Libs!")

adjective = input("Please, write an adjective: ")
while not verify_word(adjective):
    adjective = input("Please, write just one word that is an adjective: ")

substantive = input("Now, write a substantive: ")
while not verify_word(substantive):
    substantive = input("Please, write just one word that is a substantive: ")

verb = input("At last, write a verb: ")
while not verify_word(verb):
    verb = input("Please, write just one word that is a verb: ")

print("This is your mad libs:")
print(f"The {adjective} {substantive} loves {verb} in the park!")
