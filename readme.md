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

### Screenshot
On the homepage of the Task API go Create a user account the 
![Website](img.png)



# REST API

The REST API to Todo API is described below.

## Sign Up

### Request

`POST /auth/signup`

    'Accept: application/json' http://127.0.0.1:8000//auth/signup/

Add your sign up request as shown in the sample below:

    `{
        "email": "joedon@gmail.com",
        "username": "joedon",
        "password": "joedon@2023"
     }`

### Response

    {
        "message": "User Created Successfully",
        "data": {
            "email": "joedon@gmail.com",
            "username": "joedon"
        }
    }

## Log In

### Request

`POST /auth/login`

    'Accept: application/json'  ' http://127.0.0.1:8000//auth/login/

Add your log in request after successful registration as show in the sample below:

    `{
        "email": "joedon@gmail.com",
        "username": "joedon",
        "password": "joedon@2023"
     }`

The above request will log in a user and generate a pair authentication as shown below

### Response

    {
        "message": "Login Successfull",
        "tokens": {
            "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjc4ODA2NzY2LCJpYXQiOjE2Nzg3OTk1NjYsImp0aSI6IjU4ZDM1NjkyMmZkNzRmMGJiNGE3ZmJjZjJkODI4MjQxIiwidXNlcl9pZCI6Mn0.S6d6WplOH-UhI5LnEjcTXv0lcHUJpdEy5U23_KyRYsY",
            "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3ODg4NTk2NiwiaWF0IjoxNjc4Nzk5NTY2LCJqdGkiOiI1ZDI5YWM1NjJkM2U0YjhlODc0YzBlYWI5M2JhOGViYiIsInVzZXJfaWQiOjJ9.uOyuKfWWHQ-k_X9QBsMb2urD0zrzQi36h5_Z1NKF3Tg"
        }
    }
<!--  -->