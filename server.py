from flask import Flask, request, jsonify

# Initialize the Flask app
app = Flask(__name__)

# Define a route that accepts both GET and POST requests for testing
@app.route('/', methods=['GET', 'POST'])
def log_data():
    if request.method == 'POST':
        # Extract JSON data from the request
        data = request.json
        print(f"Received data: {data}")
        return jsonify({"status": "success"}), 200
    elif request.method == 'GET':
        return "This endpoint only accepts POST requests for data submission.", 200

# Run the server on the specified host and port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

