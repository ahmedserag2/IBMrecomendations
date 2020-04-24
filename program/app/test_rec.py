from RecomendationRankBased import rank_based
from RecomendationCollaborative import Collaborative
import pandas as pd
import numpy as np 

import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
print(my_path)
path1 = os.path.join(my_path, "../data/user-item-interactions.csv")
path2 = os.path.join(my_path, "../data/articles_community.csv")
#print(path1)
df = pd.read_csv(path1)
df_content = pd.read_csv(path2)
#rank = rank_based(df)
#print(rank.get_top_articles(10,'article_id'))

#print(df.head())

colrecs = Collaborative(df)
rec_ids, rec_names = colrecs.user_user_recs_part2(20, 10)
print("The top 10 recommendations for user 20 are the following article ids:")
print(rec_ids)
print()
print("The top 10 recommendations for user 20 are the following article names:")
print(rec_names)
