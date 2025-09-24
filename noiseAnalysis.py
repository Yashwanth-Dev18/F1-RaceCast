import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import xgboost as xgb

# Load data
df = pd.read_csv("f1records.csv")

# Split features/target
X = df.drop("race_results", axis=1)
y = df["race_results"]

# ==============================
# Variance of each feature
feature_variance = X.var().sort_values()

plt.figure(figsize=(10,6))
feature_variance.head(20).plot(kind="barh")
plt.title("Lowest Variance Features (Possible Noise)")
plt.xlabel("Variance")
plt.show()

# ==============================
# Correlation with target
correlations = pd.concat([X, y], axis=1).corr()["race_results"].drop("race_results")

plt.figure(figsize=(10,6))
correlations.abs().sort_values().head(20).plot(kind="barh")
plt.title("Lowest Correlation Features with Race Result (Possible Noise)")
plt.xlabel("Absolute Correlation")
plt.show()

# ================================
# Feature importance from XGBoost
model = xgb.XGBRegressor(objective="reg:squarederror", n_estimators=200, max_depth=4)
model.fit(X, y)

xgb_importance = pd.Series(model.feature_importances_, index=X.columns).sort_values()

plt.figure(figsize=(10,6))
xgb_importance.head(20).plot(kind="barh")
plt.title("Lowest XGBoost Feature Importances (Noise)")
plt.xlabel("Importance Score")
plt.show()
