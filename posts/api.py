# posts/api.py

import requests  # 👉️ Requests module
from bs4 import BeautifulSoup  # 👉️ BeautifulSoup module
from .models import Exhibition
from .forms import ExhibitionForm
import json


def update():
    count = 0
    print(" message : start update")

    name = "문화기관통합전시정보"
    url = 'http://api.kcisa.kr/openapi/service/rest/convergence/conver6'
    serviceKey = "e8696365-85f8-49b4-b7a2-ed1fce3b590f"
    numOfRows = 30
    pageNo = 1

    while pageNo < 4:
        print(" message : update page", pageNo)
        params = {'serviceKey': serviceKey, 'numOfRows': str(
            numOfRows), 'pageNo': str(pageNo), }

        response = requests.get(url, params=params)
        xml = response.text
        soup = BeautifulSoup(xml, 'html.parser')

        for item in soup.find_all('item'):
            count += _create_object(item)

        pageNo += 1

    if count > 1:
        return str(f"message : {count} items created")
    else:
        return str(f"message : {count} item created")


def _create_object(item):

    data = {

    }

    field_list = Exhibition.FIELDS

    for field in field_list:
        Tag = item.find(field)
        if Tag:
            data[field] = Tag.text[:100]
        else:
            data[field] = "Unknown"

    form = ExhibitionForm(data=data)

    if form.is_valid():
        print(" message : 1")
        form.save()
        return 1
    else:
        print(" message :", form.is_bound, form.errors)
        return 0
