# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the Titanic dataset (available through seaborn or online)
# Using online URL for Titanic dataset (CSV file)
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic_data = pd.read_csv(url)

# Step 2: Data Exploration (viewing the first few rows and basic stats)
print(titanic_data.head())  # Display first 5 rows
print(titanic_data.describe())  # Summary statistics of the dataset
print(titanic_data.isnull().sum())  # Checking for missing values in the dataset

# Step 3: Data Cleaning (handling missing values)
# Fill missing age values with the median age
titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)
# Fill missing embarked values with the most common port 'S'
titanic_data['Embarked'].fillna('S', inplace=True)

# Drop 'Cabin' column due to too many missing values
titanic_data.drop('Cabin', axis=1, inplace=True)

# Convert categorical variables to numeric (Sex, Embarked)
titanic_data['Sex'] = titanic_data['Sex'].map({'male': 0, 'female': 1})
titanic_data['Embarked'] = titanic_data['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

# Step 4: Data Preparation (selecting features and target variable)
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
X = titanic_data[features]  # Features
y = titanic_data['Survived']  # Target (Survived or not)

# Split the data into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Modeling (using a Decision Tree Classifier to predict survival)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Step 6: Evaluation (predicting on the test set and checking accuracy)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')

# Step 7: Visualization (Plot feature importance)
importances = model.feature_importances_
plt.figure(figsize=(10, 6))
plt.barh(features, importances, color='skyblue')
plt.title('Feature Importance')
plt.xlabel('Importance')
plt.show()
