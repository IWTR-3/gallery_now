# gallery_now

I want to rest !!

##

0. 장고 설치
   `pip install django==3.2.18`

1. 의존성 파일 생성

2. 프로젝트 생성
   `django-admin startproject [프로젝트명] .`( `.` 현재위치)

3. 앱 생성
   `python manage.py startapp articles`

4. .gitignore 생성

5. settings.py 작성

   - app 등록
   - extensions 추가
   - STATIC, MEDIA 세팅

6. 로컬 개발환경 및 smart 커밋 메세지 세팅 !

   - [] 김신혜
   - [] 이수정
   - [] 전성재
   - [] 최계수

## local 개발 환경 setting 튜토리얼

1. repository clone 및 가상환경 생성

```bash
# clone remote
git clone https://github.com/IWTR-3/gallery_now.git
cd gallery_now

# virtual env setting
python -m venv .venv
source .venv/bin/activate
pip  install -r requirements.txt

# add commit message template
git config --local commit.template .github/.gitmessage.txt
```

2. 개발 및 commit

```bash
# branch from develop
git checkout -b feature/{ 기능 또는 이슈 } develop

## 작업 ##

git add {나의 작업}
git commit

git pull origin develop:develop
git merge --ff develop

## 컨플릭트 발생시 해결 후
git push origin feature/{ 기능 또는 이슈 }
```

```

```
