import json
import plotly
import pandas as pd


from flask import Flask
from flask import render_template, request, jsonify


app = Flask(__name__)

# index webpage displays cool visuals and receives user input text for model
@app.route('/')
@app.route('/index')
def index():        
    
    return render_template('index.html')





def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()