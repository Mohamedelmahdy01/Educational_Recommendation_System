import pickle
from sklearn.ensemble import RandomForestClassifier

X_sample = [
    [3, 4, 5, 2, 1, 4, 2, 4, 3, 5, 4, 3, 5, 4, 2, 3, 4, 5, 3, 4],
    [4, 3, 5, 4, 5, 2, 1, 4, 3, 5, 3, 2, 4, 4, 3, 2, 4, 3, 2, 5],
]
y_sample = [0, 1]  
model = RandomForestClassifier(random_state=42)
model.fit(X_sample, y_sample)

with open("random_forest_model.pkl", "wb") as file:
    pickle.dump(model, file)
