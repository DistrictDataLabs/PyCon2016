![Machine learning flow](machine_learning_flow.jpg)


![The machine learning application pipeline](ML_pipeline.jpg)  


![Machine learning application architecture with Flask](ML_architecture_flask.jpg)    
-the center is a postgres database that acts to both power the web application and also as computation data store for your instances

-load data, use SQL query to join, dump

-use scikit learn to run models, evaluate models, select the best one and dump to database

-the web will look for the best model load into pickle and make predictions

-as the user interacts  with web app, log data and store to DB to add to future fit predict cycles and allow app to learn and change over time

build phase ends up in the computational datastore
central application leads down to operational phase
feeds back into model and application

![Large machine learning application architecture](large_ML_architecture.jpg)
