
import os.path
import pandas as pd
import numpy as np
from RecomendationEngine import recomender


my_path = os.path.abspath(os.path.dirname(__file__))
print(my_path)
path1 = os.path.join(my_path, "../data/user-item-interactions.csv")
path2 = os.path.join(my_path, "../data/articles_community.csv")
#print(path1)
df = pd.read_csv(path1)
df_content = pd.read_csv(path2)

## No need to change the code here - this will be helpful for later parts of the notebook
# Run this cell to map the user email to a user_id column and remove the email column

class Collaborative(recomender):

    def __init__(self,df):
            recomender.__init__(self,df)
            self.user_item = self.create_user_item_matrix()


    



    def create_user_item_matrix(self):
        '''
        INPUT:
        df - pandas dataframe with article_id, title, user_id columns
        
        OUTPUT:
        user_item - user item matrix 
        
        Description:
        Return a matrix with user ids as rows and article ids on the columns with 1 values where a user interacted with 
        an article and a 0 otherwise
        '''
        # Fill in the function here
        #drop duplicates to limit user-article to only zero and one
        user_article =  self.df.drop_duplicates(subset = ['article_id','user_id']) \
        .groupby(['user_id','article_id'])['title'].count().unstack()
        user_article.fillna(0,inplace = True)
        return user_article
     # return the user_item matrix 





    def get_article_names(self,article_ids):
        '''
        INPUT:
        article_ids - (list) a list of article ids
        df - (pandas dataframe) df as defined at the top of the notebook
        
        OUTPUT:
        article_names - (list) a list of article names associated with the list of article ids 
                        (this is identified by the title column)
        '''
        # Your code here
        article_names = self.df.loc[self.df['article_id'].isin(article_ids)].title.drop_duplicates()
        return article_names # Return the article names associated with list of article ids



    def get_user_articles(self,user_id):
        '''
        INPUT:
        user_id - (int) a user id
        user_item - (pandas dataframe) matrix of users by articles: 
                    1's when a user has interacted with an article, 0 otherwise
        
        OUTPUT:
        article_ids - (list) a list of the article ids seen by the user
        article_names - (list) a list of article names associated with the list of article ids 
                        (this is identified by the doc_full_name column in df_content)
        
        Description:
        Provides a list of the article_ids and article titles that have been seen by a user
        '''
        # Your code here
        #in the user_id i did a minus 1 because user ids begin from 1
        article_ids = self.user_item.iloc[user_id-1][self.user_item.iloc[user_id-1] == 1].index.values
        article_names = self.get_article_names(article_ids)
        return article_ids, article_names # return the ids and names






    def get_top_sorted_users(self,user_id):
        '''
        INPUT:
        user_id - (int)
        df - (pandas dataframe) df as defined at the top of the notebook 
        user_item - (pandas dataframe) matrix of users by articles: 
                1's when a user has interacted with an article, 0 otherwise
        
                
        OUTPUT:
        neighbors_df - (pandas dataframe) a dataframe with:
                        neighbor_id - is a neighbor user_id
                        similarity - measure of the similarity of each user to the provided user_id
                        num_interactions - the number of articles viewed by the user - if a u
                        
        Other Details - sort the neighbors_df by the similarity and then by number of interactions where 
                        highest of each is higher in the dataframe
         
        '''
        # Your code here
        similar_users = self.user_item.loc[user_id , :].dot(self.user_item.T).sort_values(ascending=False)
        similar_users = similar_users.loc[~(similar_users.index==user_id)]

        interactions_df = pd.DataFrame({'number_of_interactions':self.df['user_id'].value_counts()})
        neighbours_df = pd.DataFrame({'similarity': similar_users})
        neighbours_df = pd.concat([neighbours_df, interactions_df], join="inner",axis = 1).reset_index()
        neighbours_df.rename(columns = {'index' : 'neighbour_id'},inplace = True)
        neighbours_df.sort_values(["similarity", "number_of_interactions"], ascending = (False, False) ,inplace = True)
        #neighbours_df.drop_duplicates(article_ids)
        return neighbours_df # Return the dataframe specified in the doc_string


    def user_user_recs_part2(self,user_id, m=10):
        '''
        INPUT:
        user_id - (int) a user id
        m - (int) the number of recommendations you want for the user
        
        OUTPUT:
        recs - (list) a list of recommendations for the user by article id
        rec_names - (list) a list of recommendations for the user by article title
        
        Description:
        Loops through the users based on closeness to the input user_id
        For each user - finds articles the user hasn't seen before and provides them as recs
        Does this until m recommendations are found
        
        Notes:
        * Choose the users that have the most total article interactions 
        before choosing those with fewer article interactions.

        * Choose articles with the articles with the most total interactions 
        before choosing those with fewer total interactions. 
       
        '''

        # Your code here
        similar_user_ids = self.get_top_sorted_users(user_id).neighbour_id
        user_articles_ids,user_articles_titles = self.get_user_articles(user_id)
        recs = []
        rec_names = []
        #initialized two counters used an iterative approach 
        i,j = 0 , 0
        
        while(i < m):
            neighbour_articles_ids,neighbour_articles_titles = self.get_user_articles(similar_user_ids[j])
            common_articles = np.intersect1d(user_articles_ids , neighbour_articles_ids)
            df.drop_duplicates(subset = 'article_id').loc[df.drop_duplicates()['article_id'].isin(common_articles)].article_id.value_counts().index
            for article in common_articles:
                recs.append(article)  
                i += 1
                if i >= m:
                    break
            j += 1
        
        rec_names = list(self.get_article_names(recs))
        return recs , rec_names



