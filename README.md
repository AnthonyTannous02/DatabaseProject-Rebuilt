# DatabaseProject-Rebuilt

the Fall semester of 2022 was when I took the Database Systems Course. Fall 2022 was one of my hardest semesters yet. However, despite all the disappointments
and hardship, I refused to concede and came out victorious.

Long Story Short, The DB Systems course required us to create a Website that was to be implemented using the MySQL DBMS with any languages we needed.
Personally, I chose back-end and contributed to most of the Database design (which I beleive is still not as perfect as I thought it would be).
I used the Flask Python Framework as I was already familiar with Python. After the semester ended, I knew I wanted to be productive and create a website
while I was having my winter break. After considering all my options, I chose to rebuild the DB project the way I envisioned it.

To achieve my goal, I went ahead and deleted everything that my project partners built (front-end, DB) in order to respect their work and fully implement 
my vision of the website.

I used the following tools to create the Website "Deliverou":
  - MySQL (Workbench and Server)
  - Python and Flask
  - HTML 5
  - CSS 3
  - Javascript (including jQuery and AJAX)

!important: In order for this website to work properly on your local machine, it is highly recommended that you run the following command in the terminal of
your project: pip install -r requirements.txt

The Website was divided into three sections:
  - home_page (It was used mainly for the home page. It included the navbar and footer that were implemented inside base.html and extended using Jinja2 to avoid
                rewriting all the code again)
  - auth_page (It served as the container for everything related to Login, Signup, Profile, etc.)
  - main_page (It served as a container for anything related to the core functionalities of the website)
  - DBs (contains the databases that should be executed by ..........
  
As for the files found outside the sections mentioned, they are as follows:
  - mainApp.py (used to initiate and run the flask application as well as managing all the blueprints and additions)
  - database.py (includes classes and objects that were used to facilitate the connection process between MySQL and Flask)
  - dataLoader.py (includes 90% of the queries used in the applications, it was created to minimize the wasted and redundant lines used in the route.py files)
 
As for the Sections, they are mainly split into parts as shown below:
  - 
