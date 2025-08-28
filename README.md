## Real Estate Backend (Django+DRF)

### Features

- Listing management (registration,editing,deleting,viewing)
- Category and image management
- User registration and login(JWT)
- API documentation (Swagger and Redoc)

## Running the project locally

### Prerequisites

- Python 3.8 to 3.12
- pip (Python package installer)
- virtualenv (optional but recommended)

### Steps to run the project

1. Clone the repository

```bash
git clone https://github.com/Elid1993/django_Realestate.git && cd django_Realestate
```
2. Create and activate virtual environment

```bash
python -m venv venv  
venv\scripts\activate  #windows
source venv/bin/activate  #linux/mac
```

3. Install requirements

```bash
pip install -r requirements.txt
```
4. Rename `.env.example` to `.env` and configure your own "SECRET_KEY" as needed.

5. database migration

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create administrator user

```bash
python manage.py createsuperuser
```

7. Run project

```bash
python manage.py runserver
```
To access the application, open your web browser and navigate to `http://localhost:8000/`

## Available endpoints

- Swagger UI: http://localhost:8000/api/schema/swagger-ui/
- Redoc: http://localhost:8000/api/schema/redoc/
- Schema (openAPI): http://localhost:8000/api/schema/