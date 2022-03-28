import pickle
from joblib import load

print("Models are getting initiated: Beauty")
phone_model_scaler = load("models/electronics_model/phone_model/std_scaler.bin")
phone_model = pickle.load(open("models/electronics_model/phone_model/model", "rb"))
print("Models are loaded succesfully : Beauty")


class BeautyPredicter:
    def __init__(self, data):
        self.data = data

    def proper_data(self):
        if type(self.data) != dict:
            return False

        if set(self.data.keys()).issubset(set(["age", "gender", "income"])):
            return False

        self.data["gender"] = 1 if self.data["gender"] == "Male" else 0
        return True

    def getMakeupPremium(self):
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
            int(max(phone_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getMakeupMidrange(self):
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
            int(max(phone_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getHaircarePremium(self):
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
            int(max(phone_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getHaircareMidrange(self):
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
            int(max(phone_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getBodycarePremium(self):
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
            int(max(phone_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getBodycareMidrange(self):
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
            int(max(phone_model.predict_proba(scaled_data)[0]))
        )
        return prediction
