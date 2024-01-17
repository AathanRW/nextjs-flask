from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/api/python")
def hello_world():
    qwe = [{'username': "hello"}]
    return jsonify(qwe)
