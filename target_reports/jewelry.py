import pickle
from joblib import load
import numpy as np


print("Models are getting initiated : Jewelry")
bracelet_model_scaler = load("models/jewelry_model/bracelet_model/scaler_bracelet.pkl")
bracelet_model = pickle.load(
    open("models/jewelry_model/bracelet_model/model_bracelet.sav", "rb")
)

earring_model_scaler = load("models/jewelry_model/earring_model/scaler_earrings.pkl")
earring_model = pickle.load(
    open("models/jewelry_model/earring_model/model_earrings.sav", "rb")
)

menscollection_model_scaler = load(
    "models/jewelry_model/menscollection_model/scaler_menscollection.pkl"
)
menscollection_model = pickle.load(
    open("models/jewelry_model/menscollection_model/model_menscollection.sav", "rb")
)

necklace_model_scaler = load("models/jewelry_model/necklace_model/scaler_necklace.pkl")
necklace_model = pickle.load(
    open("models/jewelry_model/necklace_model/model_necklace.sav", "rb")
)

ring_model_scaler = load("models/jewelry_model/ring_model/scaler_ring.pkl")
ring_model = pickle.load(open("models/jewelry_model/ring_model/model_ring.sav", "rb"))

all_model_scaler = load("models/jewelry_model/scaler_jewelry.pkl")
all_model = load("models/jewelry_model/model_jewelry.sav")
print("Models are loaded succesfully: Jewelry")


class TargetReportJewelry:
    def __init__(self):
        pass

    # Bracelet
    def getBraceletPremium(self):
        results = {}
        for age in [28, 30, 40, 50, 65, 80]:
            for income in [10, 20, 30, 40, 50, 60, 70, 80, 90, 120]:
                for gender in [0, 1]:
                    for education in [0, 1]:
                        scaled_data = all_model_scaler.transform(
                            np.array([age, income, gender, education, 2, 1]).reshape(
                                1, -1
                            )
                        )

                        prediction = {}
                        prediction["binary"] = str(all_model.predict(scaled_data)[0])
                        prediction["probability"] = str(
                            round(
                                max(all_model.predict_proba(scaled_data)[0]) * 100,
                                2,
                            )
                        )

                        if prediction["binary"] == "1":
                            results[prediction["probability"]] = [
                                age,
                                income,
                                gender,
                                education,
                                2,
                                1,
                            ]
                        print(results, prediction["probability"])

        print(results[max(results.keys())], max(results.keys()))
        return prediction

        return prediction

    def getBraceletMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = bracelet_model_scaler.transform(
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
        prediction["binary"] = str(bracelet_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(bracelet_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    # Earring
    def getEarringPremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = earring_model_scaler.transform(
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
        prediction["binary"] = str(earring_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(earring_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    def getEarringMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = earring_model_scaler.transform(
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
        prediction["binary"] = str(earring_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(earring_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    # Menscollection
    def getMenscollectionPremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = menscollection_model_scaler.transform(
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
        prediction["binary"] = str(menscollection_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(menscollection_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    def getMenscollectionMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = menscollection_model_scaler.transform(
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
        prediction["binary"] = str(menscollection_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(menscollection_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    # Necklace
    def getNecklacePremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = necklace_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                    1,
                ]
            ).reshape(1, -1)
        )

        scaled_data = np.array(scaled_data).reshape(1, -1)
        prediction = {}
        prediction["binary"] = str(necklace_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(necklace_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    def getNecklaceMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = necklace_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                    0,
                ]
            ).reshape(1, -1)
        )
        scaled_data = np.array(scaled_data).reshape(1, -1)
        prediction = {}
        prediction["binary"] = str(necklace_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(necklace_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    # Ring
    def getRingPremium(self):
        if not self.proper_data():
            return 100.00

        scaled_data = ring_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                    1,
                ]
            ).reshape(1, -1)
        )

        prediction = {}
        prediction["binary"] = str(ring_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(ring_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction

    def getRingMidrange(self):
        if not self.proper_data():
            return 100.00

        scaled_data = ring_model_scaler.transform(
            np.array(
                [
                    self.data.get("age"),
                    self.data.get("income") // 1000,
                    self.data.get("gender"),
                    self.data.get("education"),
                    0,
                ]
            ).reshape(1, -1)
        )

        prediction = {}
        prediction["binary"] = str(ring_model.predict(scaled_data)[0])
        prediction["probability"] = str(
            round(max(ring_model.predict_proba(scaled_data)[0]) * 100, 2)
        )
        return prediction
