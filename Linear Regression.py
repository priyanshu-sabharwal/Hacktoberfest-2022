##Building a Linear Regression Model
#Predicting the percentage of a student by the number of hours they studied
#Author : Harshdeep Singh Narula
#The code will run successfully run on Jupyter Notebook or Google Colab

#Importing Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing Dataset


url = "http://bit.ly/w-data"
data = pd.read_csv(url)
data.head()


x=data[['Hours']]
y=data['Scores']


#Plotting the data


plt.scatter(x,y,color='green')
plt.title('Hours vs Percentage')  
plt.xlabel('Hours')  
plt.ylabel('Percentage')  
plt.show()

#Splitting data into test and train dataframes


from sklearn.model_selection import train_test_split as tts
x_train,x_test,y_train,y_test=tts(x,y,test_size=0.2,random_state=42)
x_test

#Model Fitting


from sklearn.linear_model import LinearRegression
trainer=LinearRegression()
trainer.fit(x_train,y_train)


#Plotting the Best Fit


plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,trainer.predict(x_train))
plt.title('Comparison of training values with the prepared model')
plt.xlabel('Hours')
plt.ylabel('Percentage')
plt.show()

#Predicting Values


y_pred=trainer.predict(x_test)

df=pd.DataFrame({'Actual': y_test,'Predicted': y_pred})

print(df)

val=[[9.25]]
val_pred=trainer.predict(val)
print("No of Hours = {0}".format(val[0][0]))
print("Predicted Score = {0}".format(val_pred[0]))

#Evaluation metrics


from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred)) 


from sklearn.metrics import r2_score
r=r2_score(y_test,y_pred)
print("R2 score : {}".format(r))
