import pandas as pd
import numpy as np

np.random.seed(42)
n_samples = 1000
data = {
    "customerID": range(1, n_samples + 1),
    "tenure": np.random.randint(1, 72, n_samples),
    "MonthlyCharges": np.random.uniform(20, 120, n_samples),
    "Contract": np.random.choice(["Month-to-month", "One year", "Two year"], n_samples),
    "Churn": np.random.choice(["Yes", "No"], n_samples, p=[0.3, 0.7])
}
df = pd.DataFrame(data)
df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})
df.to_csv("../files/train.csv", index=False)
