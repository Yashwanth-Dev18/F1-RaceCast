import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# -----------------------------------
#  LOADING AND PREPARING THE DATA
# -----------------------------------
#print("Loading data...")
df = pd.read_csv('f1records.csv')

# Define the target column
TARGET_COL = 'race_results'

# Separate features (X) and target (y)
y = df[TARGET_COL]  # This is what we want to predict (1-20)
X = df.drop(columns=[TARGET_COL])

# print(f"Dataset shape: {X.shape}")
# print(f"Target value range: {y.min()} to {y.max()}")

# ----------------------------
#   TRAIN-TEST DATA SPLIT
# ----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
# print(f"Training set: {X_train.shape}, Test set: {X_test.shape}")

# -------------------------------------
#   TRAINING GRADIENT BOOSTING MODEL
# -------------------------------------

# Model: Gradient Boosting (Often gives best performance)


gb_model = GradientBoostingRegressor(
    n_estimators=150,
    learning_rate=0.1,
    max_depth=8,
    random_state=42
)

# gb_model = GradientBoostingRegressor(
#     n_estimators=200,           # More trees for better learning
#     learning_rate=0.05,         # Slower learning to capture patterns
#     max_depth=6,                # Better generalization
#     min_samples_split=20,       # Prevent overfitting
#     min_samples_leaf=10,        # More robust to noise
#     subsample=0.8,              # Stochastic gradient boosting
#     random_state=42,
#     max_features='sqrt'
# )

gb_model.fit(X_train, y_train)

# -------------------------
#   EVALUATING THE MODEL
# -------------------------
def evaluate_model(model, X_test, y_test, model_name):
    print(f"\n{model_name} Evaluation:")
    print("=" * 40)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Calculate metrics
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Mean Absolute Error (MAE): {mae:.3f}")
    print(f"Root Mean Squared Error (RMSE): {rmse:.3f}")
    print(f"R² Score: {r2:.3f}")
    
    # Additional analysis
    accuracy_within_1 = np.mean(np.abs(y_test - y_pred) <= 1)
    accuracy_within_2 = np.mean(np.abs(y_test - y_pred) <= 2)
    accuracy_within_3 = np.mean(np.abs(y_test - y_pred) <= 3)
    
    print(f"Accuracy within ±1 position: {accuracy_within_1:.2%}")
    print(f"Accuracy within ±2 positions: {accuracy_within_2:.2%}")
    print(f"Accuracy within ±3 positions: {accuracy_within_3:.2%}")
    
    return y_pred, mae
gb_pred, gb_mae = evaluate_model(gb_model, X_test, y_test, "Gradient Boosting")


# '-------------------------------------------------------------------'

# gb_pred, gb_mae = evaluate_model(gb_model, X_test, y_test, "Gradient Boosting")

# # 2. Add feature category analysis
# driver_cols = [col for col in X.columns if col in ['VER','HAM','LEC','RUS','PER','SAI','NOR','ALO','TSU','PIA','STR','LAW','HAD','BEA','OCO','HUL','BOR','GAS','COL','BOT','ZHO','RIC','VET','ROS','MAG','SCH','RAI','GRO','KVY','LAT','ERI','MAS','BUT','NAS','MAL','PAL','VAN','SAR','SUT']]
# car_cols = [col for col in X.columns if any(x in col for x in ['Mercedes','Ferrari','Red Bull','Williams','McLaren','Toro Rosso','Force India','Sauber','Lotus','Haas','Renault','AlphaTauri','Racing Point','Alfa Romeo','Aston Martin','Alpine','Racing Bulls','Kick Sauber'])]
# circuit_cols = [col for col in X.columns if any(x in col for x in ['Circuit','Autodrom','Grand Prix','International','Street'])]
# weather_cols = ['dry_track', 'wet_track']

# # Analyze feature importance by category
# importances = gb_model.feature_importances_
# feature_imp_df = pd.DataFrame({'feature': X.columns, 'importance': importances})
# feature_imp_df = feature_imp_df.sort_values('importance', ascending=False)

# def analyze_category_importance(feature_list, category_name):
#     cat_importance = feature_imp_df[feature_imp_df['feature'].isin(feature_list)]['importance'].sum()
#     print(f"{category_name} total importance: {cat_importance:.2%}")
#     return cat_importance

# car_importance = analyze_category_importance(car_cols, "Cars")
# driver_importance = analyze_category_importance(driver_cols, "Drivers")
# circuit_importance = analyze_category_importance(circuit_cols, "Circuits")
# weather_importance = analyze_category_importance(weather_cols, "Weather")

# print(f"\n🏎️ Car vs Driver Impact Ratio: {car_importance/driver_importance:.2f}x")

# # Show top features
# print(f"\n🔍 Top 10 Most Important Features:")
# print(feature_imp_df.head(10).to_string(index=False))

# '-----------------------------------------------------------------------'



# -----------------------
#   DATA VISUALIZATION
# -----------------------
'Visualizing data and evaluating model...'

# Scatter plot of predictions vs actual values
plt.figure(figsize=(12, 5))

# plt.subplot(1, 2, 1)
# plt.scatter(y_test, rf_pred, alpha=0.6, s=20)
# plt.plot([1, 20], [1, 20], 'r--', linewidth=2)
# plt.xlabel('Actual Position')
# plt.ylabel('Predicted Position')
# plt.title('Random Forest: Predicted vs Actual')
# plt.grid(True, alpha=0.3)

plt.subplot(1, 2, 2)
plt.scatter(y_test, gb_pred, alpha=0.6, s=20, color='orange')
plt.plot([1, 20], [1, 20], 'r--', linewidth=2)
plt.xlabel('Actual Position')
plt.ylabel('Predicted Position')
plt.title('Gradient Boosting: Predicted vs Actual')
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Error distribution plot
plt.figure(figsize=(10, 6))
errors = y_test - gb_pred
plt.hist(errors, bins=30, alpha=0.7, edgecolor='black')
plt.axvline(x=0, color='red', linestyle='--', linewidth=2)
plt.xlabel('Prediction Error (Actual - Predicted)')
plt.ylabel('Frequency')
plt.title('Distribution of Prediction Errors')
plt.grid(True, alpha=0.3)
plt.show()

# ------------------------
#   FEATURE IMPORTANCE
# ------------------------
'Analyzing feature importance...'

# importances = gb_model.feature_importances_
# feature_names = X.columns

# # Create DataFrame and sort by importance
# feature_imp_df = pd.DataFrame({'feature': feature_names, 'importance': importances})
# feature_imp_df = feature_imp_df.sort_values('importance', ascending=False)

# # Plot top 20 features
# plt.figure(figsize=(12, 8))
# top_features = feature_imp_df.head(20)
# sns.barplot(x='importance', y='feature', data=top_features)
# plt.title('Top 20 Most Important Features for Position Prediction')
# plt.xlabel('Importance')
# plt.tight_layout()
# plt.show()

# print("Top 10 most important features:")
# print(top_features.head(10).to_string(index=False))


# -------------------------
#    MAKE PREDICTIONS
# -------------------------
def predict_race_result(driver, car, circuit, weather_dry=True):
    "Predicts race result for a specific scenario"

    custom_input = pd.DataFrame([np.zeros(len(X.columns))], columns=X.columns)
    
    # Setting the relevant features to 1
    custom_input[driver] = 1
    custom_input[car] = 1
    custom_input[circuit] = 1
    custom_input['dry_track' if weather_dry else 'wet_track'] = 1
    
    # Make prediction
    prediction = gb_model.predict(custom_input)[0]
    return round(prediction, 1)


# def predict_race_result(driver, car, circuit, weather_dry=True):
#     "Predicts race result for a specific scenario with confidence"

#     custom_input = pd.DataFrame([np.zeros(len(X.columns))], columns=X.columns)
    
#     # Setting the relevant features to 1
#     custom_input[driver] = 1
#     custom_input[car] = 1
#     custom_input[circuit] = 1
#     custom_input['dry_track' if weather_dry else 'wet_track'] = 1
    
#     prediction = gb_model.predict(custom_input)[0]

#     predictions = []
#     for pred in gb_model.staged_predict(custom_input):
#         predictions.append(pred[0])
    
#     late_predictions = predictions[-50:]
#     mean_pred = np.mean(late_predictions)
#     std_pred = np.std(late_predictions)
    
#     confidence_interval = (max(1, mean_pred - std_pred), min(20, mean_pred + std_pred))
    
#     return round(mean_pred, 1), confidence_interval

# predicted_position, confidence = predict_race_result( 
#     driver='HAM',
#     car='Ferrari: SF-25 - 2025',
#     circuit='Baku City Circuit- Baku- AZERBAIJAN',
#     weather_dry=True
# )

# print(f"Predicted finishing position: P{int(predicted_position)}")
# print(f"Confidence interval: P{int(confidence[0])} to P{int(confidence[1])}")

# Example prediction
'''predicted_position = predict_race_result(
    driver='HAM',
    car='Ferrari: SF-25 - 2025',
    circuit='Baku City Circuit- Baku- AZERBAIJAN',
    weather_dry=True
)
predicted_position = int(predicted_position)
print(f"Predicted finishing position: P{predicted_position}")'''


joblib.dump(gb_model, "f1_gb_main_model.pkl")
print("Model saved as f1_gb_main_model.pkl")

'''
After tremendous effort, I finally chose to go with Gradient Boosting from rigorous evaluation.
A gradient boosting model is a machine learning technique that combines multiple weak decision trees into a single, 
strong predictive model to improve accuracy for regression and classification tasks. 

It works by building trees sequentially, with each new tree learning from the "mistakes" or residuals (errors) of 
the previous ones. The "gradient" refers to the algorithm's use of gradient descent to minimize the loss function, 
effectively correcting errors and guiding the model toward better predictions.

This is reasonable for a PoC, given the unpredictability of F1 racing :)
'''