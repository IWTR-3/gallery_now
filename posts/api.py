# posts/api.py

import requests # 👉️ Requests module
from bs4 import BeautifulSoup # 👉️ BeautifulSoup module
from .models import Exhibition

# 문화기관 통합 전시정보
url = "http://api.kcisa.kr/openapi/service/rest/convergence/conver6"
serviceKey = "7a1ac8ea-5c3b-4e44-b978-60596f3b002d"

def update():
    count = len(Exhibition.objects.all())
    print("update exhibition list")

    url = 'http://api.kcisa.kr/openapi/service/rest/convergence/conver6'
    serviceKey = "7a1ac8ea-5c3b-4e44-b978-60596f3b002d"

    params ={'serviceKey' : serviceKey}
    response = requests.get(url, params=params)
    xml = response.text
    soup = BeautifulSoup(xml, 'html.parser')
    for item in soup.find_all('item'):
        
        title = item.find('title').text
        time = item.find('time').text
        # referenceIdentifier = item.find('referenceIdentifier').text
        venue = item.find('venue').text
        charge = item.find('charge').text
        period = item.find('period').text
        grade = item.find('grade').text
        uci = item.find('uci').text


        new_item = Exhibition.objects.create(title=title, period=period, time=time, charge=charge, venue=venue, grade=grade, uci=uci)
        print(new_item)
    print(count, len(Exhibition.objects.all()))
    if count < len(Exhibition.objects.all()):
        return True
    else:
        return False


