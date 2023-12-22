## Task Manager Using Django



## Features
- User login/Register 
- Task creation forms using crispy forms
- Complete Search and filter options
- Multiple image uploads and delete corresponding to the task
- LoginRequired to to access
- Customized admin for search and filter task


## Technology Used
-   Programming Language: Python 3.12
-   Framework: Django=4.2, djangorestframework=3.14
-   Database: Postgres16
-   Front-end: HTML5, CSS3, Bootstrap5
-   VCS: Git, GitHub
-   Editor: VS Code
-   Operating System: Windows 11



## How to Run Locally

-   Install Python

## Installation

Download and install python from their website

```bash
  https://www.python.org/downloads/
```

-   Clone the repository

```bash
git clone https://github.com/fahadfoysal/task_manager
```

-   Go to the project directory

```bash
cd task-manager
```

-   Create a virtual environment

```bash
python -m venv venv
```

-   Activate the virtual environment

```bash
venv/bin/activate
```

-   Install all the packages from requirements.txt

```bash
pip install -r requirements.txt
```

-   Run the server

```bash
python manage.py runserver
```

-   Open your browser with the following URL  http://127.0.0.1:8000/

-   To deactivate the virtual environment

```bash
deactivate
```

### Setup PostgreSQL Database

-   Install Postgres database 

```bash
https://www.postgresql.org/download/
```

-   Login to Postgres using the command prompt

```bash
psql -u postgres
```

-   Create a database

```bash
CREATE DATABASE taskmanagerdb;
```

-   Exit from the command prompt


-   Now, Configure setings.py `

-  Create environment variables to keep secret database info, and secret key. file name should be .env

```bash
SECRET_KEY=
DEBUG=
DB_ENGINE=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_HOST=
DB_PORT=
```

### Load taskdb.json fixtures from taskdb.json

-   Run the command to load data from `taskdb.json`

```bash
python manage.py loaddata taskdb.json
```

-   Make migrations

```bash
python manage.py make migrations
```
-   Migrate

```bash
python manage.py migrate
```


### To use the Admin Panel

-   Create a superuser with your username, email address, and password, hit the following command to create.

```bash
python manage.py createsuperuser
```

### Admin Panel

-   Run the server from your command prompt or terminal

```bash
python manage.py runserver
```

-   Open your browser with the following URL http://127.0.0.1:8000/admin


-   Login with your created superuser account and explore and manage as the admin.


## API Details

-   **Endpoint:** http://127.0.0.1:8000/api/tasks
-   **Method:** GET, PUT
-   **Description:**
    -   Returns all the tasks
    - Create task

-   **Endpoint:** http://127.0.0.1:8000/api/tasks/1/
-   **Method:** GET, PUT, PATCH, DELETE
-   **Description:**
    -   Retrieve Task
    -   Create Task
    -   Update task
    -   Delete task

## For Mac and Linux

-   use command as python3, pip3

## Installation

$ brew install python3 or
sudo apt install python3
