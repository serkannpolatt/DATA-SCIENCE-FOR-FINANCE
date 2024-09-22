from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict(np.array(data["features"]).reshape(1, -1))
    return jsonify({"prediction": int(prediction[0])})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
