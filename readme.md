# Disaster Response Pipeline Project

### Project Motivation:
This project is aimed to visualize and classify disaster messages from the DisasterResponse data sets.

### project phases:
In this project there were 3 phases:
1. build an ETL pipeline to load,clean and save data from the database
2. buid a ML pipeline to deploy a clasification model
3. the flask app which uses the ML model to classify messages and runs visualizations on the data set

### libraries and frameworks used
- pandas
- sklearn
- numpy
- plotly
- flask(framework)

### Acknowledgments
Udacity for making such a complete nanodegree
IBM for providing the datasets and making this project possible

### runnning:
1. to run the flask app run the following command in the program/app directory.

    - python run.py

2. Go to http://0.0.0.0:3001/

### room for Improvments:
- i would start by modularizing the code some more by putting the user_id in the collaborative filtering class itself
		this way each colaborativerec object would have its own user_id and its own recomendations and wont be just some
		object i could call just to get the recomendations
- an ETL aproach were i can run python scripts to wrangle my data instead of mapping the each user email to user_id in the 
		run.py file

- for the users that dont have much reccomendations because they didnt read much articles in the first place content based filtering would be needed

