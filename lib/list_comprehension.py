#!/usr/bin/env python3

def return_evens(num_list):
    evens = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
    
    return evens

def make_exclamation(sentence_list):
    new_list = []
    for sentence in sentence_list:
        new_list.append(f'{sentence}!')
    
    return new_list
    
print(make_exclamation(["Hello", "I'm doing great", "Python is fun"]))