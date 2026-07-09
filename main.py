from src.prediction.predictor import predict_price


def main():

    price = predict_price(
        location="Whitefield",
        total_sqft=1500,
        bath=2,
        balcony=1,
        bhk=3,
    )

    print("\n========== PREDICTED PRICE ==========")
    print(f"Predicted Price : ₹ {price} Lakhs")


if __name__ == "__main__":
    main()