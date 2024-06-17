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
- npm install @craco/craco

3. To activate App use:
- While in front folder use 'npm run build' to make build of the front end components
- Then run 'python manage.py runserver' while standing in src folder to start the app