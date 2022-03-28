from numpy import product
from target_reports.automobile import TargetReportAutomobile
from utilities.reachCalculation import Reach
from utilities.electronics import electronics_utilities
from utilities.automobile import automobile_utilities
from utilities.beauty import beauty_utilities
from utilities.fashion import fashion_utilities
from utilities.jewelry import jewelry_utilities
from target_reports.target_report import TargetReportData


def TweakPadResultData(data):
    if data.get("category").lower() == "electronics":
        return electronics_utilities(data)

    if data.get("category").lower() == "automobile":
        return automobile_utilities(data)

    if data.get("category").lower() == "beauty":
        return beauty_utilities(data)

    if data.get("category").lower() == "fashion":
        return fashion_utilities(data)

    if data.get("category").lower() == "jewellery":
        return jewelry_utilities(data)


def InvestmentResultData(data):
    def processInvestmentResultData(data, calculatedData, actualReach):
        for key in calculatedData.keys():
            data[key] = calculatedData[key]
        for key in actualReach.keys():
            data[key] = actualReach[key]
        return data

    reach = Reach(
        fb=data.get("fb"),
        yt=data.get("yt"),
        insta=data.get("insta"),
        google=data.get("google"),
    )
    calculatedData = reach.amount_calculation()

    actualReach = reach.actual_reach()

    return processInvestmentResultData(data, calculatedData, actualReach)


def ProfitCalculation(data):
    impression = int(data.get("impression"))
    CTR = int(data.get("CTR"))
    conversion_rate = int(data.get("conversionRate"))
    product_price = int(data.get("productPrice"))
    product_margin = int(data.get("productMargin"))

    earnings = (
        impression * CTR * conversion_rate * product_price * product_margin
    ) // (10**6)
    marketing_expense = int(data.get("marketingExpense"))

    return "Success" if earnings >= marketing_expense else "Failure"


def TargetReportCalculation(data):
    return TargetReportData(data)
