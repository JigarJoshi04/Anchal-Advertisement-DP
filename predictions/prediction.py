import random
from joblib import load
import pickle
from predictions.jewelry import JewelryPredicter

print("Models are getting initiated")
print(
    "######################################## Mobile Phone Models Loading ###################################################"
)
phone_model_scaler = load("models/electronics_model/phone_model/std_scaler.bin")
phone_model = pickle.load(open("models/electronics_model/phone_model/model", "rb"))
print(
    "######################################## Mobile Phone Models Loaded Successfully ###################################################"
)


print(
    "######################################## Vehicle Models Loading ###################################################"
)
vehicle_model_scaler = load("models/vehicle_model/scaler.pkl")
vehicle_model = pickle.load(open("models/vehicle_model/model.sav", "rb"))
print(
    "######################################## Vehicle Models Loaded Successfully ###################################################"
)


print(
    "######################################## Bike Models Loading ###################################################"
)
bike_model_scaler = load("models/bike_model/scaler_bike.pkl")
bike_model = pickle.load(open("models/bike_model/model_bike.sav", "rb"))
print(
    "######################################## Bike Models Loaded Successfully ###################################################"
)
print("Model are successfully loaded")


class Predict:
    def __init__(self, data):
        self.data = data
        j = JewelryPredicter()

    def proper_data(self):
        if type(self.data) != dict:
            return False

        if set(self.data.keys()).issubset(set(["age", "gender", "income"])):
            return False

        self.data["gender"] = 1 if self.data["gender"] == "Male" else 0
        return True

    # Electronics
    def getMobilePremium(self):
        if not self.proper_data():
            return 100.00

        return str(
            phone_model.predict(
                phone_model_scaler.transform(
                    [
                        [
                            self.data.get("gender"),
                            self.data.get("age"),
                            self.data.get("income"),
                        ]
                    ]
                )
            )[0]
        )

    def getMobileMidrange(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getTvPremium(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getTvMidrange(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getHeadphonePremium(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getHeadphoneMidrange(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    # Automobile
    def getCarPremium(self):
        if not self.proper_data():
            return 100.00

        return str(
            vehicle_model.predict(
                vehicle_model_scaler.transform(
                    [
                        [
                            self.data.get("gender"),
                            self.data.get("age"),
                            self.data.get("income"),
                        ]
                    ]
                )
            )[0]
        )

    def getCarMidRange(self):
        if not self.proper_data():
            return 100.00

        return str(
            vehicle_model.predict(
                vehicle_model_scaler.transform(
                    [
                        [
                            self.data.get("gender"),
                            self.data.get("age"),
                            self.data.get("income"),
                        ]
                    ]
                )
            )[0]
        )

    def getBikePremium(self):
        if not self.proper_data():
            return 100.00

        return str(
            bike_model.predict(
                bike_model_scaler.transform(
                    [
                        [
                            self.data.get("age"),
                            self.data.get("income"),
                            self.data.get("gender"),
                        ]
                    ]
                )
            )[0]
        )

    def getBikeMidRange(self):
        if not self.proper_data():
            return 100.00

        return str(
            bike_model.predict(
                bike_model_scaler.transform(
                    [
                        [
                            self.data.get("age"),
                            self.data.get("income"),
                            self.data.get("gender"),
                        ]
                    ]
                )
            )[0]
        )

    # Fashion
    

    # Makeup
    def getMakeupPremium(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getMakeupMidrange(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getHaircarePremium(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getHaircareMidrange(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getBodycarePremium(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )

    def getBodycareMidrange(self):
        if not self.proper_data():
            return 100.00

        return phone_model.predict(
            phone_model_scaler.transform(
                [
                    [
                        self.data.get("gender"),
                        self.data.get("age"),
                        self.data.get("income"),
                    ]
                ]
            )
        )
