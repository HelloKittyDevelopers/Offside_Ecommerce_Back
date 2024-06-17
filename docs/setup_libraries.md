#Main Setup

1. Create virtual enviornment:
- In main folder ENOCRAECOMERCE use the command 'python -m venv .venv'
- Verify the name is in gitignore just in case to avoid unnecesary temporary files
- To activate use: '.\.venv\Scripts\Activate.ps1'

2. After activating virtual env install following libraries:
- pip install psycopg2  
- pip install django
- pip install django-allauth      
- pip install django-crispy-forms 
- pip install django-countries    

// correr esto estando en el folder front
- npm install @craco/craco
- npm install react-router-dom
- npm install bootstrap bootstrap
- npm install react-bootstrap bootstrap

3. To activate App use:
- While in front folder use 'npm run build' to make build of the front end components
- Then run 'python manage.py runserver' while standing in src folder to start the app