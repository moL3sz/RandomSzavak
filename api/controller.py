from jsonDbHandler import readContent
from random import randrange,choice






def selectRandomWords(n):
    words: dict = readContent()
    resultWords = set()
    while len(resultWords) != n:
        letterIndex = randrange(0,len(words.keys()))
        letter = list(words.keys())[letterIndex]
        selectedWord = choice( words[letter] )
        if len(selectedWord) != 1:
            resultWords.add(selectedWord)
    return list(resultWords)
    pass
def selectRandomWordsStartWith(n,k):
    pass

def selecRandomWordsWithLenght(n,k):
    words: dict = readContent()
    resultWords = set()
    while len(resultWords) != n:
        letterIndex = randrange(0,len(words.keys()))
        letter = list(words.keys())[letterIndex]
        ww = words[letter]

        correctLengthWords = list(filter(lambda x : len(x) == k, ww))
        selectedWord = choice(correctLengthWords)
        if len(selectedWord) != 1:
            resultWords.add(selectedWord)
    return list(resultWords)