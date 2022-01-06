## TODO list API

created with django rest framework

## Description

vertion 1 of a RESTFul API to create users and tasks. Each user can register and keep track of their own tasks and mark them as complete when they are finished. The user has the posibiltiy to edit the description of the tasks and delete them. The admin can create staff users to check all the tasks.

## End Points

### Tasks
-   `GET /api/todos/`
-   `POST /api/todos/`
-   `PUT /api/todos/{pk}/`
-   `GET /api/todos/{pk}/`
-   `PATCH /api/todos/{pk}/`
-   `DELETE /api/todos/{pk}/`

## Documentation

All the API docs are available in **[http://0.0.0.0:8000/docs/](http://0.0.0.0:8000/docs/)** builded with **Django REST Swagger**

## Installation process

### Install the system dependencies
-   **Docker**
-   **Docker-compose**

## Get the code

Clone the repository `https://github.com/ogs13/drf-todoapp.git`

## Run the command to run app

`docker-compose up -d`

## Run the test

`python manage.py test`
