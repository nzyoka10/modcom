# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

# Load the Iris dataset (preloaded dataset in seaborn for simplicity)
from sklearn.datasets import load_iris
iris = load_iris()

# Convert the dataset into a pandas DataFrame
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Step 1: Data Exploration (basic statistics and data visualization)
print(df.head())  # Display the first 5 rows of the dataset
print(df.describe())  # Get summary statistics of the data

# Visualize the data - scatter plot of sepal length vs. sepal width
plt.figure(figsize=(8, 6))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['species'])
plt.title('Sepal Length vs. Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.show()

# Step 2: Data Preparation (split data into training and testing sets)
X = df.drop('species', axis=1)  # Features
y = df['species']  # Target (species)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Modeling (using Logistic Regression to classify species)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Step 4: Evaluation (testing the model and checking accuracy)
y_pred = model.predict(X_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy * 100:.2f}%')
