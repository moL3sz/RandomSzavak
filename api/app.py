#!/usr/bin/env python3
import json
from flask import Flask,request,jsonify,abort
from flask_cors import cross_origin,CORS
from controller import *

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"/*": {"origins": "*"}})
@app.route("/generate_token")
@cross_origin()
def generateToken():
    try:
        ip_address = request.remote_addr
        token,creation_date,experation_date = addTokenToDb(ip_address)
        return {"access_token":token,"creation_date":str(creation_date),"experation_date":str(experation_date)}
    except Exception as e:
        abort(500)



@app.route("/getwords", methods=["GET","POST"])
@cross_origin()
@access_required
def getWords():
    try:
        params = request.get_json()
        size = int(params["size"])
        sw = params["sw"]
        l = params["l"]
        if sw != "" and l == "":
            selectedWords = selectRandomWordsStartWith(size,sw)
            pass
        elif sw == "" and l != "":
            l = int(l)
            selectedWords = selecRandomWordsWithLenght(size,l)
            pass 
        elif sw != "" and l != "":
            l = int(l)
            selectedWords = selectRandomWordsWithLengthAndStartWith(size,l,sw)
        else:
            selectedWords = selectRandomWords(size)         
        returnData = {"words":list(selectedWords)}
        return jsonify(returnData)
    except Exception as e:
        raise e
    return "300"
