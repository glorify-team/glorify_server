# glorify_server
Glorify project in django.

## Running the project
* Create virtualenv
* install requirements.txt using pip
* Create a `config.py` file in the project `settings.py` folder. Add the following: 
```
SECRET_KEY = "XXXX" # your django secret key

DATABASES = {'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}} # Your DB configuration

STATIC_URL = '/static/' # your static url configuration

STATIC_ROOT = 'basedir/' + STATIC_URL # your static root configuration
```
* migrate the project: `python manage.py migrate`
* start the project: `python manage.py runserver`


