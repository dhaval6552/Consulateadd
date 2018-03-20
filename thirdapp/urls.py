from django.conf.urls import url
from . import views
app_name= 'thirdapp'
urlpatterns = [
    url(r'^index/',views.index,name= 'index'),
    url(r"^register/",views.register,name='register'),
    url(r'^login/',views.Login, name='Login'),
    url(r'^logout/',views.Logout, name='Logout'),
    url(r'^user_detail',views.user_detail,name='user_detail')
]