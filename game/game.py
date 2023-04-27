from rich.prompt import Prompt
from rich.console import Console
from random import choice
from game.words import word_list
from game.solver.solver import solver

# Text Highlighting on Command-Line
def correct_place(letter):
    return f'[black on green]{letter}[/]'
def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'
def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'
def delete_last_line():
    print("\033[2A\033[J", end="")

# Pattern 
squares = {
    'correct_place': '🟩',
    'correct_letter': '🟨',
    'incorrect_letter': '⬛'
}

# Guess Evaluation 
def check_answer (guess, answer):
    result = []
    pattern = []
    letters = []
    for i, letter in enumerate(guess):
        if guess[i] == answer[i]:
            letters.append({"letter": letter, "index" : i})
            pattern.append( squares["correct_place"])
            result += correct_place(letter)
        elif (letter in answer):
            letters.append({"letter": letter, "index" : i+ 16})
            pattern.append( squares["correct_letter"])
            result += correct_letter(letter)
        else:
            letters.append({"letter": letter, "index" : -1})
            pattern.append( squares["incorrect_letter"])
            result += incorrect_letter(letter)
    return ''.join(pattern+[" "]+result), letters

# Game Loop
def game (console, answer):
    iteration = 0
    solved = False
    guessed_words = []
    guessed_letters = []
    full_pattern = []

    #* Game loop:
    while not solved:
        iteration += 1
        guess = solver(guessed_letters,word_list)

        #* check if guess is a valid input
        while guess not in word_list or guess in guessed_words:
            guess = solver(guessed_letters,word_list)
        pattern, letters = check_answer(guess, answer) 

        #* Round Evaluation
        full_pattern.append(pattern)
        guessed_letters.append(letters)
        guessed_words.append(guess)
        if guess == answer:
            solved = True

        #* print results
        # console.print(result)

    console.print(*full_pattern, sep="\n")
    console.print(iteration)
    return iteration
