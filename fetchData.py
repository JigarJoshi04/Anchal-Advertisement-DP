import json
import pymongo
FILEPATH = 'config.json'


def genderData(mydb, productName, quality):
    collist = mydb.list_collection_names()
    print(collist)
    if productName in collist:
        # mycol = mydb[productName]
        print("The collection exists.")
        gender = mydb[productName].aggregate([
            { "$match": { "$and": [ { "quality": quality }, { "purchased": 1 } ] } },
            {"$group": {"_id": "$sex", "count":{"$sum": 1}}}
            ])
        genderList = []
        for i in gender:
            if i['_id'] == 0 :
                sex = 'Female'
            else:
                sex = 'Male'
            genderList.append((sex, i['count']))
        print('genderList',genderList)
        return genderList

def ageData(mydb, productName, quality):
    collist = mydb.list_collection_names()
    print(collist)
    if productName in collist:
        # mycol = mydb[productName]
        print("The collection exists.")
        age = mydb[productName].aggregate([
            { "$match":  { "$and": [ { "quality": quality }, { "purchased": 1 } ] } },
            {"$group": {"_id": {
                "$concat": [
                    { "$cond": [ { "$and": [ { "$gte": ["$age", 18] }, { "$lt": ["$age", 30] } ]}, "18 - 30", ""] },
                    { "$cond": [ { "$and": [ { "$gte": ["$age", 30] }, { "$lt": ["$age", 50] } ]}, "30 - 50", ""] },
                    { "$cond": [ { "$and": [ { "$gte": ["$age", 50] }, { "$lt": ["$age", 81] } ]}, "50 - 80", ""] },
                ]
              }  , "count":{"$sum": 1}}}
            ])
        ageList = []
        for i in age:
            ageList.append((i['_id'], i['count']))
        ageList.sort()
        print('ageList',ageList)
        return ageList

def incomeData(mydb, productName, quality, purchased):
    collist = mydb.list_collection_names()
    print(collist)
    if productName in collist:
        # mycol = mydb[productName]
        print("The collection exists.")
        income = mydb[productName].aggregate([
            { "$match": { "$and": [ { "quality": quality }, { "purchased": purchased } ] } },
            {"$group": {"_id": {
                "$concat": [
                    { "$cond": [ { "$and": [ { "$gte": ["$monthly_income", 10] }, { "$lt": ["$monthly_income", 20] } ]}, "10 - 20k", ""] },
                    { "$cond": [ { "$and": [ { "$gte": ["$monthly_income", 20] }, { "$lt": ["$monthly_income", 40] } ]}, "20 - 40k", ""] },
                    { "$cond": [ { "$and": [ { "$gte": ["$monthly_income", 40] }, { "$lt": ["$monthly_income", 60] } ]}, "40 - 60k", ""] },
                    { "$cond": [ { "$and": [ { "$gte": ["$monthly_income", 60] }, { "$lt": ["$monthly_income", 80] } ]}, "60 - 80k", ""] },
                    { "$cond": [ { "$and": [ { "$gte": ["$monthly_income", 80] }, { "$lt": ["$monthly_income", 100] } ]}, "80 - 100k", ""] },
                    { "$cond": [ { "$and": [ { "$gte": ["$monthly_income", 100] }, { "$lt": ["$monthly_income", 201] } ]}, "100 - 200k", ""] },
                ]
              }  , "count":{"$sum": 1}}}
            ])
        incomeList = []
        for i in income:
            incomeList.append((i['_id'], i['count']))
        incomeList.sort()
        print('incomeList',incomeList)
        return incomeList

def educationData(mydb, productName, quality):
    collist = mydb.list_collection_names()
    print(collist)
    if productName in collist:
        # mycol = mydb[productName]
        print("The collection exists.")
        education = mydb[productName].aggregate([
            { "$match": { "$and": [ { "quality": quality }, { "purchased": 1 } ] } },
            {"$group": {"_id": "$education", "count":{"$sum": 1}}}
            ])
        educationList = []
        for i in education:
            if i['_id'] == 0 :
                ed = 'Uneducated'
            else:
                ed = 'Educated'
            educationList.append((ed, i['count']))
        print('educationList',educationList)
        return educationList

def purchasedData(mydb, productName, quality):
    collist = mydb.list_collection_names()
    print(collist)
    if productName in collist:
        # mycol = mydb[productName]
        print("The collection exists.")
        purchased = mydb[productName].aggregate([
            { "$match":{ "quality": quality }},
            {"$group": {"_id": "$purchased", "count":{"$sum": 1}}}
            ])
        purchasedList = []
        for i in purchased:
            if i['_id'] == 0 :
                ed = 'Not Purchased'
            else:
                ed = 'Purchased'
            purchasedList.append((ed, i['count']))
        print('purchasedList',purchasedList)
        return purchasedList

def makeIncomeData(purchasedList, notPurchasedList, quality):
    purchasedList.sort()
    notPurchasedList.sort()
    purchasedData = []
    notPurchasedData = []
    labels = [] 
    for i in purchasedList:
        labels.append(i[0])
        purchasedData.append(i[1])
        
    for i in notPurchasedList:
        notPurchasedData.append(i[1])  

    if quality == 1:
         l = labels.pop(0)
         labels.append(l)
         p = purchasedData.pop(0)
         purchasedData.append(p)
         n = notPurchasedData.pop(0)
         notPurchasedData.append(n)
         
    listData = {
        "labels" : labels,
        "purchasedData": purchasedData,
        "notPurchasedData": notPurchasedData,
    }    
    return listData

def makeDict(arrayList):
    arrayList.sort()
    data = []
    labels = []
    for i in arrayList:
        labels.append(i[0])
        data.append(i[1])
        
    listData = {
        "labels" : labels,
        "data": data,
    }
    return listData

def connection(productName, quality):
    with open(FILEPATH) as f:
        data = json.load(f)
    connection = data['connection'][0]
    myclient = pymongo.MongoClient(connection['host'])

    mydb = myclient[connection['db']]
    
    genderList = genderData(mydb, productName, quality) 
    ageList = ageData(mydb, productName, quality) 
    purchasedIncomeList = incomeData(mydb, productName, quality, 1) 
    notPurchasedIncomeList = incomeData(mydb, productName, quality, 0) 
    educationList = educationData(mydb, productName, quality) 
    purchasedList = purchasedData(mydb, productName, quality) 
    dictData = {
        "product": productName,
        "cost": quality,
        "genderList": makeDict(genderList),
        "ageList": makeDict(ageList),
        "incomeList": makeIncomeData(purchasedIncomeList, notPurchasedIncomeList, quality),
        "educationList": makeDict(educationList),
        "purchasedList": makeDict(purchasedList),
    }
    print("Final Data",dictData)
    return dictData
    

# #driver code
# if __name__ == "__main__" :
#     connection('ring', 1)