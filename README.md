# books_test

## Database Configuration
1. Buat database di Postgresql
2. Di ```settings.py``` rubah HOST, NAME, USER, PASSWORD dan PORT sesuai koneksi anda 
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'book_test_db',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'p@ssw0rd',
        'PORT': '5432',
    },
}
```

## Redis Configuration
Redis fro Windows:
Silahkan mengikuti langkah-langkah diwebsite ini
```
https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/
```

Redis fro Linux:
Silahkan mengikuti langkah-langkah diwebsite ini
```
https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-linux/
```
Note : Digunakan untuk optimasi query

## Installation
Ubuntu atau Bash Terminal:

install virtual environment
```
$ python3 -m venv venv
```
Mengaftifkan virtual environment
```
$ source venv/bin/activate
```
Install library Python
```
(venv)$ pip install -r requirements.txt
```
Masuk ke directory App
```
(venv)$ cd dash/
```
migrations database
```
(venv) .../dash$ ./manage.py migrate
```
python collectstatic
```
(venv) .../dash$ ./manage.py collectstatic
```
runing Project
```
(venv) .../dash$ ./manage.py runserver
```
runing Unit Test
```
(venv) .../dash$ ./manage.py test
```

CMD Terminal:

install virtual environment
```
$ python3 -m venv venv
```
Mengaftifkan virtual environment
```
$ venv\Scripts\activate
```
Install library Python
```
(venv)$ pip install -r requirements.txt
```
Masuk ke directory App
```
(venv)$ cd dash/
```
migrations database
```
(venv) .../dash$ python3 manage.py migrate
```
python collectstatic
```
(venv) .../dash$ python3 manage.py collectstatic
```
runing Project
```
(venv) .../dash$ python3 manage.py runserver
```
runing Unit Test
```
(venv) .../dash$ python3 manage.py test
```