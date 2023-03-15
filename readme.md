# Todo API.

This is simple REST API that allows users to create, retrieve, update, and delete items from a todo list. The APIis using JWT Authentication and is be able to:
● Retrieve a list of all todo items.
● Retrieve a specific todo item by ID.
● Update a specific todo item by ID.
● Delete a specific todo item by ID.


### Cloning the repository

Clone the repository using the command below :

```bash
git clone https://github.com/WayneMusungu/PetWebsite.git

```

Move into the directory where we have the project files :
```bash
cd emmerce_project

```

Create a virtual environment :
```bash
# Create our virtual environment
python -m venv venv

```

--> Activate the virtual environment : <br><br>
windows
```bash
venv\scripts\activate

```
linux
```bash
source venv/bin/activate

```

--> Install the requirements :
```bash
pip install -r requirements.txt

```

--> Migrate Database
```bash
python manage.py migrate

```

--> Create Super User
```bash
python manage.py createsuperuser

```

#

### Running the App

--> To run the App, we use :
```bash
python manage.py runserver

```

> ⚠ Then, the development server will be started at http://127.0.0.1:8000/

<!-- ### Screenshot
On the homepage of the Task API go Create a user account the 
![Website](img.png) -->



# REST API

The REST API to Todo API is described below.

## AUTHENTICATION

### Sign Up

#### Request

`POST /auth/signup` `Accept: application/json`

    http://127.0.0.1:8000/auth/signup/

Add your sign up request as shown in the sample below:

    {
        "email": "warren@gmail.com",
        "username": "warren",
        "password": "warren@2023"
    }

#### Response

    {
        "message": "User Created Successfully",
        "data": {
            "email": "warren@gmail.com",
            "username": "warren"
        }
    }

### Log In

#### Request

`POST /auth/login` `Accept: application/json`

    http://127.0.0.1:8000/auth/login/

Add your log in request after successful registration as show in the sample below:

    `{
        "email": "warren@gmail.com",
        "password": "warren@2023"
     }`

The above request will log in a user and generate a pair authentication as shown below

#### Response

    {
        "message": "Login Successfull",
        "tokens": {
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODA2NzY2LCJpYXQiOjE2Nzg3OTk1NjYsImp0aSI6IjU4ZDM1NjkyMmZkNzRmMGJiNGE3ZmJjZjJkODI4MjQxIiwidXNlcl9pZCI6Mn0.S6d6WplOH-UhI5LnEjcTXv0lcHUJpdEy5U23_KyRYsY",
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3ODg4NTk2NiwiaWF0IjoxNjc4Nzk5NTY2LCJqdGkiOiI1ZDI5YWM1NjJkM2U0YjhlODc0YzBlYWI5M2JhOGViYiIsInVzZXJfaWQiOjJ9.uOyuKfWWHQ-k_X9QBsMb2urD0zrzQi36h5_Z1NKF3Tg"
        }
    }

### Create Token Pair
Upon successful log in one need to create token pair. This takes a set of user credentials and returns an access and refresh JSON web token pair to prove their authentication of those credentials.

#### Request

`POST /auth/jwt/create` `Accept: application/json`

    http://127.0.0.1:8000/auth/jwt/create/

Pass in your logged in credentials to generate a refresh and an access token

    `{
        "email": "joedon@gmail.com",
        "password": "joedon@2023"
     }`

#### Response

    {
        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3ODg4NjAwNSwiaWF0IjoxNjc4Nzk5NjA1LCJqdGkiOiJhODQ5MzEyMjc3ZmU0ZmFjYWJlMGE4YjdiNzU5Nzc4MiIsInVzZXJfaWQiOjJ9.KjBEq1xGbmK9OZnTbneSe5XDjthrFispJPVtiwu5HKM",
        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODcwMjMxLCJpYXQiOjE2Nzg4NjMwMzEsImp0aSI6IjYyNWVlY2E3ZGVmOTQ5NTBhZjEzOTA3NDg3MzQ4MzY0IiwidXNlcl9pZCI6Mn0.7hAADOuA3490OrifJg3pp5hSBPeYED3siO-T4Z-tjCI"
    }

> ⚠ Ensure, to copy the value of the access token and pass it as the bearer token as it will be responsible for enabling the user to create, update and delete a todo task

## TASKS
Here a user will be able to get all tasks, create, update and delete

### Show all Tasks
Here no authentication is required to view all tasks posted by different users.

#### Request

`GET /tasks` `Accept: application/json`

    http://127.0.0.1:8000/tasks/
Send a request to the above endpoint and it will show all tasks posted by registered users

#### Response

    {
        "count": 2,
        "next": null,
        "previous": null,
        "results": [
            {
                "id": 2,
                "title": "To do",
                "description": "Finish on the to do project",
                "created_at": "2023-03-14T13:29:14.126753Z",
                "updated_at": "2023-03-14T13:29:14.325222Z"
            },
            {
                "id": 1,
                "title": "History",
                "description": "Read on Kenyas's History",
                "created_at": "2023-03-14T13:13:51.649873Z",
                "updated_at": "2023-03-14T13:29:34.811755Z"
            }
        ]
    }

### Show a specific task
This endpoint retrieves a specific task by its id.

#### Request

`GET /tasks/{id}` `Accept: application/json`

    http://127.0.0.1:8000/tasks/1/
This will show the task id 1

#### Response

    {
        "id": 1,
        "title": "History",
        "description": "Read on Kenyas's History",
        "created_at": "2023-03-14T13:13:51.649873Z",
        "updated_at": "2023-03-14T13:29:34.811755Z"
    }

### Show a specific task that does not exit
This endpoint retrieves a specific task by its id that is non existent.

#### Request

`GET /tasks/{id}` `Accept: application/json`

    http://127.0.0.1:8000/tasks/99/
This will show an error because the task by that id does not exist

#### Response
    {
        "detail": "Not found."
    }

### Create a Task
This endpoint is responsible for creating a task

Remember the access token? Click on `Authorization` on token type select `Bearer Token` on the token then pass in the acccess token `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODcwMjMxLCJpYXQiOjE2Nzg4NjMwMzEsImp0aSI6IjYyNWVlY2E3ZGVmOTQ5NTBhZjEzOTA3NDg3MzQ4MzY0IiwidXNlcl9pZCI6Mn0.7hAADOuA3490OrifJg3pp5hSBPeYED3siO-T4Z-tjCI`

#### Request

`POST /tasks/` `Accept: application/json`

    http://127.0.0.1:8000/tasks/

In the body pass in the json format of the tasks like shown below:

    {
        "title": "Phone",
        "description": "Make a review on the latest phone on my youtube channel."
    }


#### Response
    {
        "id": 4,
        "title": "Phone",
        "description": "Make a review on the latest phone on my youtube channel.",
        "created_at": "2023-03-15T06:58:45.025809Z",
        "updated_at": "2023-03-15T06:58:45.087628Z"
    }

### Get a Current User's Task
This endpoint is responsible for getting all the tasks of the logged in user

Remember the access token? Click on `Authorization` on token type select `Bearer Token` on the token then pass in the acccess token `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODcwMjMxLCJpYXQiOjE2Nzg4NjMwMzEsImp0aSI6IjYyNWVlY2E3ZGVmOTQ5NTBhZjEzOTA3NDg3MzQ4MzY0IiwidXNlcl9pZCI6Mn0.7hAADOuA3490OrifJg3pp5hSBPeYED3siO-T4Z-tjCI`

#### Request

`GET /tasks/current_user` `Accept: application/json`

    http://127.0.0.1:8000/tasks/current_user/

Send a blank request to the above endpoint and a response will show the user's task links

#### Response
    {
        "id": 2,
        "username": "warren",
        "email": "warren@gmail.com",
        "todos": [
            "http://127.0.0.1:8000/tasks/4/",
            "http://127.0.0.1:8000/tasks/2/",
            "http://127.0.0.1:8000/tasks/1/"
        ]
    }

### Update a specific task
This endpoint is responsible for updating a specific task by its id

Remember to do the same procedure of passing in your bearer token? Click on `Authorization` on token type select `Bearer Token` on the token then pass in the acccess token `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODcwMjMxLCJpYXQiOjE2Nzg4NjMwMzEsImp0aSI6IjYyNWVlY2E3ZGVmOTQ5NTBhZjEzOTA3NDg3MzQ4MzY0IiwidXNlcl9pZCI6Mn0.7hAADOuA3490OrifJg3pp5hSBPeYED3siO-T4Z-tjCI`

#### Request

`PUT /tasks/1` `Accept: application/json`

    http://127.0.0.1:8000/tasks/1/

On the body section pass in the JSON format of title and description as shown below:
    {
        "title": "History",
        "description": "Read on Agrarian Revolution"
    }

#### Response
    {
        "id": 1,
        "title": "History",
        "description": "Read on Agrarian Revolution",
        "created_at": "2023-03-14T13:13:51.649873Z",
        "updated_at": "2023-03-15T07:18:26.783015Z"
    }

### Delete a specific task
This endpoint is responsible for deleting a specific task by its id

Remember to do the same procedure of passing in your bearer token? Click on `Authorization` on token type select `Bearer Token` on the token then pass in the acccess token `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODcwMjMxLCJpYXQiOjE2Nzg4NjMwMzEsImp0aSI6IjYyNWVlY2E3ZGVmOTQ5NTBhZjEzOTA3NDg3MzQ4MzY0IiwidXNlcl9pZCI6Mn0.7hAADOuA3490OrifJg3pp5hSBPeYED3siO-T4Z-tjCI`

#### Request

`DELETE /tasks/4` `Accept: application/json`

    http://127.0.0.1:8000/tasks/4/


### Error Response 
Here are some of the error responses that will show:

#### Sign Up with preexisting email
Signing up with an already registered email:
   
    {
        "errors": [
            "Email has already been used"
        ]
    }

#### Log In with invalid credentials
Log in with invalid credentials:
   
    {
        "message": "Invalid email or password"
    }

#### No Token Response
In case where no token was passed the following response will be displayed:
    
    {
    "detail": "Authentication credentials were not provided."
    }

#### Invalid Token Response
In the case of an invalid token the following response will be displayed:

    {
        "detail": "Given token not valid for any token type",
        "code": "token_not_valid",
        "messages": [
            {
                "token_class": "AccessToken",
                "token_type": "access",
                "message": "Token is invalid or expired"
            }
        ]
    }

### Deleting a task that does not exist
This endpoint deletes a specific task by its id that is non existent.

#### Request

`DELETE /tasks/{id}` `Accept: application/json`

    http://127.0.0.1:8000/tasks/99/
This will show an error because the task by that id does not exist

#### Response
    {
        "detail": "Not found."
    }

### Deleting a tasks that is not uploaded by a user
This endpoint deletes a task created by another user

#### Request

`DELETE /tasks/{id}` `Accept: application/json`

    http://127.0.0.1:8000/tasks/99/
This will show an error because the task by that id is not assigned to that user

#### Response
    {
        "detail": "You do not have permission to perform this action."
    }

