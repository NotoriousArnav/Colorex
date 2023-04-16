from flask import (
        jsonify, 
        Flask,
        render_template
    )

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')

@app.post('/results')
def results():
    return ''
