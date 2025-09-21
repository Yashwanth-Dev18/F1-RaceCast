import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import lightgbm as lgb
import matplotlib.pyplot as plt
import joblib

# ==================
# 1. Load dataset
# ==================
df = pd.read_csv("f1records.csv")  # replace with your CSV path

X = df.drop("race_results", axis=1).values
y = df["race_results"].values

# ======================
# 2. Train/test split
# ======================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# 3. Preparing LightGBM datasets
# ================================
train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test, reference=train_data)

# =========================
# 4. Setting parameters
# =========================
params = {
    'objective': 'regression',
    'metric': 'mae',        # optimize MAE directly
    'learning_rate': 0.1,
    'num_leaves': 31,
    'max_depth': 3,
    'feature_fraction': 0.8,
    'bagging_fraction': 0.8,
    'bagging_freq': 1,
    'lambda_l1': 5.0,
    'lambda_l2': 5.0,
    'verbose': -1,
    'seed': 42
}

# ==========================
# 5. Training LightGBM
# ==========================
gbm = lgb.train(
    params,
    train_data,
    num_boost_round=1000,
    valid_sets=[train_data, test_data],
    valid_names=['train', 'test'],
    callbacks=[lgb.early_stopping(stopping_rounds=50), lgb.log_evaluation(50)]
)

# ===================
# 6. Predictions
# ===================
y_pred_train = gbm.predict(X_train, num_iteration=gbm.best_iteration)
y_pred_test  = gbm.predict(X_test, num_iteration=gbm.best_iteration)

# ===================
# 7. Evaluation
# ===================
print("Train MSE:", mean_squared_error(y_train, y_pred_train))
print("Train MAE:", mean_absolute_error(y_train, y_pred_train))
print("Test MSE:", mean_squared_error(y_test, y_pred_test))
print("Test MAE:", mean_absolute_error(y_test, y_pred_test))


joblib.dump(gbm, "f1_lgbm_model.pkl")
print("Model saved as f1_lgbm_model.pkl")