# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:38:12 2024

@author: Lenovo
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import csv

# Load the dataset from CSV
#csv_file_path = 'output_with_analyst.csv'
csv_file_path = 'output10.csv'

df = pd.read_csv(csv_file_path)

# Separate features (X) and target variable (y)
X = df[['Rule Description', 'Level']]
y = df['Analyst']

# Perform one-hot encoding on the categorical column 'Rule Description'
# ColumnTransformer is used to apply transformations to different columns
# OneHotEncoder is used to encode the 'Rule Description' column
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [0])], remainder='passthrough')
X_encoded = ct.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Initialize and train the random forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of the random forest classifier: {accuracy:.2f}")


with open('output11.csv') as file_obj: 
      
    # Create reader object by passing the file  
    # object to reader method 
    reader_obj = csv.reader(file_obj) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    s1=0
    for row in reader_obj: 
        if s1>0:
            #print(row)
            new_event = pd.DataFrame([row], columns=['Rule Description', 'Level'])
            new_event_encoded = ct.transform(new_event)
            predicted_analyst = rf_classifier.predict(new_event_encoded)
            #print(f"Predicted Analyst for the new event: {predicted_analyst[0]}")
            print("Incident "+str(row)+" has been assigned to : "+str(predicted_analyst[0]))
            print('')
            s1=s1+1
        else:
            s1=s1+1