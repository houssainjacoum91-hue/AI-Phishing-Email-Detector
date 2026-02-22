from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

html_template = """
<!doctype html>
<title>AI Phishing Detector</title>
<h2>AI Phishing Email Detector</h2>
<form method=post>
  <textarea name=email rows=6 cols=60 placeholder="Paste email content here..."></textarea><br><br>
  <input type=submit value=Detect>
</form>
{% if prediction %}
<h3>Result: {{ prediction }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        email = request.form["email"]
        data = vectorizer.transform([email])
        result = model.predict(data)[0]
        prediction = "⚠ Phishing Email" if result == 1 else "✅ Legitimate Email"
    return render_template_string(html_template, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
