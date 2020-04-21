from RecomendationEngine import recomender
import pandas as pd 

import os.path



class rank_based(recomender):


	def __init__(self,df):
		recomender.__init__(self,df)

	def get_top_articles(self,n, col_id):
		"""INPUT:
			n - (int) the number of top articles to return
			df - (pandas dataframe) df as defined at the top of the notebook 
		    
	    OUTPUT:
	    	top_articles - (list) A list of the top 'n' article titles 
	    
		"""
		titles = []
		ids = self.get_top_article_ids(n,col_id)
		return self.df.drop_duplicates(subset = 'article_id')[self.df['article_id'].isin(ids)]['title']
	    # Return the top article titles from df (not df_content)

	def get_top_article_ids(self,n,col_id):
		'''
	    INPUT:
	    n - (int) the number of top articles to return
	    df - (pandas dataframe) df as defined at the top of the notebook 
	    
	    OUTPUT:
	    top_articles - (list) A list of the top 'n' article titles 
	    
		'''
	    # Your code here
	     
		return self.df[col_id].value_counts().index[:n] # Return the top article ids