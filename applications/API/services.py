import os
import requests, json

def getBanxico(serie, startDate, endDate):
# URL de la API Banxico
    url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series/{}/datos/{}/{}'. format(serie, startDate, endDate)
    headers = {'Bmx-Token': '331baa59193fc3b4003416b1e92c7b529c06f62da6edbbf21ecd1479f110d9e1'}
    response = requests.get(url, headers=headers)
    
    response_data = json.loads(response.content)

    #response_data = response.json()
    
    return response_data
    """
    result = response_data["bmx"]
    return result
    """