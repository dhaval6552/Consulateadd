from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/',views.index,name= 'index'),
    url(r'^user/',views.user,name='user'),
    url(r'^details',views.form_details,name='form_details')
]