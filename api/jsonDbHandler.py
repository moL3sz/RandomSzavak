import json

REL_PATH = "meta/words.json"
def readContent():
    return json.load(open(REL_PATH))
def writeContent(content):
    json.dump(content,open(REL_PATH,"w"),indent = 6,ensure_ascii=False)