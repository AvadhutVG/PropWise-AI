from flask import jsonify, request

from src.prediction.utils import get_available_locations
from src.prediction.predictor import predict_price
from flask import jsonify, request, render_template

def register_routes(app):

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/locations")
    def locations():
        return jsonify(get_available_locations())

    @app.route("/predict", methods=["POST"])
    def predict():

        data = request.get_json()

        predicted_price = predict_price(
            location=data["location"],
            total_sqft=float(data["total_sqft"]),
            bath=int(data["bath"]),
            balcony=int(data["balcony"]),
            bhk=int(data["bhk"]),
        )

        return jsonify({
            "predicted_price": predicted_price
        })