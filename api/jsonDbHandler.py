import json
import psycopg2
from datetime import date
class Database:
    @property
    def service():
        return "PostgreSQL on Heroku"
    def __init__(self):
        self.host : str= "ec2-34-249-247-7.eu-west-1.compute.amazonaws.com"
        self.username : str= "pflfupbtvoglzd"
        self.password : str= "b7dc3d326b0dff07c31c6c7d8859fc056abe8f3dafeffc026402e7ad2a87392f"
        self.database : str= "d4949bhi982mne"
        self.port : int = 5432
        self.db = psycopg2.connect(dbname=self.database,user=self.username,password=self.password,host=self.host,port=self.port)
        if self.db:
            print("[+] Successfully connected!")
    def get_db(self):
        if self.db:
            return self.db
        return None
db = Database().get_db()

REL_PATH = "meta/words.json"
def readContent():
    return json.load(open(REL_PATH))
def writeContent(content):
    json.dump(content,open(REL_PATH,"w"),indent = 6,ensure_ascii=False)
