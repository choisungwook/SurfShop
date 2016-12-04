import os

apps = ['account', 'address', 'lecture', 'rental', 'shop']
make_command = 'python manage.py makemigrations '
migrate_command = 'python manage.py migrate '

#make migrations
for app in apps:
        os.system(make_command + app)

for app in apps:
        os.system(migrate_command + app)
