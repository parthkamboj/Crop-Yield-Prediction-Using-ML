from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_country_names', methods=['GET'])
def get_country_names():
    response = jsonify({
        'countries': util.get_country_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_item_names', methods=['GET'])
def get_item_names():
    response = jsonify({
        'items': util.get_item_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response



@app.route('/predict_crop_yield', methods=['GET', 'POST'])
def estimate_crop_yield():
    avg_rainfall = float(request.form['avg_rainfall'])
    item = request.form['item']
    avg_temp = float(request.form['avg_temp'])
    country = request.form['country']
    pesticides_tonnes = float(request.form['pesticides_tonnes'])

    response = jsonify({
        'estimated_crop_yield': util.get_estimated_crop_yield(country,item,avg_rainfall,pesticides_tonnes,avg_temp)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Crop Yield Prediction...")
    util.load_saved_artifacts()
    app.run()

