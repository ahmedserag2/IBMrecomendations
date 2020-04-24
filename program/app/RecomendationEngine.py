import pandas as pd

class recomender:
	def __init__(self,df):
		self.df = df
		email_encoded = self.email_mapper()
		del self.df['email']
		df['user_id'] = email_encoded


	def email_mapper(self):
	    coded_dict = dict()
	    cter = 1
	    email_encoded = []
	    
	    for val in self.df['email']:
	        if val not in coded_dict:
	            coded_dict[val] = cter
	            cter+=1
	        
	        email_encoded.append(coded_dict[val])

	    return email_encoded

	