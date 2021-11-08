from os import access
from jsonDbHandler import readContent,db
from random import randint, randrange,choice
import hashlib
import time
from flask import abort,g,request
from functools import wraps
from datetime import date
words : dict = readContent()

allWords = []
for w in words.values():
    allWords.extend(w)
def selectRandomWords(n):
    resultWords = set()
    if n > len(allWords):
        n = len(allWords)
    while len(resultWords) != n:
        selectedWord = choice( allWords )
        if len(selectedWord) != 1:
            resultWords.add(selectedWord)
    return list(resultWords)
    pass
def selectRandomWordsStartWith(n,sw):
    resultWords = set()
    correctStartWithWords = list(filter(lambda e: e.startswith(sw), allWords))
    if len(correctStartWithWords ) < n:
        n = len(correctStartWithWords)
    while len(resultWords) != n:
        selectedWord = choice(correctStartWithWords)
        if len(selectedWord) != 1:
            resultWords.add(selectedWord)
    return list(resultWords)


    pass
def selecRandomWordsWithLenght(n,k):
    resultWords = set()
    correctLengthWords = list(filter(lambda x : len(x) == k, allWords))
    if n > len(correctLengthWords):
        n = len(correctLengthWords)
        
    while len(resultWords) != n:
        selectedWord = choice(correctLengthWords)
        if len(selectedWord) != 1:
            resultWords.add(selectedWord)
    return list(resultWords)
def selectRandomWordsWithLengthAndStartWith(n,k,sw):
    resultWords = set()
    correctWords = list(filter(lambda e: e.startswith(sw) and len(e) == k, allWords))
    if n > len(correctWords):
        n = len(correctWords)
    while len(resultWords) != n:
        selectedWord = choice(correctWords)
        if len(selectedWord) > 1:
            resultWords.add(selectedWord)
    return list(resultWords)
def addTokenToDb(ip):
    token,creation_date,experation_date = checkIPHasToken(ip)
    if token:
        print("[*] Ip address has a valid token")
        return token,creation_date,experation_date
    token = generateAccessToken()
    creation_date = date.today()
    nextMonth = creation_date.month + 1 if creation_date.month != 12 else 1
    experation_date = date(creation_date.year, nextMonth,creation_date.day)
    print(creation_date,experation_date)
    sql = "INSERT INTO access_tokens(ip_address, token, creation_date, experiation_date) VALUES(%s, %s, %s, %s)"
    cur = db.cursor()
    cur.execute(sql,(ip,token,creation_date,experation_date))
    db.commit()
    return token,creation_date,experation_date

    pass
def generateAccessToken():
    hash = hashlib.sha256()
    hash.update(str(time.time()+randint(0,1000000)).encode("utf-8"))
    
    return hash.hexdigest()
def checkIPHasToken(ip):

    cursor = db.cursor()
    sql = "SELECT token,creation_date,experiation_date FROM access_tokens WHERE ip_address = %s"
    cursor.execute(sql,(ip,))
    data = cursor.fetchall()
    if len(data) > 0:
        return data[0]
    return [None]*3
def validToken(token):
    sql = "SELECT token from access_tokens WHERE token = %s"
    cursor = db.cursor()
    cursor.execute(sql,(token,))
    data = cursor.fetchall()
    return True if data else False
def access_required(f):
    def handler(*args, **kw):
        request_data = request.get_json()
        sender_ip = request.remote_addr
        print(sender_ip)
        if "access_token" in request_data:
            if validToken(request_data["access_token"]):
                return f(*args,**kw)
            else:
                abort(401)
            pass
        else:
            abort(401)
    handler.__name__ = f.__name__
    return handler
















