
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(
    open('/Users/preetichauhan/Practice/PCOSPrediction/model.pkl', 'rb'))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    val = [list(data.values())]
    print(val)
    prediction = model.predict(val)
    print(prediction)

    output = prediction[0]

    print(output)

    dictarr = {"output": output}
    return jsonify(output=int(output))


if __name__ == "__main__":
    app.run(host="192.168.0.101", port=5000)
