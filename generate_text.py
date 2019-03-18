import random
import time

# import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('-p', '--path',
#         help='Path to the text file/database')
# args = vars(parser.parse_args())
# 
# path = args['path']


def addToDict(chain, wordList):
    for i in range(len(wordList)):
        if i + 3 > len(wordList):
            break
        try:
            chain[wordList[i] + ' ' + wordList[i + 1]].append(wordList[i + 2])
        except KeyError:
            chain[wordList[i] + ' ' + wordList[i + 1]] = [wordList[i + 2]]

def generateNextWord(wordList, chain):
    i = (len(wordList))
    if i >= 2:
        i -= 1
        if wordList[i - 1] + ' ' + wordList[i] in chain:
            newWord = (random.choice(chain[wordList[i - 1] + ' ' + wordList[i]]))
            return newWord
    return None
	
def generateIndexText(chain, index):
    line = ""
    line = index
    wordList = line.split()
    counter = 0
    while(True):
        counter += 1
        newWord = generateNextWord(wordList, chain)
        if newWord is None:
            break
        wordList.append(newWord)
        if counter > 500:
            #print()
            #print("Too Long")
            #print()
            break
    return ' '.join(wordList)

def make_phrase(path):
    chain = {}

    with open(path) as line:
        lines = line.readlines()

    for line in lines:
        wordList = line.split()
        addToDict(chain, wordList)
    
    quote_start = [word for word in list(chain.keys()) if word[0].isupper()]

    index = random.choice(quote_start)
    phrase = generateIndexText(chain, index)
    return phrase

# phrase = make_phrase(path)
# print(phrase)
