from django.db import models
from django.contrib.auth import get_user_model
from apis.models import *
from django.conf import settings
from taggit.managers import TaggableManager  # 👈 for taggit
from taggit.models import (
    TagBase,
    TaggedItemBase
)


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    # CLOSED_DAYS_CHOICES = (
    #     ('Monday', 'Monday'),
    #     ('Tuesday', 'Tuesday'),
    #     ('Wednesday', 'Wednesday'),
    #     ('Thursday', 'Thursday'),
    #     ('Friday', 'Friday'),
    #     ('Saturday', 'Saturday'),
    #     ('Sunday', 'Sunday'),
    # )
    closed_days = models.CharField(max_length=255, blank=True)
    contact = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return '(%s) %s' % (self.pk, self.name)


"""
gallery ={
 ('DDP(동대문 디지털 플라자)', '02-337-2555'),
 ('GS칼텍스 예울마루', '061 - 808 - 7080'),
 ('JCC재능문화센터', '02-2138-7373 / 02-3670-0383'),
 ('KCDF갤러리', '02-732-9382'),
 ('KF갤러리', '02-2151-6520'),
 ('KT&G 상상마당 갤러리', '02-330-6223'),
 ('KT&G 상상마당 갤러리(2F)', '02-330-6223'),
 ('갤러리175', '02-746-9670'),
 ('거제문화예술회관', '055-680-1009'),
 ('경기도미술관', '031-481-7000'),
 ('경주예술의전당', '1588-4925'),
 ('경주예술의전당 대전시실(4F)', '1588-4925'),
 ('고양아람누리', '031-960-0180'),
 ('고양아람누리 아람미술관', '031-960-0180'),
 ('고양어울림누리 어울림미술관', '031-960-9730'),
 ('고은사진미술관', '051-746-0055'),
 ('광주문화예술회관 대극장', '062-613-8357'),
 ('광화랑', '02-399-1167'),
 ('구리아트홀', '031-550-8800~1'),
 ('국립무형유산원', '063-280-1474'),
 ('국립아시아문화전당', '1899-5566'),
 ('국립현대미술관(과천관)', '02-2188-6000'),
 ('국립현대미술관(덕수궁관)', '02-522-3342'),
 ('국립현대미술관(서울관)', '02-3701-9500'),
 ('그레뱅 뮤지엄', '02-777-4700'),
 ('금나래아트홀', '02-2124-8955'),
 ('김해문화의전당', '055-320-1261'),
 ('꿈의숲 아트센터', '02-2289-5401'),
 ('나루아트센터', '02-2049-4700 / 010-2874-6881'),
 ('단원미술관', '031-481-0504'),
 ('대구 아양아트센터', '053-230-3312'),
 ('대구미술관', '053-790-3000'),
 ('대림미술관', '02-720-0667'),
 ('대전광역시이응노미술관', '042) 611-9821'),
 ('대전시립미술관', '(042)483-3763'),
 ('대학로극장', '02-3668-0007'),
 ('대한민국예술원 미술관', '02-3479-7211'),
 ('덕수궁 미술관', '02-724-6326'),
 ('동대문디자인플라자(DDP)', '02-2153-0000'),
 ('동대문역사문화공원', '02-2182-5533'),
 ('동탄아트스페이스', '031.8015.8266'),
 ('리각미술관', '041-565-3463 / 070-4111-3463'),
 ('마포아트센터', '02-705-7888'),
 ('마포아트센터 갤러리맥', '02-3274-8600'),
 ('무계원', '02-379-7131~2, 02-6203-1162'),
 ('문화역 서울 284', '1522-1178'),
 ('문화역서울 284 전관', '02-3407-3503'),
 ('문화역서울 284(구 서울역사)', '02-398-7951'),
 ('뮤지엄산', '033-730-9000'),
 ('미메시스 아트 뮤지엄', '031-955-4100, 4400'),
 ('백남준아트센터', '031-201-8500, 8571'),
 ('벡스코(제1전시장 3-A홀)', '1599-8879'),
 ('복합문화공간 NEMO', '070-7533-8998'),
 ('부산시립미술관', '051-747-9384'),
 ('부평아트센터', '032-500-2000'),
 ('북서울 꿈의숲 상상톡톡미술관', '2289-5401'),
 ('북서울 꿈의숲아트센터', '02-2289-5401'),
 ('블루메미술관(BMOCA)', '031-944-6324'),
 ('사비나미술관', '02-736-4371'),
 ('사비나미술관 전관', '02-736-4371'),
 ('서울미술관', '02-2124-8954'),
 ('서울시립미술관', '02)2151-6520'),
 ('서울시립미술관 남서울생활미술관', '02-598-6246'),
 ('서울시립미술관 북서울미술관', '02-2124-5269'),
 ('서울시립미술관 서소문본관', '02-2124-8942'),
 ('서울시민청', 'null'),
 ('서울애니메이션센터', '02-3455-8346'),
 ('서울혁신파크', '070-8656-3303'),
 ('서울혁신파크 5동 (서울특별시 은평구 통일로 684)', 'null'),
 ('성곡미술관', '02-737-7650'),
 ('성남아트센터', '031-783-8142 / 02-722-4414'),
 ('세종문화회관', '02-722-2267'),
 ('세종문화회관 미술관', '02-399-1000'),
 ('세종문화회관 미술관 본관, 세종문화회관 전시관', '02-723-9486, 9487'),
 ('세종이야기.충무공이야기 전시장', '02-399-1177~8'),
 ('소마미술관', '1588-2618'),
 ('수성아트피아', '053-668-1566, 1585'),
 ('수원시미술전시관', '031-211-0343'),
 ('아르코미술관', '02-760-4850~3'),
 ('아르코예술극장', '02-3668-0007'),
 ('아미미술관', '041-353-1555'),
 ('아트선재센터', '02-739-7067-8'),
 ('아트스페이스 휴', '031-955-1595'),
 ('아트허브 온라인 갤러리(ARTHUB Online Gallery)', '02-2654-7138'),
 ('아하갤러리', '070-4135-0826'),
 ('알파갤러리', '02-3788-9468'),
 ('어반플루토', 'null'),
 ('예술의전당', '02-747-0727'),
 ('예술의전당 V-갤러리', '02-720-9785'),
 ('올림푸스홀', '1544-3200'),
 ('용산아이파크몰', '1688-6875'),
 ('용산전쟁기념관', '1661-0553'),
 ('용산전쟁기념관 기획전시실', '1661-0207'),
 ('용인포은아트홀', '031-260-3360'),
 ('울산광역시문화예술회관', '052-226-8251~3'),
 ('울산현대예술관', 'null'),
 ('의정부예술의전당', '031)828-5826'),
 ('이브 갤러리', '02-540-5695'),
 ('이응노미술관', '042-611-9821'),
 ('인사동 KCDF Gallery', '02-398-7957'),
 ('인천종합문화예술회관', '010-3339-0684'),
 ('전시실 1, 2', '031-5170-3700'),
 ('전쟁기념관', '02-523-9095'),
 ('전쟁기념관 2층 기획전시실', '02-709-3139'),
 ('제주도립미술관', '064-710-4300'),
 ('천안예술의전당', '1566-0155'),
 ('청와대 사랑채', '02-739-4684'),
 ('청주시한국공예관', '043-268-0255 학예사무실'),
 ('춘천문화예술회관', '033-262-1361'),
 ('충무아트센터 갤러리', '02-2230-6638'),
 ('평촌아트홀', '031-687-0500'),
 ('포스코미술관', '02-3457-1665'),
 ('하남문화예술회관', '031-790-7979'),
 ('한가람디자인미술관', '02-3408-3665'),
 ('한가람미술관', '02-723-6577'),
 ('한국국제교류재단 문화센터', '02)2151-6516'),
 ('한국예술종합학교', '02-720-9282'),
 ('함평군립미술관', '061-320-2276'),
 ('헬로우뮤지움 어린이미술관', '02-562-4420'),
 ('현대어린이책미술관', '031-5170-3700'),
 ('횡성 웰리힐리파크', '070-8276-8922')}
from posts.forms import *
for name, contact in gallery:
    data = {'name':name, 'contact':contact}
    form = GalleryForm(data=data)
    if form.is_valid():
        form.save()
    else:
        print(" messege :", form.is_bound, form.errors)
"""


class Artist(models.Model):
    name_ko = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    # COUNTRIES = [
    #     ('KOR', 'South Korea'),
    #     ('USA', 'United States'),
    #     ('JPN', 'Japan'),
    #     ('CHN', 'China'),
    #     # Add more countries as needed
    # ]
    # nationality = models.CharField(max_length=3, choices=COUNTRIES)

    def __str__(self):
        return '%s  %s' % (self.name_ko, self.name_en)


class Exhibition(models.Model):
    REQUIRED_FIELDS = ['title', 'period', 'time', 'charge',
                       'grade']  # 'thumbnail'

    title = models.CharField(max_length=100)
    period = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    time = models.CharField(max_length=100, blank=True)
    charge = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=100, blank=True)

    thumbnail = models.ImageField(upload_to='posts/thumbnails/', blank=True)
    item = models.ForeignKey(
        Item, on_delete=models.SET_DEFAULT, default=1)

    artists = models.ManyToManyField(
        Artist, related_name="exhibitions", blank=True)
    gallery = models.ForeignKey(
        Gallery, on_delete=models.SET_DEFAULT, default=1)

    tags = TaggableManager()

    def __str__(self):
        return '(%s) %s' % (self.pk, self.title)


"""
from posts.forms import *
for item in Item.objects.all():
    data = {
        'title': item.title[:100],
        'period': item.period[:100],
        'description': item.description,
        'time': item.time[:100],
        'charge': item.charge[:100],
        'grade': item.grade[:100],
        'thumbnail': item.thumbnail,
        'item': item,
        'gallery': Gallery.objects.get(name=item.venue[1:].strip()),
        'tags': item.title + item.description + item.venue[1:].strip(),
    }
    form = ExhibitionForm(data=data)
    if form.is_valid():
        post = form.save()
        img_path = item.thumbnail
        post.thumbnail = img_path
        post.save()
    else:
        print("message : ", form.is_bound, form.errors)

for post in Exhibition.objects.all():
    img_path = post.item.thumbnail
    post.thumbnail = img_path
    post.save()
"""


class Review(models.Model):
    exhibition = models.ForeignKey(
        Exhibition, on_delete=models.SET_DEFAULT, default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_DEFAULT, default=1)
    content = models.CharField(max_length=255)


class Theme(models.Model):

    title = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='themes/thumbnails/', blank=True)
    exhibitions = models.ManyToManyField(
        Exhibition, related_name='themes', blank=True)

    # on_delete=models.SET_NULL, null=Tru


"""
from posts.forms import *
import random
c = Exhibition.objects.all().count()
for _ in range(20):
    n = random.randint(0, 21)

    for i in range(n):
        posts
    data = { 'title':"테마 제목", 'description':"테마 설명", "exhibitions":None}
    form = ThemeForm(data=data)
"""
