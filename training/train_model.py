import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from pathlib import Path

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

model_path = Path(__file__).parent.parent / 'src' / 'iris_model.joblib'
model_path.parent.mkdir(parents=True, exist_ok=True)
joblib.dump(model, model_path)
