import os
import sys
sys.path.append('/code/gdsite') 
# os.environ['DJANGO_SETTINGS_MODULE'] = '.gdsite.settings'
from django.contrib.auth.models import User
from sys import argv



def username_exists(username):
    if User.objects.filter(username=username).exists():
        return True
    return False


username = argv[1]
print(username)
username_exists(username)