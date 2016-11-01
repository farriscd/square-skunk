# todo: switch between words and numbers i.e 'zero' -> '0'
#       fix parse_parens
#       adjust scoring system i.e. ('carbon dioxide' passes as 'argon', 'morphine' as 'heroin')
#       figure out how to parse 'or', questions with multiple correct answers

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

    #checks string for parentheses and removes them    
    if string.find('(') != -1:
        string = remove_parens(string)

    #checks string for items on parsed list and removes them
    string = remove_parseable(string)

    #splits string into list, sorts alphabetically, rejoins as string
    lstring = sorted(string.split())
    string = ''.join(lstring)    

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

## Scoring ##
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
