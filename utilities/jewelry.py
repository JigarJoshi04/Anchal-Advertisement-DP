from predictions.jewelry import JewelryPredicter


def jewelry_utilities(data):
    jewelry_predictor = JewelryPredicter(data)
    if data.get("product").lower() == "bracelet":
        if data.get("cost").lower() == "premium":
            return jewelry_predictor.getBraceletPremium()
        else:
            return jewelry_predictor.getBraceletMidrange()

    if data.get("product").lower() == "earring":
        if data.get("cost").lower() == "premium":
            return jewelry_predictor.getEarringPremium()
        else:
            return jewelry_predictor.getEarringMidrange()

    if data.get("product").lower() == "menscollection":
        if data.get("cost").lower() == "premium":
            return jewelry_predictor.getMenscollectionPremium()
        else:
            return jewelry_predictor.getMenscollectionMidrange()

    if data.get("product").lower() == "necklace":
        if data.get("cost").lower() == "premium":
            return jewelry_predictor.getNecklacePremium()
        else:
            return jewelry_predictor.getNecklaceMidrange()

    if data.get("product").lower() == "ring":
        if data.get("cost").lower() == "premium":
            return jewelry_predictor.getRingPremium()
        else:
            return jewelry_predictor.getRingMidrange()
