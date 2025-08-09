from flask import Flask, jsonify
import random, os

app = Flask(__name__)

@app.route('/random', methods=['GET'])
def get_random_number():
    return jsonify({'random_number': random.randint(1, 100)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
