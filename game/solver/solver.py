from random import choice

def solver (previous_guesses, word_list):    
    words = filterlist(word_list,previous_guesses)
    selection = choice (words)
    return selection

def filterlist(word_list, guesses):
    words = word_list
    for guess in guesses:
        for data in guess:
            index = data["index"]
            letter = data["letter"]
            if index in range (0,5): 
                words = foundWithIndex(letter,index,words)
            elif index in range (16,21): 
                words = foundWithoutIndex(letter, index-16, words)
            if index == -1:
                words = foundNotInWord (letter,words)
    return words

def foundWithIndex (letter,index, word_list):
    new_word_list = []
    for word in word_list:
        if word[index] == letter:
            new_word_list.append(word)
    return new_word_list

def foundWithoutIndex (letter, index ,word_list):
    new_word_list = []
    for word in word_list:
        if (letter in word and word[index] != letter) :
            new_word_list.append(word)
    return new_word_list

def foundNotInWord (letter, word_list):
    new_word_list = []
    for word in word_list:
        if letter not in word:
            new_word_list.append(word)
    return new_word_list

