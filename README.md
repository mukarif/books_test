# puskeu_e_document

## Installation
Ubuntu:

```
$ python3 -m venv venv
```
```
$ source venv/bin/activate
```
```
(venv)$ pip install -r requirements.txt
```

```
(venv)$ cd dash/
```
```
(venv) .../dash$ ./manage.py runserver
```

## Install Sentry SDK
```
pip install --upgrade sentry-sdk
```


## run API 
aktifkan settings_api_prod

linux 
```
export DJANGO_SETTINGS_MODULE=dash.settings_api_prod
```

windows 
```
set DJANGO_SETTINGS_MODULE=dash.settings_api_prod
```

jalan kan django api local bersama front end
```
cd dash
./manage.py runserver 8001
```
anda bisa mengakses ap di localhost:8001

## Type dokumen dalam QR 
DS = disposisi QR
ND = nota dinas QR
SR = Surat QR 
TR = Telegram QR

## Tabel Disposisi
```
Disposisi adalah buku Agenda pada staff urtu, terdapat nomor agenda
```

### How to generate a Postgresql Dump/Restore from a Docker container?

Use the following command from a UNIX or a Windows terminal:

```bash
# dump:
$ docker exec -i puskeu_e_document_db_1 pg_dump -U puskeu -F t -d puskeu_e_document > /home/puskeu/puskeu_e_document.dump

# drop schema:
$ docker exec -i puskeu_e_document-db-1 psql -U puskeu -d puskeu_e_document -c "DROP SCHEMA IF EXISTS public CASCADE;"

# create schema:
$ docker exec -i puskeu_e_document-db-1 psql -U puskeu -d puskeu_e_document -c "CREATE SCHEMA public AUTHORIZATION puskeu;"

# restore:
$ docker exec -i puskeu_e_document-db-1 pg_restore -U puskeu -F t -d puskeu_e_document < /Users/user/puskeu_e_document.dump
```

upload file MAX 100MB dari nginx