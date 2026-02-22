import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset
data = {
    "email": [
        "Congratulations! You won a free iPhone. Click here now!",
        "Your bank account has been suspended. Verify immediately.",
        "Meeting scheduled for tomorrow at 10 AM.",
        "Please find attached the project report."
    ],
    "label": [1, 1, 0, 0]  # 1 = Phishing, 0 = Legitimate
}

df = pd.DataFrame(data)

# Convert text to numerical features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["email"])
y = df["label"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer
pickle.dump(model, open("phishing_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")
