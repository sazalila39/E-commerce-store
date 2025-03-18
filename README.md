# E-commerce Store

This project uses Poetry for dependency management, SQLAlchemy for database interactions, asyncio for asynchronous operations, and PostgreSQL as the database backend.

## Poetry Installation
**1. Initialize poetry:**
```bash
poetry init
```
**2. Install Dependencies**
```bash
poetry install
```

### Usage

Create a `.env` file with your database credentials:
```python
DB_NAME=database_name
DB_USER=user_name
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
```
Load environment variables from `.env`

```python
from dotenv import dotenv_values

config = dotenv_values(".env") 
```

### Database Setup & Connection
Install SQLAlchemy & Async Driver and connect to Postresql:
```bash
poetry add sqlalchemy asyncpg

from sqlalchemy.ext.asyncio import create_async_engine
engine = create_async_engine("postgresql+asyncpg://user:password@localhost/db", echo=True)
```
### AWS PostgreSQL Setup
- Create RDS Instance:
- Get Database Endpoint
- Connect: ``` psql -h your-rds-endpoint -U your-username -d your-database-name ```


