# labquiz
A platform for teachers to host quizzes for students
(File will be updated along with the development)

## Instructions
To create a new virtual environment and install all the requirements, run the code:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

To setup the database, follow these instructions:

* Install MySQL
* Create a database and assign it a name
* Create a .env file inside the folder containing settings.py
* Copy the code from .env-sample in your .env file and edit it according to your system preferences.
* In the main project folder, run the code:

        python manage.py makemigrations
        python manage.py migrate

Now you can run the server with the code:

    python manage.py runserver