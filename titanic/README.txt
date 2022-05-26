This Django project builds a web application that classify whether
a Titanic passenger is likely to survive based on the input information.


- pclass [Passenger Class: Key in an integer, where 1='1st', 2='2nd', 3='3rd']

- sex [Gender: Key in an integer, where 0='Male', 1='Female']

- age [Age: Enter a positive number, e.g. 1-100]

- sibsp [Number of Siblings and Spouses onboard: Key in a non-negative integer]

- parch [Number of parents and children onboard: Key in a non-negative integer]

- fare [Fare paid by passenger: Key in a positive number]

- embarked [Port of Embarkation: Key in an integer where, 0='Southampton', 1='Cherbourg', 2='Queenstown']

- title [Title of passenger: Key in an integer, where (0,1,2,3,4,5,6,7)=('Mr','Miss','Mrs','Master','Dr','Rev','Officer','Royalty') ]</p>

The input features are derived from the training dataset of Kaggle Titanic - Machine Learning from Disaster
https://www.kaggle.com/competitions/titanic/data


To run the web app locally in your own computer: open terminal and run the commands
> cd titanic
This is to change directory to where 'manage.py' is located within the repository
> python manage.py runserver

Files needed for running Django project:
- All files except those involved training, where it was used prior to
generating the titanic_model.sav for model inference/prediction 
