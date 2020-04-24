import json
import plotly
import pandas as pd
from RecomendationCollaborative import Collaborative

import os.path


from flask import Flask
from flask import render_template, request, jsonify
from RecomendationRankBased import rank_based

app = Flask(__name__)

def email_mapper():
        coded_dict = dict()
        cter = 1
        email_encoded = []
        
        for val in df['email']:
            if val not in coded_dict:
                coded_dict[val] = cter
                cter+=1
            
            email_encoded.append(coded_dict[val])

        return email_encoded



# index webpage displays cool visuals and receives user input text for model

my_path = os.path.abspath(os.path.dirname(__file__))
df_path = os.path.join(my_path, "../data/user-item-interactions.csv")

df = pd.read_csv(df_path)
email_encoded = email_mapper()
del df['email']
df['user_id'] = email_encoded
rank = rank_based(df)
colrecs = Collaborative(df)
topRatedRecs = rank.get_top_articles(10,'article_id')


@app.route('/')
@app.route('/index')
def index():
    query = request.args.get('query', int('1')) 

    rec_ids, rec_names = colrecs.user_user_recs_part2(query, 10)

    return render_template('index.html',data = topRatedRecs,userMatch = rec_names)


# web page that handles user query and displays model results
@app.route('/recomendations')
def recomendations():
    # save user input in query

    # use model to predict classification for query
    #classification_labels = model.predict([query])[0]
    #classification_results = dict(zip(df.columns[4:], classification_labels))
    query = request.args.get('query', int('1')) 
    rec_ids, rec_names = colrecs.user_user_recs_part2(int(query), 10)


    # This will render the go.html Please see that file. 
    return render_template(
        'recomendations.html',
        data = topRatedRecs,userMatch=rec_names
    )



def main():
    app.run(host='0.0.0.0', port=3001, debug=True)


if __name__ == '__main__':
    main()