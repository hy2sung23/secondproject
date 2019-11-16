from django.shortcuts import render
from .models import Blog #동일한 폴더를 말할 때 .(dot) 사용, 여기서 Blog라는 클래스를 불러와라
# Create your views here.

def home(request):
    blogs = Blog.objects #Blog라는 클래스 안에 있는 객체를 blogs라는 녀석에 담을 것이다 = 쿼리셋
    return render(request, 'home.html', {'blogs':blogs})