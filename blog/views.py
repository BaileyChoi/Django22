from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView

# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-pk'  # 최신 등록순으로 나열
    # 템플릿 없는 이유? 모델명_List.html : post_list.html 가 이미 자동으로 생성됐기 때문
    # 파라미터 모델명_list : post_list

    # 추가로 넘기고 싶은 인자 있을때 오버라이딩
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

class PostDetail(DetailView):
    model = Post
    # 템플릿 모델명_Detail.html : post_detail.html
    # 파라미터 모델명 : post

    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count
        return context

def category_page(request,slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    return render(request,'blog/post_list.html', {
        'category': category,
         'post_list': post_list,
         'categories': Category.objects.all(),
         'no_category_post_count': Post.objects.filter(category=None).count
         }
    )

def tag_page(request,slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    return render(request,'blog/post_list.html', {
        'tag': tag,
        'post_list': post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count
        }
    )

# FBV 스타일
#def index(request):
#    posts1 = Post.objects.all().order_by('-pk')

#   return render(
#       request,
#       'blog/index.html',
#       {'posts': posts1}
#   )

#def single_post_page(request, pk):
#   post2 = Post.objects.get(pk=pk)

#   return render(
#       request,
#       'blog/single_post_page.html',
#       {'post': post2}
#   )

