from RecomendationRankBased import rank_based

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
rank = rank_based(df)
print(rank.get_top_articles(10,'article_id'))