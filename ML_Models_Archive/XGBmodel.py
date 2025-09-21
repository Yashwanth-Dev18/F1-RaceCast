import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, make_scorer
import xgboost as xgb
import joblib

# 1. Load dataset
df = pd.read_csv("f1records.csv")

X = df.drop("race_results", axis=1).values
y = df["race_results"].values

# 2. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, shuffle=True
)

# 3. Define model with regularization
model = xgb.XGBRegressor(
    objective='reg:squarederror',
    n_estimators=700,
    learning_rate=0.1,
    max_depth=3,
    subsample=0.8,
    colsample_bytree=0.8,
    reg_alpha=3.0,
    reg_lambda=4.0,
    random_state=42
)

# 4. Cross-validation setup
kf = KFold(n_splits=5, shuffle=True, random_state=42)
mse_scorer = make_scorer(mean_squared_error, greater_is_better=False)
mae_scorer = make_scorer(mean_absolute_error, greater_is_better=False)

# CV scores
cv_mse_scores = cross_val_score(model, X_train, y_train, scoring=mse_scorer, cv=kf, n_jobs=-1)
cv_mae_scores = cross_val_score(model, X_train, y_train, scoring=mae_scorer, cv=kf, n_jobs=-1)

# 5. Retrain on full training data
model.fit(X_train, y_train)

# 6. Evaluate Train/Test
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

train_mse = mean_squared_error(y_train, y_pred_train)
train_mae = mean_absolute_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)
test_mae = mean_absolute_error(y_test, y_pred_test)

# 7. Summary Table
results = pd.DataFrame({
    "Metric": ["MSE", "MAE"],
    "CV Mean": [-np.mean(cv_mse_scores), -np.mean(cv_mae_scores)],
    "Train": [train_mse, train_mae],
    "Test": [test_mse, test_mae]
})

print(results.to_string(index=False))

# Save trained model
joblib.dump(model, "f1_xgb_model.pkl")
print("Model saved as f1_xgb_model.pkl")

