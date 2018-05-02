[![Build Status](https://travis-ci.com/evenset/ketabdan-project.svg?branch=develop)](https://travis-ci.com/evenset/ketabdan-project)

# Ketabdan

Ketabdan is an open source platform to publish electronic books, podcasts, short stories and more

## Installation
You need to install the following tools
1. Docker [community edition (CE)](https://docs.docker.com/install/)
2. Docker [Compose](https://docs.docker.com/compose/install/)

or if you prefer you can use [virtualenv](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-virtualenv-with-Python-3)


### Development Environment

We use `virtualenv` and mainly `Python 3.6` for the initial development. Or you can work with the docker containers
which uses `Python 3.6`

### Docker implementation

You need to install Docker and Docker compose to be able to run this locally. After successful installation the following command will help you to launch your application at `http://localhost:8000`

```bash
docker-compose up
```

## Useful commands
### Docker-compose
Build coker imgages
```bash
docker-compose build
```

Start/Stop dockers
```bash
docker-compose up
docker-compose down
```
Run Django commands
```bash
docker-compose run web python manage.py makemigrations
```
_Remember if you commands create files in your project directory, you need to change the permissions from root to
your local user by `sudo chown -R local_user_name:local_user_group directory`_

### Django
In recent versions of Django you need to create the migrations like this:
```bash
python manage.py makemigrations podcasts
```