from rich.console import Console
import time
from random import choice
from game.words import generate_answer_list
from game.game import game

#! set this to how ever many rounds you want to play 
ITERATIONS = 100;

if __name__ == '__main__':
    console = Console();
    scores = []
    for i in range (ITERATIONS):
        # plays a fresh game of Wordle 
        scores.append (game(console, choice(generate_answer_list())))
        time.sleep(2)
    
    # Score tracking 
    scores.sort();
    average_score = sum(scores)/ITERATIONS
    highest_score = min(scores)
    lowest_score = max(scores)

    console.print ("Rounds Played :" ,ITERATIONS)
    console.print ("Average Score :" ,average_score)
    console.print ("Highest Score :" ,highest_score)
    console.print ("Lowest Score  :" ,lowest_score)



