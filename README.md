## Features
- User authentication and authorization.
- RESTful API endpoints for catalog, cart, identity, order.
- MySQL Database management using Django ORM.
- Asynchronous task management using Django Q.
- Environment-specific configurations.
- Swagger API documentation with drf_yasg.
- Uses rest framework JWT for auth 

# View documentation at:
https://4413backend-production.up.railway.app/swagger/

# View admin page at:
https://4413backend-production.up.railway.app/admin/

# View Frontend at:
https://4413frontend-production.up.railway.app/

# Prerequisites
- Python 3.11
- MySQL or PostgreSQL

- Specify environment variables in .env file for your database connection

## Running locally

```
python -m venv venv
source venv/bin/activate
```

```
pip install -r requirements.txt
```

```
python manage.py migrate
python manage.py createsuperuser
```

```
python manage.py runserver
```