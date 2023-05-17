# posts/api.py

import requests  # 👉️ Requests module
from bs4 import BeautifulSoup  # 👉️ BeautifulSoup module
from .models import Exhibition
from .forms import ExhibitionForm
import json
import urllib


def update():
    count = 0
    print(" message : start update")

    name = "문화기관통합전시정보"
    url = 'http://api.kcisa.kr/openapi/service/rest/convergence/conver6'
    serviceKey = "e8696365-85f8-49b4-b7a2-ed1fce3b590f"

    numOfRows = 30
    pageNo = 1

    while pageNo < 4:
        """
        api 에서 xml 가져오기
        """
        print(" message : update page", pageNo)

        params = {'serviceKey': serviceKey, 'numOfRows': str(
            numOfRows), 'pageNo': str(pageNo), }

        response = requests.get(url, params=params)
        xml = response.text

        savePath = f'./page_{pageNo}.xml'
        f = open(savePath, "w")
        f.write(xml)

        """
        저장해 둔 xml 파일 사용
        """
        # savePath = f'./page_{pageNo}.xml'
        # f = open(savePath, "r")
        # xml = f.read()

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
    # FIELDS = ['title', 'period', 'time', 'charge', 'grade', ]

    for field in field_list:
        Tag = item.find(field)

        if Tag:
            data[field] = Tag.text[:100]  # data['title'] = "쿤스트라움 창작미술"
        else:
            data[field] = "Unknown"

    Tag = item.find('referenceidentifier')
    if Tag:
        imgUrl = Tag.text  # imgUrl = "http://www.artgy.or.kr/upload/tbl_show/2014koons_bn01.gif"
    else:
        imgUrl = None
        print(" message : imgUrl not found")

    data['tags'] = data['title']

    form = ExhibitionForm(data=data)

    if form.is_valid():

        print(" message : success")

        post = form.save()
        if imgUrl:

            format = imgUrl.split('.')[-1]

            savePath = f'./media/posts/thumbnails/{post.pk}.{format}'
            img_path = f'posts/thumbnails/{post.pk}.{format}'

            urllib.request.urlretrieve(imgUrl, savePath)

            # urlretrieve(이미지 파일 경로:url, 이미지를 저장할 경로)

            post.thumbnail = img_path
            post.save()

        return 1
    else:
        print(" message :", form.is_bound, form.errors)
        return 0


# test in the shell
"""
from posts import api
api.update()

posts = Exhibition.objects.all()
for post in posts:
    imgPath = f'posts/thumbnails/{post.pk}.jpg'
    post.thumbnail = imgPath
    post.save()

posts = Exhibition.objects.all()
for post in posts:
    post.delete()
from posts import api
api.update()
"""
