This guide will help you set up a Django project and run it on your local machine.

Prerequisites
Before we get started, you need to have the following software installed on your computer:

1. Python (version 3.6 or later)
2. pip (package manager for Python)
3. Virtualenv (optional, but recommended for isolating the project environment)

Step 1: Create a Virtual Environment
It's a good practice to isolate the project environment from the system environment. To do this, you can use virtualenv.

Install virtualenv using pip:

>>pip install virtualenv

Create a new virtual environment and activate it:

>>virtualenv venv
>>venv/Source/activate

Step 2: Run the Server

>>python manage.py runserver
