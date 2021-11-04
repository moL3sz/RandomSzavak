"""
    - Author: Molesz
"""




from typing import List
from bs4 import BeautifulSoup
import requests
from jsonDbHandler import readContent,writeContent




BASE_URL = "https://www.arcanum.com"
MAIN_URL ="https://www.arcanum.com/hu/online-kiadvanyok/Lexikonok-a-magyar-nyelv-ertelmezo-szotara-1BE8B/"
def scrapeLetters() -> List[str]:

    hrefToWordsByLetters = []
    mainPage = requests.get(MAIN_URL)
    parser = BeautifulSoup(mainPage.text,"html.parser")


    letterContainer = parser.find("div",{"class":"list-group mb-3"})
    lettersWithHref = letterContainer.find_all("a")[1:-2]
    for letter in lettersWithHref:
        yield (letter["href"],letter.text.strip())
def scrapeWordsPage(wordsURL):
    currentPage = requests.get(wordsURL)
    parser = BeautifulSoup(currentPage.text, "html.parser")
    wordsList = set()
    wordsContainer = parser.find("div",{"class":"list-group mb-3"})
    words = wordsContainer.find_all("a")
    for word in words:
        parsedWord = word.text.strip().split(" ")[0]
        wordsList.add(parsedWord)
    return list(wordsList)
    pass

def scrapeWords(letterURL):
    

    #get max page
    currentPage = requests.get(BASE_URL+letterURL)
    parser = BeautifulSoup(currentPage.text, "html.parser")
    pagination = parser.find("ul",{"class":"pagination pagination-sm"})
    allWords = []
    if pagination:
        MAX_PAGE = int(pagination.find_all("li")[-1].text.strip())
    else:
        MAX_PAGE = 1
    WORDS_URL_PAGE = BASE_URL + letterURL +"/?page={}"
    for pageNumber in range(1,MAX_PAGE+1):
        print(f"[*] On page: {pageNumber}")
        pageWords = scrapeWordsPage(WORDS_URL_PAGE.format(pageNumber))
        allWords.extend(pageWords)
    return allWords
    
def main():
    wordsByLetters = {}
    for letterHref,letter in scrapeLetters():
        print(f"[*] On letter: {letter}")
        allWords = scrapeWords(letterHref)
        wordsByLetters[letter] = allWords
    writeContent(wordsByLetters)
    

if __name__ == "__main__":
    main()




