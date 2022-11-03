# 앱 만들기
# python manage.py startapp 앱이름
# (venv) ls로 확인

# css 파일
# static/bl/boot~  temp/bl/post_list.html-{% load~%},<link rel~>

# 모델 만들기
# blog/models.py   settings.py-App 추가  makemigrations&migrate  blog/admin.py

# admin에서 제목 표현
# models.py-__str__

# 서울 기준으로 작성 시각 설정
# settings.py-TIME_ZONE,USE_TZ

# 자동으로 작성 시각 수정시각 설정
# model.py-auto  makem&mig

# URL 설정
# Prj/urls.py

# FBV스타일 post_list
# Prj/urls-path  blog/urls.py-path  views.py-index(request)  tem/bl/index.html

# 템플릿 문법
# {% for in/endfor %} {% if/elif/else/endif %}
# {{ 변수 }}  {{ 변수 | 옵션 }}

# CBV스타일 post_list
# urls-path   views.py-class   temp/bl/post_list.html-for p in post_list

# 미디어
# setting.-MEDIA  models.-head image_  makem&mig  Prj/url.-urlpatterns+=  post_list.-src={{p.head.url }},{% if }
# 파일
# models.=file_  post_detail.-{% if %}

# test
# assertEqual(a,b): a==b, assetIs(a,b): a is b, assertIn/NotIn(a,b): a in b assetTrue(x): x is True

# 다대일 마이그레이션
# makem  fix one-off: 1  dafault value: 1

