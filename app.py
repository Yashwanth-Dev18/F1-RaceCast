import pandas as pd
import numpy as np
import joblib

# 1. Load the trained model
model = joblib.load("f1_xgb_model.pkl")

# 2. Load dataset columns for one-hot encoding
df = pd.read_csv("f1records.csv")  # just to get column names
columns = df.columns.tolist()
columns.remove("race_results")  # remove target

# 3. Function to create a one-hot encoded input vector
def create_input_vector(driver, track, car, track_condition):

    vector = np.zeros(len(columns))

    # Match driver
    driver_col = [c for c in columns if c.startswith(driver)]
    if driver_col:
        idx = columns.index(driver_col[0])
        vector[idx] = 1

    # Match track
    track_col = [c for c in columns if track in c]
    if track_col:
        idx = columns.index(track_col[0])
        vector[idx] = 1

    # Match car
    car_col = [c for c in columns if c == car]
    if car_col:
        idx = columns.index(car_col[0])
        vector[idx] = 1

    # Track condition
    if track_condition.lower() == "dry":
        idx = columns.index("dry_track")
        vector[idx] = 1
    elif track_condition.lower() == "wet":
        idx = columns.index("wet_track")
        vector[idx] = 1
    else:
        raise ValueError("track_condition must be 'dry' or 'wet'")

    return vector.reshape(1, -1)

# 4. Function to predict finishing position
def predict_result(driver, track, car, track_condition):
    X_input = create_input_vector(driver, track, car, track_condition)
    pred = model.predict(X_input)
    if int(round(pred[0])) <= 0:
        print("Predicted finishing position: P1")
    elif int(round(pred[0])) > 20:
        print("Predicted finishing position: P20")
    else:
        print(f"Predicted finishing position: P{int(round(pred[0]))}")

# 5. Example usage
if __name__ == "__main__":
    # Replace these with your desired scenario
    predict_result(
        driver="VER",
        track="Monaco",
        car="RB19",
        track_condition="dry"
    )