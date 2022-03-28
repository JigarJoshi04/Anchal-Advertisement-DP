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

print("Models are loaded succesfully: Jewelry")


class JewelryPredicter:
    def __init__(self, data):
        self.data = data

    def proper_data(self):
        if type(self.data) != dict:
            return False

        if set(self.data.keys()).issubset(
            set(["age", "gender", "income", "education"])
        ):
            return False

        self.data["gender"] = 1 if self.data["gender"] == "Male" else 0
        self.data["education"] = 1 if self.data["education"] == "Educated" else 0
        return True

    # Bracelet
    def getBraceletPremium(self):
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
