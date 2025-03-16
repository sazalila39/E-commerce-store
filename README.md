# E-commerce Store
## Overview

This project uses Poetry for dependency management, SQLAlchemy for database interactions, asyncio for asynchronous operations, and PostgreSQL as the database backend.

## Prerequisites
Ensure you have the following installed:

- Python >= 3.12

- Poetry (dependency management)

- PostgreSQL (database backend)

## Required Dependencies

The project requires the following dependencies:
```bash
[tool.poetry.dependencies]
python = ">=3.12"
sqlalchemy = "^2.0.39"
psycopg2-binary = "^2.9.10"
asyncpg = "^0.30.0"
python-dotenv = "^1.0.1"
```

## Poetry Installation
**1. Installation**
```bash
pip install poetry
```
**2. Initialize Poetry**
If starting a new project:
```bash
poetry new project_name
```
If setting up manually in an existing directory:
```bash
poetry init
```
This will create a pyproject.toml file interactively.

**3. Install Dependencies**
```bash
poetry install
```
This will create a virtual environment and install all dependencies listed in `pyproject.toml` and `poetry.lock`.

**4. Managing Dependencies**
- To add new dependencies:
```bash
poetry add package_name
```
- To remove dependencies:
```bash
poetry remove package_name
```
- To update dependencies:
```bash
poetry update
```
- To regenerate `poetry.lock`:
```bash
poetry lock
```

## Installing psycopg2-binary
`psycopg2-binary` is a Python package that provides a simple way to connect and interact with PostgreSQL databases.
You can install psycopg2-binary using pip:
```bash
poetry add psycopg2-binary
```
## Installing python-dotenv
`python-dotenv` is a Python library that loads environment variables from a `.env` file into your application, which is useful for managing database credentials and other sensitive information.

Install `python-dotenv` using:

```bash
poetry add python-dotenv
```
### Usage

Create a `.env` file with your database credentials:
```python
DB_NAME=mydatabase
DB_USER=myuser
DB_PASSWORD=mypassword
DB_HOST=localhost
DB_PORT=5432
```
Load environment variables from `.env`

```python
from dotenv import dotenv_values

config = dotenv_values("../../.env") 
```

## Installing SQLAlchemy and AsyncIO Support
Install SQLAlchemy and async database driver:
```bash
poetry add sqlalchemy asyncpg
```
## Basics of Async and Await

`async` **keyword:** Used to define an asynchronous function (coroutine).

`await` **keyword:** Used to pause execution until an asynchronous task completes.

### Async and Await in SQLAlchemy

When working with databases, asynchronous programming helps prevent blocking operations.

#### Synchronous Example:
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://user:password@localhost/db")
Session = sessionmaker(bind=engine)

def get_data():
    session = Session()
    result = session.execute("SELECT * FROM users;")
    data = result.fetchall()
    session.close()
    return data
```
#### Asynchronous Example:
```python
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine("postgresql+asyncpg://user:password@localhost/db")
Session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async def get_data():
    async with Session() as session:
        result = await session.execute("SELECT * FROM users;")
        return result.fetchall()
```

## AWS PostgreSQL Setup and Usage

### Create an RDS PostgreSQL Instance:

**1.** On the AWS Management Console, navigate to RDS > Create Database .

**2.** Choose Standard Create.

**3.** Select PostgreSQL as the database engine.

**4.** Choose an instance type based on your needs (db.t3.micro for free tier).

**5.** Set a database name, username, and password.

**6.** Configure security settings:
- Ensure Public Access is enabled if you want to connect externally.

- Add inbound rules to the security group to allow connections from your IP.

**7.** Click Create Database and wait for the instance to be available.

### Get the Database Endpoint

Navigate to RDS > Databases.

Click on your PostgreSQL instance.

Copy the Endpoint (e.g., your-rds-endpoint.rds.amazonaws.com).

## Connecting to AWS PostgreSQL
**1. Set Up Environment Variable**
```bash
DATABASE_URL="postgresql+asyncpg://your-username:your-password@your-rds-endpoint:5432/your-database-name"
```
**2. Connect Using psql**
```bash
psql -h your-rds-endpoint.rds.amazonaws.com -U your-username -d your-database-name
```
Enter your password when prompted.

**3. Connect Using SQLAlchemy in Python**
```bash
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql+asyncpg://your-username:your-password@your-rds-endpoint:5432/your-database-name"
engine = create_async_engine(DATABASE_URL, echo=True)
```
## Running the Project
### Activate Virtual Environment
Poetry automatically creates a virtual environment:
```bash
poetry shell
```
### 2. Run the Application
Use the following command to start the application:
```bash
python my_file.py
```

## 🤝 Contributing

### Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch `git checkout -b feature-branch`.

Commit your changes `git commit -m "Added a new feature"`.

Push to the branch `git push origin feature-branch`.

Open a Pull Request.


