import pandas as pd
import numpy as np

data=pd.read_csv('diabetes.csv')

data.head()

df=data[['Pregnancies','Age','Glucose','BloodPressure','SkinThickness','Insulin','BMI','Outcome']]

df.head()

x=df[['Glucose','BloodPressure','SkinThickness','Insulin','Pregnancies','Age','BMI']]
y=df['Outcome']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.20,random_state=51)

from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

model=LogisticRegression()

model.fit(x_train,y_train)
'''
model.score(x_train,y_train)

model.score(x_test,y_test)

confusion_matrix(y_train,model.predict(x_train))

aa=model.predict_proba([[183,64,0,0,8,32,30]])
print(model.predict([[183,64,0,0,8,32,40]]))
aa
'''
import joblib

path="predictive_model.sav"
joblib.dump(model,path)

