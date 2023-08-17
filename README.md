# p-library

>> A terminal and Python GUI app for managing books.

## Alembic for running migrations

### Install Alembic

pip install alembic

### Initialize Alembic (run this in your project directory)

alembic init alembic

### Edit alembic.ini to configure your database connection

### Create an initial migration

alembic revision --autogenerate -m "Initial migration"

### Modify your models (e.g., add new fields)

### Generate a new migration

alembic revision --autogenerate -m "Add new fields"

### Review and adjust the migration script in alembic/versions/

### Apply the migration

alembic upgrade head
