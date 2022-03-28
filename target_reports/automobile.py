from predictions.automobile import AutomobilePredicter
import pickle
from joblib import load

print("Models are getting initiated: Automobile")
vehicle_model_scaler = load("models/automobile_model/vehicle_model/scaler.pkl")
vehicle_model = pickle.load(
    open("models/automobile_model/vehicle_model/model.sav", "rb")
)

bike_model_scaler = load("models/automobile_model/bike_model/scaler_bike.pkl")
bike_model = pickle.load(
    open("models/automobile_model/bike_model/model_bike.sav", "rb")
)
print("Models are loaded succesfully : Automobile")


class TargetReportAutomobile:
    def __init__(self):
        pass

    def carPremium(self):
        results = {}
        probas = []
        for age in [15, 20, 25, 30, 35, 40, 45]:
            for income in [10, 15, 30, 50, 70, 150]:
                for gender in [0, 1]:
                    print("here")
                    scaled_data = vehicle_model_scaler.transform(
                        [[gender, age, income]]
                    )

                    prediction = {}
                    prediction["binary"] = str(vehicle_model.predict(scaled_data)[0])
                    prediction["probability"] = str(
                        int(max(vehicle_model.predict_proba(scaled_data)[0]) * 100)
                    )

                    if prediction["binary"] == "1":
                        results[prediction["probability"]] = [gender, age, income]
                    print(results, prediction["probability"])
                    probas.append(vehicle_model.predict_proba(scaled_data)[0])

        print(probas)
        print(results)
        print(results[max(results.keys())])
        return prediction

    def getCarMidRange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = vehicle_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(vehicle_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(vehicle_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    # Bike
    def getBikePremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = bike_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(bike_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(bike_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    def getBikeMidRange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = bike_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(bike_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(bike_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction


print(TargetReportAutomobile().carPremium())
