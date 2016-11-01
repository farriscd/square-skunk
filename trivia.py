#!/usr/bin/python3

import json
import random
import sys
from trivia_parse import *

trivia = {}
with open('trivia.txt') as json_data:
    trivia = json.load(json_data)

def next_question(trivia_list):
    return random.choice(list(trivia_list.keys()))

def check_answer(question, guess, trivia_list):
    parsed_guess = parse(guess)
    parsed_answer = parse(trivia_list[question])
    if sys.argv[1] == '-d':
        print(parsed_guess)
        print(parsed_answer)
    if weighted_score(parsed_guess, parsed_answer) >= score_threshold:
        return True
    else:
        return False
    #return parsed_guess == parsed_answer

score_threshold = 0.80

score = 0
while True:
    question = next_question(trivia)
    print(question)
    guess = input()
    if check_answer(question, guess, trivia) != True:
        print("Wrong!", (trivia[question]))
        print("Your score:", (score))
        break
    del trivia[question]
    score += 1
