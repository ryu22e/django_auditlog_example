# django_auditlog_example

Example for django-auditlog

## Requirements

- Git
- Python 3.12 or [rye](https://rye-up.com/)


## Setup

### For Python 3.12

```bash
$ git clone git@github.com:ryu22e/django_auditlog_example.git
$ cd django_auditlog_example
$ python3.12 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements-dev.lock
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver  # Open http://localhost:8000/ in your browser
```

### For rye

```bash
$ git clone git@github.com:ryu22e/django_auditlog_example.git
$ cd django_auditlog_example
$ rye sync
$ source .venv/bin/activate
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
$ python manage.py runserver  # Open http://localhost:8000/ in your browser
```
