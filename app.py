# Triggering CI

from flask import Flask, jsonify # type: ignore

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify(message="Hello, CI/CD World!")

if __name__ == '__main__':
    app.run(debug=True)