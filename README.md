# David McCartney DevOps Week 5 Project
## MMA Stats web app 

### Resources
* Trello: https://trello.com/b/AffqoFeG/project-board
* Website: http://35.197.208.121/

### Contents
* Brief
    * Minimum Requirements
* Functionality
* Data
* Tech Stack
* CI Pipeline
* Front-End Design
* Risk Assessment
* Difficulties and Lessons learned
* Future Improvements
* Authors

## Brief
For my week 5 project the brief I received was to create a CRUD application using Flask and Python making use of practices and methodologies learned in the weeks leading up to the project. These 
included things such as OOP, Scrum, Automation, Continuous Integration and Continuous Development. 

Using Flask and Python I was tasked with creating a web application that could connect to a mySQL database, take a user input(being fighter data) write that to the database, while being able to view, 
update and delete fighters from the database. 

## Minimum Requirements
* Use a project management/tracking tool for user stories and MoSCoW prioritisation, such as trello or Jira.
* Design a relational database with a minimum of one relationship across two tables.
* Provide documentation.
* A functioning CRUD web application written in python that follows best programming practices learned in coursework
* Integration between VCS(version control system), CI server and cloud based VM so that code pushes are build automatically.

## Functionality
 The project I came up with was an MMA stats webapp that was user driven and kept upto date stats on all fighters. Users would be able to add fighters to the database, edit a fighters stats and delete a 
 fighter from the database in the event they retired. The plan was to also allow users to have a personal list of their favourite fighters but time constraints meant this found its way to the back of the 
 product backlog and planned to be implemented in the future. I chose an MMA stats website as I am a huge MMA fan, and follow all the organisations from UFC to ONE championship. I think my love started when
 my dad took me to a muay thai events as a teenager. 
 
 The min requirements from the brief where satisfied with the following user stories:
 * As a user I must be able to create and account with the following. First and last name, email address and password(which would be hashed for encryption).
 * As a user I must be able to CREATE one to many fighter entries. This creates the relationship between Users and Fighters using a one to many relationship.
 * As a user I must be able to READ all fighter entries.
 * As a user I must be able to UPDATE a fighters entry with up-to-date statistics.
 * As a user I must be able to DELETE a fighters entry in the event they retire. 
 
 Here are the screen grabs of my Trello board detailing all users stories following MoSCoW prioritisation.
 <a href="https://ibb.co/YQWsJnR"><img src="https://i.ibb.co/vqBnfyw/trello-board.png" alt="trello-board" border="0" /></a>

## Data 
Here is the entity relationship diagram outlining the fields in each table and the relationships between them.
<a href="https://ibb.co/TqgJwMf"><img src="https://i.ibb.co/G35GdQ6/project-ERD.png" alt="project-ERD" border="0" /></a>

Here you see the Users one to many relationship with Fighters where one user can add many fighters. You can also see the future functionality of the many to many relationship where users have many fighters 
in their favourites and fighters can belong to many users favourites.

## Tech Stack
* Project management/tracking: Trello.
* Database: GCP SQL Server using mySQL
* Backend: Python
* Frontend: Flask
* VCS: Github
* CI Server: Jenkins
* Run on Linux VM using GCP.

## CI Pipeline
<a href="https://ibb.co/SPYj8Sd"><img src="https://i.ibb.co/L8jFWKJ/CI-Pipeline.png" alt="CI-Pipeline" border="0" /></a>
* The web app is programmed in python and flask using pycharm.
* Changes are then pushed to the github repository where all changes are recorded and documented.
* After a successful change has been made and functionality met this is reflected in the Trello boards.
* When a push happens it triggers jenkins to build the live app again automatically so the changes are seen in the browser after a few moments.

## Front-end Design

Here you can see my initial wire frame design and thoughts about how I wanted the web app to look. The current build is underneath, as you can see the design isn't there yet but is planned for future iterations.
<a href="https://ibb.co/RczGFJD"><img src="https://i.ibb.co/sqypfXV/wireframe-screeny.png" alt="wireframe-screeny" border="0" /></a>
<a href="https://ibb.co/gZyMW5M"><img src="https://i.ibb.co/VYVWC7W/website-screen-grabs.png" alt="website-screen-grabs" border="0" /></a>
## Risk Assessment
<a href="https://ibb.co/w63vDQJ"><img src="https://i.ibb.co/C0Nrx9J/risk.png" alt="risk" border="0" /></a>

## Difficulties and Lessons Learned
The difficulties I faced completing the brief came mainly from technologies I hadn't used before. I hadn't used a VCS, linux or programmed in python before this project and new what I wanted to do but had to get over 
the barrier of learning how these technologies operated. Linux was difficult for me at teh beginning as I had no experience working with, after I started to grasp the ideas of it though I felt myself make real progress.

I had also never used Github before and that was a hurdle I had to get over, now I feel comfortable using it I can see the flexibility and robustness it adds to the software development process.

As with learning anything in the theory phase it can often be hard to conceptualise ideas such as the CI pipeline. Having now dipped my toe and seen through my project how the individual aspect of devops join together it 
has given me an deeper understanding and some context for the ideas learned in the coursework.

## Future Improvements
The improvements I will add to the website are going to include:
* Addition of User Favourites table and functionality allowing users to see their favourite fighters stats only.
* Search system to search for a fighter using their name.
* Filter system allowing for filtering of fighters based on weightclass, record etc.
* Addition of Gym table allowing users to see where fighters train and all fighters housed at specific gyms.

## Author
David McCartney 