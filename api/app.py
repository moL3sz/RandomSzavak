import json
from flask import Flask,request,jsonify,abort
from flask_cors import cross_origin,CORS
from controller import selectRandomWords,selecRandomWordsWithLenght,selectRandomWordsStartWith
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route("/getwords/<int:nums>/<sw>/<int:l>")
@cross_origin()
def getWords(nums,sw,l):
    try:
        if sw != "*" and l == "*":
            selectedWords = selectRandomWords(nums)
            pass
        elif sw == "*" and l != "*":
            selectedWords = selecRandomWordsWithLenght(nums,int(l))
            pass
        elif sw != "*" and l != "*":
           pass
        else:
            selectedWords = selectRandomWords(nums)
            pass
            

        
        returnData = {"words":list(selectedWords)}
        return jsonify(returnData)
        pass
    except Exception as e:
        raise e
if __name__  == "__main__":
    app.run(debug=True)