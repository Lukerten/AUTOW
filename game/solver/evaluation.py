from game.solver.solver import filterlist
from math import log2, ceil

def evaluateGuess (word_list, guesses):
    previousGuesses = guesses[:-1]

    old_set = len(filterlist(word_list,previousGuesses))
    new_set = len(filterlist(word_list,guesses))

    # score the actual information gathered 
    info = bits (old_set, new_set)

    return info, new_set

def bits (num1, num2):
    larger_num = max(num1, num2)
    smaller_num = min(num1, num2)
    count = log2(larger_num / smaller_num)

    return round(count,3)