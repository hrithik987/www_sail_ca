import requests

cookies = {
    'PHPSESSID': 'b0617bb7efaaf38cd5e76f3e9d4da2cc',
    '2c.cId': '68871fcc25fa5e3d7b179fc2',
    'ssUserId': 'b4f7472c-833d-4a7f-bf3f-75fe9cc80c1d',
    '_isuid': 'b4f7472c-833d-4a7f-bf3f-75fe9cc80c1d',
    'ssSessionIdNamespace': '14ec24f3-cc1b-42f1-9fb5-008746e5f92f',
    'OptanonAlertBoxClosed': '2025-07-28T06:59:30.029Z',
    'form_key': 'zxy52RAn6ujeGhO0',
    'mage-cache-storage': '{}',
    'mage-cache-storage-section-invalidation': '{}',
    'mage-cache-sessid': 'true',
    'PHPSESSID': 'b0617bb7efaaf38cd5e76f3e9d4da2cc',
    'absolunet_favorite_pos': '16',
    'absolunet-favorite-cache-timeout': '{%22updated_at%22:%221751636297%22%2C%22language%22:%22en%22}',
    'mage-messages': '',
    'gtm-session-start': 'undefined',
    '_gcl_au': '1.1.1455358967.1753685976',
    '_ga': 'GA1.1.970384176.1753685976',
    'recently_viewed_product': '{}',
    'recently_viewed_product_previous': '{}',
    'product_data_storage': '{}',
    '_fbp': 'fb.1.1753685978202.121323285180314985',
    'FPID': 'FPID2.2.fHWeFBXznKjvH8%2B2MF9anJYhXz%2FCnWil1zZHeC5phSo%3D.1753685976',
    'FPLC': 'revNpfjYkFnnVHSBL7OA8tNSv9o9ygv8o04ZnPp%2BlciXzb0831n2NpL6wa51iOtdW7fBvwcTdW42oHqOqQqNNoZJuN1vd3YgC3%2Fom6XCHQS1fdiuX1I6%2F0rFLiDKUg%3D%3D',
    'productsSku': '{}',
    '__pr.o9dakr': 'hVp9LbZhqS',
    'form_key': 'zxy52RAn6ujeGhO0',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Jul+28+2025+12%3A33%3A59+GMT%2B0530+(India+Standard+Time)&version=202308.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=770731d0-f97d-430a-b9a6-df738453fa78&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0007%3A1&geolocation=US%3BNJ&AwaitingReconsent=false',
    'ssShopperId': 'b4f7472c-833d-4a7f-bf3f-75fe9cc80c1d',
    'ssViewedProducts': '_23-03397',
    '_ga_6K4TC6H80X': 'GS2.1.s1753685976$o1$g1$t1753686241$j59$l0$h0',
    '_ga_CAPI': 'GS2.1.s1753686065$o1$g1$t1753686241$j60$l0$h1460276904',
    '_uetsid': '6ccb94306b8011f0a7ed3795465b9220',
    '_uetvid': '6ccc40206b8011f0884a6db41d0ec4bb',
    '_fpb': 'fb.1.1753685978202.121323285180314985',
    '_ga_LLHWP3ZL9G': 'GS2.1.s1753686069$o1$g0$t1753686242$j60$l0$h0',
    'savedSwatches': '{}',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36',
    # 'cookie': 'PHPSESSID=b0617bb7efaaf38cd5e76f3e9d4da2cc; 2c.cId=68871fcc25fa5e3d7b179fc2; ssUserId=b4f7472c-833d-4a7f-bf3f-75fe9cc80c1d; _isuid=b4f7472c-833d-4a7f-bf3f-75fe9cc80c1d; ssSessionIdNamespace=14ec24f3-cc1b-42f1-9fb5-008746e5f92f; OptanonAlertBoxClosed=2025-07-28T06:59:30.029Z; form_key=zxy52RAn6ujeGhO0; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; PHPSESSID=b0617bb7efaaf38cd5e76f3e9d4da2cc; absolunet_favorite_pos=16; absolunet-favorite-cache-timeout={%22updated_at%22:%221751636297%22%2C%22language%22:%22en%22}; mage-messages=; gtm-session-start=undefined; _gcl_au=1.1.1455358967.1753685976; _ga=GA1.1.970384176.1753685976; recently_viewed_product={}; recently_viewed_product_previous={}; product_data_storage={}; _fbp=fb.1.1753685978202.121323285180314985; FPID=FPID2.2.fHWeFBXznKjvH8%2B2MF9anJYhXz%2FCnWil1zZHeC5phSo%3D.1753685976; FPLC=revNpfjYkFnnVHSBL7OA8tNSv9o9ygv8o04ZnPp%2BlciXzb0831n2NpL6wa51iOtdW7fBvwcTdW42oHqOqQqNNoZJuN1vd3YgC3%2Fom6XCHQS1fdiuX1I6%2F0rFLiDKUg%3D%3D; productsSku={}; __pr.o9dakr=hVp9LbZhqS; form_key=zxy52RAn6ujeGhO0; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jul+28+2025+12%3A33%3A59+GMT%2B0530+(India+Standard+Time)&version=202308.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=770731d0-f97d-430a-b9a6-df738453fa78&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0007%3A1&geolocation=US%3BNJ&AwaitingReconsent=false; ssShopperId=b4f7472c-833d-4a7f-bf3f-75fe9cc80c1d; ssViewedProducts=_23-03397; _ga_6K4TC6H80X=GS2.1.s1753685976$o1$g1$t1753686241$j59$l0$h0; _ga_CAPI=GS2.1.s1753686065$o1$g1$t1753686241$j60$l0$h1460276904; _uetsid=6ccb94306b8011f0a7ed3795465b9220; _uetvid=6ccc40206b8011f0884a6db41d0ec4bb; _fpb=fb.1.1753685978202.121323285180314985; _ga_LLHWP3ZL9G=GS2.1.s1753686069$o1$g0$t1753686242$j60$l0$h0; savedSwatches={}',
}

import requests
from parsel import Selector


for itr in range(1, 10):

    response = requests.get(
        'https://www.sail.ca/en/canadianh-florent-hat-unisex-1276549',
        # cookies=cookies,
        headers=headers
    )

    sel = Selector(text=response.text)

    name = sel.xpath('//span[@data-ui-id="page-title-wrapper"]/text()').get('N/A')
    price = sel.xpath('//span[@class="price-final_price special-price"]//span[@class="price"]/text()').get('N/A')
    sku = sel.xpath('//td[@data-th="SKU"]/text()').get('N/A')
    print(name)
    print(price)
    print(sku)
    print(response.status_code)
    print('\n')






