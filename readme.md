# Disaster Response Pipeline Project

### Project Motivation:
This is a recomendation engine aimed to provide articles for the users to read on the IBM watson platform.

### Acknowledgments
Udacity for making such a complete nanodegree
IBM for providing the datasets and making this project possible

### project phases:
In this project there were 2 phases:
1. taking a functional aproach aimed to analyze the data and quickly provide recomendations in jupyter notebooks
2. an OOP aproach aimed to implement all my recomendations into the flask app


### directories
There are two main directories in this project
1. the program (contains the flask application,templates and the datasets)
2. the notebook and tests(this is whats basically provided in the udacity workspace)

### the recommendations methods used:
1. rankbased approach returns the top rated articles
2. collaborative filtering using SVD(not included in flask app)
 and calculating coefficents using the dot product


### libraries and frameworks used
- pandas
- sklearn
- numpy
- flask(framework)



### runnning:
1. to run the flask app run the following command in the program/app directory.

    - python run.py

2. Go to http://0.0.0.0:3001/

3. NOTE : the flask app is fully functional but the notebook might give you an error if you tried running it because
	i am using an absolute file path for the csv files so just replace with your filepath 

### room for Improvments:
- i would start by modularizing the code some more by putting the user_id in the collaborative filtering class itself
		this way each colaborativerec object would have its own user_id and its own recomendations and wont be just some
		object i could call just to get the recomendations
- an ETL aproach were i can run python scripts to wrangle my data instead of mapping the each user email to user_id in the 
		run.py file

- for the users that dont have much reccomendations because they didnt read much articles in the first place content based filtering would be needed

