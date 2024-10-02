from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the pickled model
try:
    with open('./tvs-credit-6-ml-model', 'rb') as model_file:
        model = pickle.load(model_file)
except FileNotFoundError:
    print("Model file not found. Ensure the path is correct.")
    model = None

# Define the /predict route
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded properly.'}), 500
    
    try:
        # Get the JSON data from the request
        data = request.json

        # Convert the data into a format the model can predict (assuming input is a list of features)
        features = np.array(data['features']).reshape(1, -1)

        # Get the prediction from the model
        prediction = model.predict_proba(features)[0][1]

        # Return the prediction as a JSON response
        return jsonify({'prediction': prediction.tolist()})
    
    except KeyError:
        return jsonify({'error': 'Invalid input format. Please provide features as a JSON object.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
