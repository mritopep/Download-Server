from flask import Flask
from flask import send_file
from flask_ngrok import run_with_ngrok
app = Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def index():
    path = "/Examples.pdf"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run() 
