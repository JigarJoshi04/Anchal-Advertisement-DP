from predictions.automobile import AutomobilePredicter


def automobile_utilities(data):
    automobile_predictor = AutomobilePredicter(data)
    if data.get("product").lower() == "car":
        if data.get("cost").lower() == "premium":
            return automobile_predictor.getCarPremium()
        else:
            return automobile_predictor.getCarMidRange()

    if data.get("product").lower() == "bike":
        if data.get("cost").lower() == "premium":
            return automobile_predictor.getBikePremium()
        else:
            return automobile_predictor.getBikeMidRange()
