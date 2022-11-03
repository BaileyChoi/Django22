from django.urls import path
from . import views

urlpatterns = [     #IP주소/blog/
    path('', views.PostList.as_view()), # CBV스타일
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page)
    # path('', views.index),   #IP주소/blog  FBV 스타일
    # path('<int:pk>/', views.single_post_page),
]
