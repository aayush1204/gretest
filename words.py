from flask import *
import json
from flask import Flask, request, make_response, jsonify
import pandas as pd
import numpy as np

import random
app = Flask(__name__)

def respond(fullfilment):
    return make_response(jsonify({'fulfillmentText': fullfilment}))

@app.route('/')
def login():
    return "ananya"
    # return render_template("info.html")

@app.route('/success')
def departures_handler():
    try:
        req = request.get_json(silent=True, force=True)
        print(json.dumps(req))

        df = pd.read_excel('vocabulary.xls')
        print(df)
        x = random.randint(4, 1000)
        return respond("Word - " + df.iloc[x][0] + " "+ "Meaning - " + df.iloc[x][1])

        # location = req.get('queryResult').get('parameters').get('current-location')

        # if location == 'home':
        #     return respond("Oh so you are home now. Well, you better hurry!")
        # elif location == 'work':
        #     return respond("At work? Well, are you sure it's time to leave already?")
        # else:
        #     return respond("I am not sure where " + location + " is.")


    except Exception as e:
        print(e)
        return respond("Sorry, an error occurred. Please check the server logs.")




if __name__=="__main__":
    app.run(debug=True)
