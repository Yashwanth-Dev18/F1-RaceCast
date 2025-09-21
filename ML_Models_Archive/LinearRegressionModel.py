import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Loading dataset
df = pd.read_csv("f1records.csv")  # replace with your file path
X = df[["VER","HAM"]]  # simplify to 2 features for contour visualization
y = df["race_results"].values

# Normalizing features (important for gradient descent)
X = (X - X.mean()) / X.std()

m = len(y)  # number of samples
X_b = np.c_[np.ones((m,1)), X.values]  # add bias term
n_features = X_b.shape[1]


# Initializing weights and bias
W = np.random.randn(n_features)  # W[0] = bias
learning_rate = 0.0001
n_iterations = 20000


# Gradient descent
cost_history = []

for i in range(n_iterations):
    y_pred = X_b.dot(W)
    error = y_pred - y
    cost = (1/m) * np.sum(error**2)
    cost_history.append(cost)
    
    # Gradients
    gradients = (2/m) * X_b.T.dot(error)
    
    # Update weights
    W = W - learning_rate * gradients

print("Trained weights:", W)
print("Final cost:", cost_history[-1])


plt.plot(cost_history)
plt.xlabel("Iteration")
plt.ylabel("MSE Cost")
plt.title("Gradient Descent Convergence")
plt.show()

# Contour plot
w0_range = np.linspace(W[0]-10, W[0]+10, 50)
w1_range = np.linspace(W[1]-2, W[1]+2, 50)
W0, W1 = np.meshgrid(w0_range, w1_range)
J = np.zeros_like(W0)

for i in range(W0.shape[0]):
    for j in range(W0.shape[1]):
        w_temp = np.array([W0[i,j], W1[i,j], W[2]])
        J[i,j] = (1/m)*np.sum((X_b.dot(w_temp) - y)**2)

plt.contour(W0, W1, J, levels=50, cmap='viridis')
plt.xlabel("Bias w0")
plt.ylabel("Weight w1 (VER)")
plt.title("Cost Function Contour Plot")
plt.show()
