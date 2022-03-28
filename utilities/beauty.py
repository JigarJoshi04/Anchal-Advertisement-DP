from predictions.beauty import BeautyPredicter


def beauty_utilities(data):
    beuaty_predictor = BeautyPredicter(data)
    if data.get("product").lower() == "makeup":
        if data.get("cost").lower() == "premium":
            return beuaty_predictor.getMakeupPremium()
        else:
            return beuaty_predictor.getMakeupMidrange()

    elif data.get("product").lower() == "haircare":
        if data.get("cost").lower() == "premium":
            return beuaty_predictor.getHaircarePremium()
        else:
            return beuaty_predictor.getHaircareMidrange()

    elif data.get("product").lower() == "bodycare":
        if data.get("cost").lower() == "premium":
            return beuaty_predictor.getBodycarePremium()
        else:
            return beuaty_predictor.getBodycareMidrange()
