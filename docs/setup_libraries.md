#Main Setup

1. Create virtual enviornment:

- In main folder ENOCRAECOMERCE use the command 'python -m venv .venv'
- Verify the name is in gitignore just in case to avoid unnecesary temporary files
- Allow access 'Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser'
- To activate use: '.\.venv\Scripts\Activate.ps1'

2. After activating virtual env install following libraries:
- Use the requirement.txt file to download all libraries related to backend
- Take into account Frontend has its own requierement.txt but this one needs the use of 'npm install <package-name> --legacy-peer-deps' in case of errors in normal npm installation


3. To activate App use:

- Before activating the server if you want to see Django Administrator to directly add information to the DB, create the Super User using 'python manage.py createsuperuser' while standing in src folder.
- To run the app use the command 'python manage.py runserver' while standing in src folder to start the app.
- When running the app use the 'Localhost:<Port>/Admin' url to access with the login information of said Super User if you want to use Django Admin.

4. Local Database Setup Guide (Not needed if DB deploy is up in that case the credencials in settings would have HOST as the aws url).

- Enter pgAdmin4 and create a database called 'store'
- Connect postgres with project through setting with user, pass, and port
- Confirm that you don't have any files in migrations apart from '\__init_' files
- Then use command 'python manage.py showmigrations' and check that you dont have anything checked
- Finally use 'python manage.py makemigrations'
- End it with 'python manage.py migrate'
- Succesfully created database in postgres connected with project check postgres tables :D
