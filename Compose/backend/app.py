from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hallo, dit is de Flask backend die praat met MySQL!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
