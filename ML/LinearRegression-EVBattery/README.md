# EV Battery State of Health (SOH) Predictor
## Overview
This project implements a Multiple Linear Regression machine learning model to predict the degradation and State of Health (SOH) of Electric Vehicle (EV) batteries. By analyzing charging cycles and related battery metrics, the model accurately estimates the remaining health of lithium-ion cells, which is a critical metric for EV performance modeling and warranty forecasting.

## Dataset
The model is trained on the Electric Vehicle (EV) Battery Degradation & Charge dataset from Kaggle.

## Tech Stack
**Language**: Python  
**Libraries**: pandas, scikit-learn, kagglehub  
**Environment**: Google Colab / Jupyter Notebook  

## Key Features
**Automated Data Retrieval**: Uses kagglehub to directly download the latest dataset version into the environment.  
__Multiple Linear Regression__: Utilizes sklearn.linear_model.LinearRegression to analyze multi-dimensional relationships between charging habits and battery degradation. (y=mx1+mx2+mx3)  
__High Accuracy Tracking__: By properly isolating State of Health (SOH) as the target variable rather than raw capacity fluctuations, the model achieves a Root Mean Squared Error (RMSE) of approximately 1.37%.
