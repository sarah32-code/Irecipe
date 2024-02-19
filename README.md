Sarah Mustafa 
## Features


- Register and log in.
- Update user inforamtion and reset user password
- Search for a Technical problem based on user operating system
- User able to add and search solutions 
- Admin can delete users, wrong solutions.
- Admin is able to view and delete messages
- location and privacy policy
## Tech stack

  - PostgreSQL
  - Python 3
  - SQLAlchemy 
  - Flask:
    - Flask-bcrypt
    - Flask-mail
  - Jinja
  - AJAX
  - It's-Dangerous
    - TimeJSONWebSignatureSerializer
  - smtplib
  - Bootstrap
  - JS
  - CSS
## Roadmap

### Sprint 1
- create a data model
- create database 
- create templets
- user registration and authentication
- user operating system type
- user profile page and update profile
- Add functionality for a user to enter/search solutions


### Sprint 2
- web design and styling 
- testing and debugging
- create a video-demo

### Installation
1. clone the repository 
2. Activate virtual environment
  - $ cd to the repository
  - $ virtualenv env
  - $ source env/bin/activate
3. Download requirements for requirement.txt
  - $ pip3 install -r requirement.txt
4. Create a file called secrets.sh in the directory
  - $ mkdir secrets.sh
5. Create database
  - $ python3 seed.py
6. Start the server
  - $ python3 server.py
7. follow the link and enjoy! http://127.0.0.1:5001/
8. The app is deployed on AWS follow the link > 44.200.151.245

  

# IRecipe
