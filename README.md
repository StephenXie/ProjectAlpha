# ProjectAlpha
[![Build Status](https://travis-ci.com/QLSCO/ProjectAlpha.svg?branch=master)](https://travis-ci.com/QLSCO/ProjectAlpha) [![Django CI](https://github.com/QLSCO/ProjectAlpha/actions/workflows/django.yml/badge.svg)](https://github.com/QLSCO/ProjectAlpha/actions/workflows/django.yml) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![GitHub issues](https://img.shields.io/github/issues/QLSCO/ProjectAlpha)](https://GitHub.com/QLSCO/ProjectAlpha/issues/) [![GitHub issues](https://img.shields.io/github/issues-closed/QLSCO/ProjectAlpha)](https://github.com/QLSCO/ProjectAlpha/issues?q=is%3Aissue+is%3Aclosed) [![GitHub pull-requests](https://img.shields.io/github/issues-pr/QLSCO/ProjectAlpha.svg)](https://GitHub.com/QLSCO/ProjectAlpha/pulls/) [![GitHub pull-requests](https://img.shields.io/github/issues-pr-closed/QLSCO/ProjectAlpha.svg)](https://github.com/QLSCO/ProjectAlpha/pulls?q=is%3Apr+is%3Aclosed) [![Made by Stephen X](https://img.shields.io/badge/Made%20by-Stephen%20X-orange)](https://github.com/StephenXie)
## Where can I find this *AWESOME* website?
Go to https://www.stephenx.tech/ or https://www.stephenx.live/ or https://sx-my-app.herokuapp.com/ or https://www.stephenxie.com/
## Wiki
**Go to the [Wiki page](https://github.com/QLSCO/ProjectAlpha/wiki) for more information and fun facts about this project**
## Resources
**[Tailwind Documentation](https://tailwindcss.com/docs)** - Documentation for tailwind css and how to use it  
[Tailwind Kit](https://www.tailwind-kit.com/) - They have some nice css components  
[Django Documentation](https://docs.djangoproject.com/en/3.1/) - Documentation for django, pretty useful  
[Heroku Postgres](https://devcenter.heroku.com/articles/heroku-postgresql) - How to use the database  
## Local usage
Make sure you have python 3.6 or above  

First, install all of the dependencies needed  
```
pip install -r requirements.txt
```
To run, enter
```
python manage.py runserver
```
## File structure
- Todo, Formatter, Cryptic, GPAcal, PasteX, Linky - apps
  - Views - the main thing handling the the get and post requests
    - Can pass arguments to the html  
  - Scripts - what you do with the inputs
    - Interact with the views
    - Logics
  - Models - database stuff
- Templates - contains htmls
  - HTMLs - what user actually sees
  - base.html - the template html file so that we don't have to copy and paste everytime we make changes   
- AppX - Home page
- ProjectX - Settings
  - url.py - url of pages
- Static - Assets(e.g. images, css, js)
## GPA Calculator
- add and delete class button
  - implemented using JS and JQuery
- input fields: class name(optional), grade, credit, weight
- using AJAX to update GPA when the form is changed without refreshing the page
  - using jQuery
- all button and input fields are powered with some *nice* CSS
  - currently using Tailwind CSS
  - might switch to bootstrap later
- part of a student advisory center concept
  - college preparation
  - precentile finding
  - let user select what college they wanted to go to
    - gather dataset from colleges
    - show how users' GPA compare to other candidates
    - possibly implement goals/"tracks" the user should follow to reach their goal. (i.e: how they need to improve their grade to reach certain GPA, etc.)
