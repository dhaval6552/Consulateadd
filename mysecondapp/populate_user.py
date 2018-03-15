import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'Practice1.settings')
import django
django.setup()
from faker import Faker
from mysecondapp.models import User
fakegen=Faker()
def add_user(n):
    for i in range(n):
        name=fakegen.name().split()
        first=name[0]
        last=name[1]
        email1=fakegen.email()
        print(User.objects.get_or_create(first_name=first,last_name=last,email=email1))
if __name__ == '__main__':
    add_user(10)


