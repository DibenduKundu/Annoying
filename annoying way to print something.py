from random import randrange as rand
from time import sleep

def print_string(current_string, expected_character):
    some_random_character=rand(65,122)
    while True:
        print("\n"+current_string+chr(some_random_character),end="")
        sleep(0.5)  #delete this line to get result instantly
        if chr(some_random_character)==expected_character:
            break
        some_random_character=rand(65,122)

my_string =input("Enter the String: ")
current_str=""

for letter in my_string:
    print_string(current_str, letter)
    current_str+=letter #test
