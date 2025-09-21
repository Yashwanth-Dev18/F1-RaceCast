import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Data
df = pd.read_csv('f1records.csv')

# Define the target column
TARGET_COL = 'race_results'

# Separate features (X) and target (y)
y = df[TARGET_COL]  # This is what we want to predict (1-20)
X = df.drop(columns=[TARGET_COL])

# Splitting the data into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42, stratify=y
)

# Training the Random Forest Model
# Model: Random Forest (Generally works well out of the box)
rf_model = RandomForestRegressor(
    n_estimators=200,      # More trees = better performance, but slower
    max_depth=15,          # Limit tree depth to prevent overfitting
    min_samples_split=5,   # Minimum samples required to split a node
    min_samples_leaf=2,    # Minimum samples required at a leaf node
    random_state=42,
    n_jobs=-1              # Use all CPU cores
)
rf_model.fit(X_train, y_train)

# MODEL EVALUATION

# Training set evaluation
y_pred = rf_model.predict(X_train)
mae = mean_absolute_error(y_train, y_pred)
mse = mean_squared_error(y_train, y_pred)
r2 = r2_score(y_train, y_pred)

print(f"\nMean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
print(f"R-squared: {r2}")

# Test set evaluation
y_pred = rf_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\nMean Squared Error: {mse}")
print(f"Mean Absolute Error: {mae}")
print(f"R-squared: {r2}")