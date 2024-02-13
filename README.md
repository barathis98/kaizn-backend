# Kaizn-Backend

## Description
The Inventory Management Django API is a web application built using the Django framework that provides an interface for managing inventory-related operations via RESTful endpoints. 

##Swagger
Refer this URL for available endpoints : http://3.82.143.168:8000/backend/swagger/

## Prerequisites
- Python
- pip
- pipenv
- Redis
- MySQL

## Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate into the project directory:
    ```bash
    cd <project-directory>
    ```
3. Start Python Environment:
   ```
   pipenv shell
   ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Database Migration
1. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

## Running the Application
1. Run the development server:
    ```bash
    python manage.py runserver
    ```
2. Access the application in your browser at `http://127.0.0.1:8000/`.

## Testing
1. Run tests:
    ```bash
    python manage.py test
    ```
