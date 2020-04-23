import json
import plotly
import pandas as pd

import os.path


from flask import Flask
from flask import render_template, request, jsonify
from RecomendationRankBased import rank_based

app = Flask(__name__)

# index webpage displays cool visuals and receives user input text for model

my_path = os.path.abspath(os.path.dirname(__file__))
df_path = os.path.join(my_path, "../data/user-item-interactions.csv")

df = pd.read_csv(df_path)
rank = rank_based(df)

@app.route('/')
@app.route('/index')
def index():
	topRatedRecs = rank.get_top_articles(10,'article_id')
	return render_template('index.html',data = topRatedRecs)


# web page that handles user query and displays model results
@app.route('/recomendations')
def recomendations():
    # save user input in query
    query = request.args.get('query', '') 

    # use model to predict classification for query
    #classification_labels = model.predict([query])[0]
    #classification_results = dict(zip(df.columns[4:], classification_labels))
    

    # This will render the go.html Please see that file. 
    return render_template(
        'recomendations.html',
        query=query,
        classification_result=classification_results
    )



def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()