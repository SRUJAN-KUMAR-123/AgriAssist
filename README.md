# AgriAssist

### Requirements
- python 3.11
- postgres server


### Steps to deployment
1. Create a virtual environment in AgriAssist directory\
   `python3 -m venv venv`
2. Install required dependencies (make sure venv is activated)\
   `pip install -r requirements.txt`
3. Install PostGres Server\
   [Link to Installer](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
4. Migrate Django models\
   `python manage.py migrate`
5. Run Django server\
   `python manage.py runserver`
- Create django super user to access/modify models data\
  `python manage.py createsuperuser`

