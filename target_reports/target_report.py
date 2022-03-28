import json


def TargetReportData(data):
    if data.get("category").lower() == "electronics":
        report = json.load(open("target_reports/reports/electronics.json", 'r'))
        return report[data.get("product").lower()][data.get("cost").lower()]

    if data.get("category").lower() == "automobile":
        report = json.load(open("target_reports/reports/automobile.json", 'r'))
        return report[data.get("product").lower()][data.get("cost").lower()]

    if data.get("category").lower() == "beauty":
        report = json.load(open("target_reports/reports/beauty.json", 'r'))
        return report[data.get("product").lower()][data.get("cost").lower()]

    if data.get("category").lower() == "fashion":
        report = json.load(open("target_reports/reports/fashion.json", 'r'))
        return report[data.get("product").lower()][data.get("cost").lower()]

    if data.get("category").lower() == "jewellery":
        report = json.load(open("target_reports/reports/jewelry.json", 'r'))
        return report[data.get("product").lower()][data.get("cost").lower()]
