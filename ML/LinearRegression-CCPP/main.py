import math
import pandas as pd   #for reading the data
import sklearn   #for machine learning algorithms
from sklearn.linear_model import LinearRegression   #Loading Linear Regression
from sklearn.model_selection import train_test_split    #splitting the data for training and testing
from sklearn.metrics import mean_squared_error    #metric to evaluate the result

#READING DATA
dataset_path= "[DATAPATH]"
df=pd.read_excel(dataset_path)    #reading the dataset
print(df.head())    #to check if the data has been loaded properly

#EXTRACTING VALUE(X) AND TARGET(Y) FROM DF
X=df[["AT"]]    #Scikit-learn expects X to be a 2D structure (a DataFrame), so use double brackets when selecting the column in pandas.
y=df["PE"]    #y can be a 1D structure (a Series), so single brackets are fine.

#SPLITTING THE TRAINING AND TESTING DATA
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)   #to check whether it has been split

#REGRESSION
model = LinearRegression()
model.fit(X_train,y_train)

#PREDICTIONS
predictions=model.predict(X_test)
mse= mean_squared_error(y_test,predictions)
rmse= math.sqrt(mse)
print("The prediction done by your model was off by",rmse,"KW")
