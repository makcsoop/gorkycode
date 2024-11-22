from flask import Flask
from scripts import note



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    
    return ""

if __name__ == '__main__':
    app.run(port=8000, host='localhost')