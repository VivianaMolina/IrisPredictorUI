# Train and save a classification model
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load the data
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

target_names = load_iris().target_names  # Save this separately

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save both model and target names
joblib.dump((model, target_names), 'models/model_iris.pkl')