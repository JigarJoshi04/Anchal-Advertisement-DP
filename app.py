import imp
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
from target_reports.automobile import TargetReportAutomobile
from target_reports.jewelry import TargetReportJewelry
from fetchData import connection

from utilities.utils import (
    TweakPadResultData,
    InvestmentResultData,
    ProfitCalculation,
    TargetReportCalculation,
)

model_premium_phone = None
app = Flask(__name__)
CORS(app)


@app.route("/user_behavior")
def index():
    return "Hello world!"


@app.route("/domain-selection", methods=["GET", "POST"])
def domainSelection():
    data = request.get_json()
    print(data)
    return "Success!"


@app.route("/tweak-pad", methods=["GET", "POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def tweakPad():
    data = request.get_json()
    data["income"] *= 2000
    prediction = TweakPadResultData(data)
    data.update(prediction)
    try:
        data["binary"] = "Yes" if data["binary"] == "1" else "No"
        data["gender"] = "Male" if data["gender"] == 1 else "Female"
        data["education"] = "Educated" if data["education"] == 1 else "Uneducated"
    except Exception as e:
        print("Exception occurred :  ", e)

    return jsonify(data)


# profit-calculator
@app.route("/profit-calculator", methods=["GET", "POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def profit_calculator():
    data = request.get_json()
    print(data)
    data["profitability"] = ProfitCalculation(data)

    return jsonify(data)

# fetch dashboard data
@app.route("/fetch-data", methods=["GET", "POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def fetch_data():
    data = request.get_json()
    print('data',data)
    productName = data['product'].lower()
    quality = 1 if data["cost"] == "Premium" else 0
    dictData = connection(productName, quality)
    print('json',dictData)
    return jsonify(dictData)

@app.route("/predict-investment", methods=["GET", "POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def predictInvestment():
    data = request.get_json()
    response = InvestmentResultData(data)
    return jsonify(response)


@app.route("/target-report", methods=["GET", "POST"])
@cross_origin(origin="*", headers=["Content-Type"])
def targetReport():
    data = request.get_json()
    target_report = TargetReportCalculation(data)
    data.update(target_report)
    return jsonify(data)


if __name__ == "__main__":
    app.debug = True
    app.run()  # go to http://localhost:5000/ to view the page
