import joblib
from sklearn.metrics import mean_absolute_error, r2_score
from preprocess import X, y
from sklearn.model_selection import train_test_split

model = joblib.load("model/gb_model.pkl")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

preds = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, preds))
print("R2 Score:", r2_score(y_test, preds))
