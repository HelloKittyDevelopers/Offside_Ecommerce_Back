#Main Setup

1. Create virtual enviornment:

- In main folder ENOCRAECOMERCE use the command 'python -m venv .venv'
- Verify the name is in gitignore just in case to avoid unnecesary temporary files
- Allow access 'Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser'
- To activate use: '.\.venv\Scripts\Activate.ps1'

2. After activating virtual env install following libraries:

pip install psycopg2 
pip install django
pip install django-allauth
pip install django-crispy-forms
pip install django-countries

// correr esto estando en el folder front

npm install @craco/craco
npm install react-router-dom
npm install bootstrap bootstrap
npm install react-bootstrap bootstrap
npm install typescript
npm install yarn
yarn add redux react-redux redux-thunk redux-devtools-extension


3. To activate App use:

- While in front folder use 'npm run build' to make build of the front end components
- Before activate the server and visualize the Django Administrator, create the Super user 'python manage.py createsuperuser'
- Then run 'python manage.py runserver' while standing in src folder to start the app

4. Local Database Guide.

- Enter pgAdmin4 and create a database called 'store'
- Connect postgres with project through setting with user, pass, and port
- Confirm that you don't have any files in migrations apart from '\__init_' files
- Then use command 'python manage.py showmigrations' and check that you dont have anything checked
- Finally use 'python manage.py makemigrations'
- End it with 'python manage.py migrate'
- Succesfully created database in postgres connected with project check postgres tables :D
