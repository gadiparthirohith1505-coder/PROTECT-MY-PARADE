from flask import Flask, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS to allow the frontend to communicate with this backend
CORS(app)

def generate_deterministic_value(city, date):
    """
    Creates a deterministic "random" number from the city and date.
    This ensures that asking for the same city/date gives the same result.
    """
    combined_string = f"{city.lower()}{date}"
    hash_value = 0
    for char in combined_string:
        hash_value = (hash_value << 5) - hash_value + ord(char)
        hash_value &= 0xFFFFFFFF # Ensure the value stays within a 32-bit integer range
    
    # Return a consistent probability between 0 and 100
    return abs(hash_value) % 101

# Define the main API endpoint for weather prediction
@app.route('/weather', methods=['GET'])
def get_weather_prediction():
    # Get 'city' and 'date' from the request's query parameters
    city = request.args.get('city')
    date = request.args.get('date')

    if not city or not date:
        # Return an error if parameters are missing
        return jsonify({"error": "City and date parameters are required."}), 400

    # Generate a consistent probability based on the inputs
    probability = generate_deterministic_value(city, date)

    # Determine the weather condition based on the probability
    if probability > 75:
        condition = 'rainy'
        message = 'High chance of rain. You should definitely pack an umbrella!'
    elif probability > 40:
        condition = 'cloudy'
        message = 'It might be cloudy with a slight chance of showers.'
    else:
        condition = 'sunny'
        message = 'Looks like a clear day for your parade!'

    print(f"Prediction for {city} on {date}: {probability}% chance of rain. Condition: {condition}")

    # Create the response payload
    response_data = {
        "probability": probability,
        "condition": condition,
        "message": message
    }

    # Send the prediction back to the frontend as JSON
    return jsonify(response_data)

# Run the server when the script is executed
if __name__ == '__main__':
    # The server will run on port 3000 to match the frontend's configuration
    app.run(port=3000, debug=True)