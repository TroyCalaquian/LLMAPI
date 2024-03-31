from flask import Flask, request, jsonify
from model import use_pipeline

app = Flask(__name__)

@app.route('/')
def intro():
  return 'Congrats, this is the entry point! Use /convert to convert smth'

@app.route('/convert', methods=['POST'])
def convertroute():
  data = request.json
  text = data['text']
  response = use_pipeline(text)
  return jsonify({'response': response})

if __name__ == '__main__':
  app.run(host='0.0.0.0')