import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return set(sentence.lower()) 

user_input = input("Enter a sentence: ")

if is_pangram(user_input):
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")