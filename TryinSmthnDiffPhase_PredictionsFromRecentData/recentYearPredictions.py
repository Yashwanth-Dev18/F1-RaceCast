# f1_predictor_smart.py
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('f1records.csv')

# Create meaningful features instead of one-hot encoding
def create_smart_features(df):
    # Convert to numeric if needed
    df['race_results'] = pd.to_numeric(df['race_results'], errors='coerce')
    df = df.dropna(subset=['race_results'])
    
    # Extract year from car name (e.g., "McLaren: MCL39 - 2025" -> 2025)
    def extract_year(car_name):
        if '-' in car_name:
            return int(car_name.split('-')[-1].strip())
        return 2023  # default
    
    # Extract team from car name (e.g., "McLaren: MCL39 - 2025" -> "McLaren")
    def extract_team(car_name):
        if ':' in car_name:
            return car_name.split(':')[0].strip()
        return car_name
    
    # Create new features
    df['car_year'] = df['car'].apply(extract_year)
    df['team'] = df['car'].apply(extract_team)
    
    # Calculate rolling averages (this is the key!)
    df['driver_3race_avg'] = df.groupby('driver')['race_results'].transform(
        lambda x: x.shift(1).rolling(3, min_periods=1).mean()
    )
    
    df['team_3race_avg'] = df.groupby('team')['race_results'].transform(
        lambda x: x.shift(1).rolling(3, min_periods=1).mean()
    )
    
    # Fill NaN values with reasonable defaults
    df['driver_3race_avg'].fillna(10, inplace=True)
    df['team_3race_avg'].fillna(10, inplace=True)
    
    return df

# Create smart features
df = create_smart_features(df)

# Filter to only recent data (2020-2023) since 2014 data is too old
df_recent = df[df['car_year'] >= 2020]

# Prepare features
features = ['driver_3race_avg', 'team_3race_avg', 'car_year']
X = df_recent[features]
y = df_recent['race_results']

# Train/test split
train_mask = df_recent['car_year'] < 2023
test_mask = df_recent['car_year'] >= 2023

X_train, X_test = X[train_mask], X[test_mask]
y_train, y_test = y[train_mask], y[test_mask]

print(f"Training set: {len(X_train)} samples")
print(f"Test set: {len(X_test)} samples")

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
test_preds = model.predict(X_test)
mae = mean_absolute_error(y_test, test_preds)
print(f"Test MAE: {mae:.3f}")

# Smart prediction function
def smart_predict(driver, team, car_year, recent_driver_form=2.0, recent_team_form=2.0):
    """
    driver: driver name (e.g., "NOR")
    team: team name (e.g., "McLaren") 
    car_year: year of the car (e.g., 2025)
    recent_driver_form: estimated avg position in last 3 races (e.g., 2.0 for great form)
    recent_team_form: estimated team avg position in last 3 races (e.g., 2.0 for great form)
    """
    input_features = np.array([[recent_driver_form, recent_team_form, car_year]])
    prediction = model.predict(input_features)[0]
    
    print(f"\nPrediction for {driver} ({team} {car_year}):")
    print(f"Based on: Driver form P{recent_driver_form}, Team form P{recent_team_form}")
    print(f"Predicted position: P{round(prediction)} (raw: {prediction:.2f})")
    
    return prediction

# Example: Norris in McLaren 2025 (assuming great recent form)
print("\n" + "="*50)
print("SMART PREDICTION")
print("="*50)
smart_predict("NOR", "McLaren", 2025, recent_driver_form=2.5, recent_team_form=2.0)