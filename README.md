
## Features


- Register and log in.
- Update user inforamtion and reset user password
- Admin is able to view and delete messages
- location and privacy policy
- choose ingredient and browse recipes available
  
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

### Sprint 3
- add more styling
- Create Demo

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
7. follow the link and enjoy! 

  

# IRecipe
