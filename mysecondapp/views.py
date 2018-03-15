from django.shortcuts import render
from mysecondapp.models import User
from mysecondapp.forms import Details

# Create your views here.
def index(request):
    return render(request,'secondapp/index.html')

def user(request):
    user_list=User.objects.order_by('first_name')
    dic={'user_list':user_list}
    return render(request,'secondapp/users.html',context=dic)

def form_details(request):
    form=Details()
    if request.method=="POST":
        form=Details(request.POST)
        if form.is_valid():
            form.save()

    return render(request,'secondapp/form_details.html',{'form': form})
