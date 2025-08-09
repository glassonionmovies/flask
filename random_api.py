



from flask import Flask, jsonify
from flask_cors import CORS # Import the CORS library
import random, os

app = Flask(__name__)
CORS(app) # This will enable CORS for all routes

@app.route('/random', methods=['GET'])
def get_random_number():
    return jsonify({'random_number': random.randint(1, 100)})

@app.route('/srand', methods=['GET'])
def get_simple_random_number():
    return str(random.randint(100, 900))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
