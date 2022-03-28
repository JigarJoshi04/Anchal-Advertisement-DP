import pickle
from joblib import load

print("Models are getting initiated: Electronics")
phone_model_scaler = load("models/electronics_model/phone_model/std_scaler.bin")
phone_model = pickle.load(open("models/electronics_model/phone_model/model", "rb"))
print("Models are loaded succesfully : Electronics")


class ElectronicsPredicter:
    def __init__(self, data):
        self.data = data

    def proper_data(self):
        if type(self.data) != dict:
            return False

        if set(self.data.keys()).issubset(set(["age", "gender", "income"])):
            return False

        self.data["gender"] = 1 if self.data["gender"] == "Male" else 0
        return True

    # Mobile
    def getMobilePremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = phone_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(phone_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(phone_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    def getMobileMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = phone_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(phone_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(phone_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    # TV
    def getTvPremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = phone_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(phone_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(phone_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    def getTvMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = phone_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(phone_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(phone_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    # Headphone
    def getHeadphonePremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = phone_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(phone_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(phone_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    def getHeadphoneMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = phone_model_scaler.transform(
            [
                [
                    self.data.get("gender"),
                    self.data.get("age"),
                    self.data.get("income"),
                ]
            ]
        )

        prediction = {}
        prediction["binary"] = str(phone_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(phone_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction
