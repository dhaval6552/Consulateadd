from django.shortcuts import render
from mysecondapp.models import User

# Create your views here.
def index(request):
    return render(request,'secondapp/index.html')

def user(request):
    user_list=User.objects.all()
    dic={'user_list':user_list}
    return render(request,'secondapp/users.html',context=dic)
