# WebProjectX
## Where can I find this *AWESOME* website?
Go to https://www.stephenx.tech/ or https://www.stephenx.live/ or https://sx-my-app.herokuapp.com/
## Resources
**[Tailwind Documentation](https://tailwindcss.com/docs)** - Documentation for tailwind css and how to use it  
[Tailwind Kit](https://www.tailwind-kit.com/) - They have some nice css components  
[Django Documentation](https://docs.djangoproject.com/en/3.1/) - Documentation for django, pretty useful  
[Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql) - How to use the database  
## Local usage
Make sure you have python 3.6(untested w/ python 3.2) or above  
First, download all of the dependencies needed  
```
pip install -r requirements.txt
```
To run, enter
```
python manage.py runserver
```
## File structure
- Todo, Formatter, Cryptic, GPAcal - apps
  - Views - the main thing handling the the get and post requests
    - Can pass arguments to the html  
  - Scripts - what you do with the inputs
    - Interact with the views
  - Model - database stuff
- Templates - contains htmls
  - HTMLs - what user actually sees
  - base.html - the template html file so that we don't have to copy and paste everytime we make changes   
## GPA Calculator
- add and delete class button
  - implemented using JS and JQuery
- input fields: class name(optional), grade, weight
- all button and input fields are powered with some *nice* CSS and are *interactive*
  - currently using Tailwind CSS
  - might switch to bootstrap later
  - part of a student advisory center concept
