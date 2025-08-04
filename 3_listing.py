
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'origin': 'https://www.sail.ca',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.sail.ca/',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
}

params = {
    'ajaxCatalog': 'v3',
    'resultsFormat': 'native',
    'siteId': 's8zq1c',
    # 'siteId': '',
    # 'domain': 'https://www.sail.ca/en/men/accessories/hats',
    'bgfilter.category_hierarchy': 'Men>Accessories>Hats',
    'q': '',
    'page': 1,
    # 'userId': 'b4f7472c-833d-4a7f-bf3f-75fe9cc80c1d',
    'userId': '',
    # 'sessionId': '14ec24f3-cc1b-42f1-9fb5-008746e5f92f',
    'sessionId': '',
    # 'pageLoadId': 'b1146483-5efc-4e38-b8f7-66395d5da6e3',
    'pageLoadId': '',
}


import pydash as _
import requests



for itr in range(1, 1000):

    response = requests.get(
        'https://s8zq1c.a.searchspring.io/api/search/search.json',
        params=params,
        headers=headers
    )

    data = response.json()
    name = _.get(data, 'results[0].name', 'N/A')
    print(name)
    print(response.status_code)
    print('\n')

