# E-commerce Store

This project uses Poetry for dependency management, SQLAlchemy for database interactions, asyncio for asynchronous operations, and PostgreSQL as the database backend.

## Poetry Installation

**Install Dependencies**
```bash
poetry install
```
## Alembic Setup
**Create a new migration:**
```bash
alembic revision --autogenerate -m "your message"
```
**Apply migrations:**
```bash
alembic upgrade head
```

## AWS PostgreSQL Setup
- Create RDS Instance
- Get Database Endpoint
- Connect: ``` psql -h your-rds-endpoint -U your-username -d your-database-name ```


