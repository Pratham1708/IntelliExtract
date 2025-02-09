from flask import Flask, render_template, request
import spacy
import pandas as pd
import os

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

if not os.path.exists("static"):
    os.makedirs("static")

@app.route("/", methods=["GET", "POST"])
def index():
    extracted_entities = []
    csv_path = None

    if request.method == "POST":
        text = request.form.get("text", "").strip()
        if text:
            doc = nlp(text)
            extracted_entities = [
                {"Entity": ent.text, "Label": ent.label_, "Explanation": spacy.explain(ent.label_)}
                for ent in doc.ents
            ]
            
            if extracted_entities:
                df = pd.DataFrame(extracted_entities)
                csv_path = "static/entities.csv"
                df.to_csv(csv_path, index=False)

    return render_template("index.html", entities=extracted_entities, csv_path=csv_path)

if __name__ == "__main__":
    app.run(debug=True)
    