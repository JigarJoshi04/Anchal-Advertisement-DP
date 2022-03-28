from predictions.fashion import FashionPredicter


def fashion_utilities(data):
    fashion_predictor = FashionPredicter(data)
    if data.get("product").lower() == "womenswear":
        if data.get("cost").lower() == "premium":
            return fashion_predictor.getWomenswearPremium()
        else:
            return fashion_predictor.getWomenswearMidrange()

    elif data.get("product").lower() == "menswear":
        if data.get("cost").lower() == "premium":
            return fashion_predictor.getMenswearPremium()
        else:
            return fashion_predictor.getMenswearMidrange()

    elif data.get("product").lower() == "kidswear":
        if data.get("cost").lower() == "premium":
            return fashion_predictor.getKidswearPremium()
        else:
            return fashion_predictor.getKidswearMidrange()
