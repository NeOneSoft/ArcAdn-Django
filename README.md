# ARCA DNA

Django RestApi that store dna strings into Postgresql database
and evaluate if it has mutation.

#Modules:

- dna
- user authentication (using JWT)

#Requeriments:

- Postgres 4
- Python 3.8
- pip requirements are listed in the 'requirements.txt' file in the project

Before running:

This guide assumes that you already have an instance of postgresql server running and have properly installed python 3.8 in you local computer


Create your database in your local pgAdmin 4 window:
```
Create database named 'arcadn_db'
Keep in mind your database username and password
```

Once that you already have your database, username and password, set those in the follow project route:
```
ArcAdn/settings.py
```


Located at the application root folder run the following commands
```sh
NOTE: BEFORE INSTALL COMMANDS MAKE SURE THAT YOUR VIRTUAL ENVIRONMENT
      IS ACTIVATED ON YOUR DJANGO PROJECT. IF NOT FOLLOW THIS STEPS:
      $python3 -m venv "envname"
      $source "envname"/bin/activate     


$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ python3 manage.py runserver 127.0.0.1:8000
```

#After Server is running

- Open your browser at **127.0.0.1:8000**

#User Authentication

- To get access to API data you have to be registered as user. To do it stop your local server and create a superuser. For this use the next command:
```sh
python3 manage.py createsuperuser
(follow the prompt instructions)
```

#Unit Test Cases

- Unit test cases command:
    - server: pytest core/tests/server/test_server.py
    - auth: pytest core/tests/auth/test_authentication.py

#Local URLS
- api/v1/
- admin/
- docs

#Local URL Level 2 Example:
- http://127.0.0.1:8000/api/v1/POST/mutation/1/dna/ 

#Local URL Level 3 Example:
- http://127.0.0.1:8000/api/v1/POST/mutation/1/statics/

#Aditionl Functions
- Documentation
- User authentication
- JWT
- Unit Test
