import logging
from flask import Flask, request, jsonify
import pickle
import numpy as np

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | %(name)s | %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

try:
    with open('best_rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    logger.info("Model loaded successfully from best_rf_model.pkl.")
except Exception as e:
    logger.error(f"Failed to load the model: {e}")
    raise e

try:
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    logger.info("Scaler loaded successfully from scaler.pkl.")
except Exception as e:
    logger.error(f"Failed to load the scaler: {e}")
    raise e

@app.route('/')
def home():
    logger.info("Root endpoint '/' called.")
    return "House Price Prediction API - Up and Running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    logger.info(f"Received POST request data: {data}")

    try:
        bedrooms = data["bedrooms"]
        bathrooms = data["bathrooms"]
        sqft_living = data["sqft_living"]
        sqft_lot = data["sqft_lot"]
        sqft_above = data["sqft_above"]
        sqft_basement = data["sqft_basement"]

        input_features = np.array([[bedrooms, bathrooms, sqft_living,
                                    sqft_lot, sqft_above, sqft_basement]])
        
        logger.info(f"Input features (pre-scaling): {input_features.tolist()}")

        input_features_scaled = scaler.transform(input_features)
        logger.info(f"Input features (post-scaling): {input_features_scaled.tolist()}")

        prediction = model.predict(input_features_scaled)
        predicted_price = float(prediction[0])
        logger.info(f"Predicted price: {predicted_price}")

        return jsonify({"predicted_price": round(predicted_price, 2)})

    except KeyError as e:
        logger.error(f"Missing field in JSON: {e}")
        return jsonify({"error": f"Missing field in JSON: {e}"}), 400
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    logger.info("Starting Flask server on port 5000...")
    app.run(host="0.0.0.0", port=5000, debug=True)
