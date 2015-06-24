# Devf Website

### Development
------
To run the project locally you must follow some few steps:
- Create a virtual enviroment using: ```$virtualenv ENVIRONMENT_NAME```
- Activate your environment using: ```$source ENVIRONMENT_NAME/bin/activate```
- Install all Python required dependencies with: ```$pip install -r requirements.txt```
- Add ALL environment variables to your UNIX session using: ```$export $VARIABLE_NAME='VALUE'```
- Run the project with: ```$./manage.py runserver```
- Visite: [http://localhost:8000/](http://localhost:8000/)

###### Some useful commands
- Create database: ```$./manage.py migrate````
- Create super user to use the admin: ```$./manage.py createsuperuser```
- Deactivate virtualenvironment: ```$deactivate```

### Production
------
The project is fully configured to automatically set a production enviroment when it is deployed to Heroku. Just DO NOT add sensitive PRIVATE KEYS  to the project PLEASE :rocket: