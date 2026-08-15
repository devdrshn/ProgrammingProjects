#IMPORTING DATASET FOR Electric Vehicle (EV) Battery Degradation & Charge
import kagglehub
# Download latest version
path = kagglehub.dataset_download("bertnardomariouskono/electric-vehicle-ev-battery-degradation-and-charge")
print("Path to dataset files:", path)

from google.colab import drive    #mounting drive onto the notebook
drive.mount('/content/drive')

#IMPORTING ML LIBRARIES
import pandas as pd
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error

#LOADING DATASET AS DF
dataset_path="[DATASET PATH]"
df=pd.read_csv(dataset_path)
print(df.head())

#ASSIGNING FEATURES AND TARGET
X=df[["'Total_Charging_Cycles','Battery_Capacity_kWh','Avg_Temperature_C'"]])  #Change the features to see the differences in predictions
y=df['SoH_Percent']

#SPLITTING DATASET
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#TRAINING MODEL
model=LinearRegression()
model.fit(X_train,y_train)

#PREDICTING
predictions=model.predict(X_test)
val=root_mean_squared_error(y_test,predictions)
print("Your prediction was off by",val,"% from the actual State of Health of the EV Battery.")
