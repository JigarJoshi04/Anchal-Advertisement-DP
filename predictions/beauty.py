import pickle
from joblib import load
import numpy as np

print("Models are getting initiated: Beauty")
bodycare_model_scaler = load("models/beauty_model/bodycare_model/bodycare.pkl")
bodycare_model = pickle.load(
    open("models/beauty_model/bodycare_model/bodycare.sav", "rb")
)

haircare_model_scaler = load("models/beauty_model/haircare_model/haircare.pkl")
haircare_model = pickle.load(
    open("models/beauty_model/haircare_model/haircare.sav", "rb")
)

makeup_model_scaler = load("models/beauty_model/makeup_model/makeup.pkl")
makeup_model = pickle.load(open("models/beauty_model/makeup_model/makeup.sav", "rb"))
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

        scaled_data = makeup_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                ]
            ).reshape(1, -1)
        )

        prediction = {}
        prediction["binary"] = str(makeup_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            int(max(makeup_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getMakeupMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = makeup_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                ]
            ).reshape(1, -1)
        )

        prediction = {}
        prediction["binary"] = str(makeup_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            int(max(makeup_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getHaircarePremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = haircare_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                ]
            ).reshape(1, -1)
        )

        prediction = {}
        prediction["binary"] = str(haircare_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            int(max(haircare_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getHaircareMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = haircare_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                ]
            ).reshape(1, -1)
        )

        prediction = {}
        prediction["binary"] = str(haircare_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            int(max(haircare_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getBodycarePremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = bodycare_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                ]
            ).reshape(1, -1)
        )

        prediction = {}
        prediction["binary"] = str(bodycare_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            int(max(bodycare_model.predict_proba(scaled_data)[0]))
        )
        return prediction

    def getBodycareMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = bodycare_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                ]
            ).reshape(1, -1)
        )

        prediction = {}
        prediction["binary"] = str(bodycare_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            int(max(bodycare_model.predict_proba(scaled_data)[0]))
        )
        return prediction
