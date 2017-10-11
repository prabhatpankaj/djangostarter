from .production import *

from shutil import copyfile
src = os.path.join(BASE_DIR, 'db.sqlite3')
dst = "/tmp/db.sqlite3"
copyfile(src, dst)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': dst, 
    }
}