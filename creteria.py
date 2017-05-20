import requests
import json

"""
Section: Search Criteria
"""

token = ""  # Your Token

# SIC Code, See https://www.sec.gov/info/edgar/siccodes.htm
sicList = [
    '3600', '3612', '3613', '3620', '3621', '3630', '3634', '3640', '3651', '3652', '3661', '3663', '3669', '3670', '3672', '3674', '3677', '3678', '3679', '3690', '3695'
]

url = "https://plus.dnb.com/v1/search/criteria"
data = {
    "usSicV4": sicList,
    "countryISOAlpha2Code": "TW",
    "isMarketable": True,
    "isOutOfBusiness": False,
    "numberOfEmployees": {
        # You can change here to define the range
        "maximumValue": 40,
        "minimumValue": 10
    },
    "pageNumber": 1,
    "pageSize": 20
}

headers = {
    "Authorization": "Bearer " + token
}

companys = []

while(1):
    data['pageNumber'] += 1
    res = requests.post(url, headers=headers, json=data).json()
    try:
        for company in res['searchCandidates']:
            companys.append(company['organization']['duns'])
    except:
        break

with open('duns.txt', 'w') as f:
    f.write('\n'.join(companys))
