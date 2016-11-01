from lxml import html
from time import sleep
import requests
import json

questions = []
answers = []
trivia = {}

for i in range(0, 28):
    sleep(1)
    page = requests.get('' + str(i))
    tree = html.fromstring(page.content)

    questions.extend(tree.xpath('//*[starts-with(@href, "/content/")]/text()'))
    answers.extend(tree.xpath('//div[@class= "spoiler-content"]/text()'))

    for j in range(0, len(questions)):
        trivia[questions[j]] = answers[j]

print("{0} ?= {1}".format(len(questions), len(answers)))

with open('trivia.txt', 'w') as outfile:
    json.dump(trivia, outfile)
