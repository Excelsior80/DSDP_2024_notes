from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to the Iris Type Predictor API</h1>
    <p>This API has the following endpoint:</p>
    <ul>
        <li>/iris: Takes a set of four measurements (sepal length, sepal width, petal length, petal width) and returns the predicted iris type.</li>
    </ul>
    """

@app.route('/iris', methods=['POST'])
def iris():
    data = request.get_json()
    sepal_length = data.get('sepal_length')
    sepal_width = data.get('sepal_width')
    petal_length = data.get('petal_length')
    petal_width = data.get('petal_width')

    # Here you can add your model prediction code
    # For now,  it always returns 'Iris-setosa'
    iris_type = 'Iris-setosa'
    probability = 0

    return jsonify({'iris_type': iris_type, 'confidence': probability})


app.run()

