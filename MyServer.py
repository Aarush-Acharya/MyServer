from flask import Flask, jsonify, request
import os
from flask_cors import CORS
from discord import SyncWebhook


app = Flask(__name__)
CORS(app, origins=["*"])


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

@app.route('/webhook', methods=['POST'])
def onhook():
    body = request.json
    print("Hey "+ body['sender']['login'] +" interacted with a new "+ str(list(body.values())[0]) + " "+  str(list(body.keys())[1]) + " in "+ body['repository']['name'] + " belonging to "+  body['repository']['owner']['login'])
    webhook = SyncWebhook.from_url("https://discord.com/api/webhooks/1125510554585419828/lrwnSYeYQuvYHLtT4X5W5eYVMqi5J1802PfAc5WYf9VpyVQE5GI9QKKSzr4yIZCR6jmN")
    webhook.send("Hey "+ body['sender']['login'] +" did a new "+ str(list(body.values())[0]) + " "+  str(list(body.keys())[1]) + " in "+ body['repository']['name']+" belonging to "+  body['repository']['owner']['login'])
    return jsonify({'body': body})
    # payload = body.getlist('payload')
    # print(payload)

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5666))