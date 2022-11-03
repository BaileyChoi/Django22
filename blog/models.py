from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # unique:유일한 값
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)  # allow:한글사용가능

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'    # tag 클릭했을때 해당태그이름 모음페이지 나오게


# 숫자인 Pk 대신 읽을 수 있는 텍스트로 URL만들때
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # unique:유일한 값
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True) # allow:한글사용가능

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    class Meta:
        verbose_name_plural = 'Categories' #지정해준 값으로 복수형을 출력

class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    # %Y 2022, %y 22
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)  # 다대일관계, null:공란OK

    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)    # 다대일

    tags = models.ManyToManyField(Tag, blank=True) # 다대다, null=true 필요없음

    def __str__(self):
        return f'[{self.pk}]{self.title} :: {self.author} : {self.created_at}'

    def get_absolute_url(self):     # 개별 고유 url - 이름표현에 사용
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]  # 주어진 배열에서 가장 마지막 원소
        # a.txt -> a[0] / txt[1]
        # b.docx -> b / docx
        # c.xlsx -> c / xlsx
        # a.b.c.txt -> a[0] / b[1] / c[2] / txt[-1] 