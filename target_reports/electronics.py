from predictions.electronics import ElectronicsPredicter


def electronics_utilities(data):
    electronics_predictor = ElectronicsPredicter(data)
    if data.get("product").lower() == "tv":
        if data.get("cost").lower() == "premium":
            return electronics_predictor.getTvPremium()
        else:
            return electronics_predictor.getTvMidrange()

    elif data.get("product").lower() == "mobile":
        if data.get("cost").lower() == "premium":
            return electronics_predictor.getMobilePremium()
        else:
            return electronics_predictor.getMobileMidrange()

    elif data.get("product").lower() == "headphone":
        if data.get("cost").lower() == "premium":
            return electronics_predictor.getHeadphonePremium()
        else:
            return electronics_predictor.getHeadphoneMidrange()
