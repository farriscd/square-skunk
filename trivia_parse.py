# todo: switch between words and numbers i.e 'zero' -> '0'
#       recognize between word orders i.e 'john and paul' vs 'paul and john'
#       fix parse_parens
#       adjust scoring system i.e. ('carbon dioxide' passes as 'argon', 'morphine' as 'heroin')

parsed = [
    '/',
    ' !',
    ' ?',
    ' .',
    ' & ',
    ', ',
    '.',
    "'",

    ' and ',
    ' the ',
    ' a ',

    ' of ',
    ' in ',
    ' to ',
    ' for ',
    ' with ',
    ' on ',
    ' at ',
    ' from ',
    ' by ',
    ' about ',
    ' as ',
    ' into ',
    ' like ',
    ' through ',
    ' after ',
    ' over ',
    ' between ',
    ' out ',
    ' against ',
    ' during ',
    ' without ',
    ' before ',
    ' under ',
    ' around ',
    ' among ']

def contains_numbers(string):
    return any(char.isdigit() for char in string)

# process
# check for numeric -> remove commonalities -> remove white space -> count rating
## PARSE WITHOUT SPLIT ##
def parse(string):
    #convert string to lowercase
    string = string.lower()
  
    #remove excess whitespace
    string = string.strip()
    string = " ".join(string.split())    
    
    #check if string is made up entirely of numbers
    if string.isdigit():
        return string

    #checks string for items on parsed list and removes them
    string = remove_parseable(string)
    
    if string.find('(') != -1:
        string = remove_parens(string)
    
    #removes all whitespace
    string = string.replace(" ", "")

    #returns fully parsed string
    return string

def remove_parseable(string):
    for i in parsed:
        if string.startswith(i[1:]):
            string = string[len(i[1:]):]
        if i in string:
            string = string.replace(i, " ")
    return string

#only works for first set of parens, only works with pairs of parens    
def remove_parens(string):
    start = string.find('(')
    end = string.find(')')
    return string[:start]+string[end+1:]

#score method 1
def score_guess1(guess, answer):
    score = 0
    answer_list = list(answer)
    guess_list = list(guess)
    for i in answer_list:
        for j in guess_list:
            if i == j:
                score += 1
                print(i, j, score)
                break
    return score

def score_guess2(guess, answer):
    score = 0
    for i in range(0, len(answer)):
        for j in range(len(guess)):
            if answer[i] == guess[j]:
                score += 1
                print(answer[i], guess[j], score)
                break

def lower_limit(i):
    return min(abs(i-2), abs(i-1), abs(i))

def upper_limit(i, l):
    return max(l-i-2, l-i-1, l-i)+i

def score_guess(guess, answer):
    score = 0
    guess_copy = guess
    for i in range(0, len(answer)):
        guess = guess_copy
        for j in range(lower_limit(i), upper_limit(i, len(guess))):
            if guess[j] == answer[i]:
                score += 1
                break
    return score

def weighted_score(guess, answer):
    return score_guess(guess, answer)/len(answer)
