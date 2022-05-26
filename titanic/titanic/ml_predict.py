# Correct order in the dataframe
def prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title):
  import pickle
  # from sklearn.ensemble._forest import RandomForest
  x=[[pclass,sex,age,sibsp,parch,fare,embarked,title]]
  # prediction=pickle.format_version
  randomforest=pickle.load(open('titanic_model.sav','rb'))
  prediction =randomforest.predict(x)
  if prediction == 0:
      prediction ='Did not Survive'
  elif prediction == 1:
      prediction = 'Survived'
  else:
      prediction='Error! Please ensure you have keyed in positive integers in the fields of the form'
  return prediction
