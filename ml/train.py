import pandas as pd, joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import MultiLabelBinarizer

df = pd.read_csv("ml/data/symptoms.csv")  # columns: symptoms (comma list), condition
X = df['symptoms'].str.split(',').apply(lambda xs: [s.strip().lower() for s in xs])
y = df['condition']

mlb = MultiLabelBinarizer()
X_bin = mlb.fit_transform(X)

Xtr, Xte, ytr, yte = train_test_split(X_bin, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=300, random_state=42).fit(Xtr, ytr)

print("Train score:", model.score(Xtr, ytr))
print("Test  score:", model.score(Xte, yte))

joblib.dump(model, "app/model_rf.joblib")
joblib.dump(mlb, "app/symptom_binarizer.joblib")
