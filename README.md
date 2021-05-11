# MLB VISION
### Video Demo:  <https://youtu.be/sQ686XkBYmg>
Welcome to MLB VISION! this web application allows users to upload whatever videos they want and save them as well whereas delete them.
##  Getting started
The web application was made with vs code and written with Python, css, html and SQL. After running flask in the terminal, users are taken to MLB VISION website, where he/ she can login or register themself.

New users start by registering a new account under "register" After filling in a unique email, first name, username, password, and confirming the password, then users are taken to the home. These values are immediately stored to the user table.

By clicking the logo (MLB VISION) in the top left corner to go to the Homepage. You'll see at first only this written "You haven't uploaded any videos yet" but when you uploaded from "Dashboard" you can see all the videos you uploaded. And you can watch them by clicking it. 

"Dashboard" allows users to upload videos from youtube by filling all information you are asked such as "video title, link of video and description " once you finished to fill it, you'll see a table with the information you just added. You'll also be able to edit or delete the videos. 

## Folders
* static: where is stored images and css file 
* templates: where is stored all html files
*  __init__.py: Python file where are imported various app folders to direct commands requesting access to different html pages. Depending on the html page summoned, "homepage.py and views.pg" will return the page as well as different types of information stored from SQL database
* database.py: a python filewhere is stored the two tables I created, User and Video using sqlalchemy
* forms.py: a python file which i used to create upload form
* homepage.py: Python file where are imported various routes  to direct commands requesting access to different html pages. Depending on the html page summoned such as login, register and logout
* views: Python file where are imported various routes to direct commands requesting access to different html pages. Depending on the html page summoned such as home, video, edit-video, dashboard, history and delete.
* app.py: python file to help to run smoothy the program
* README.md:  a markdown file introducing my web app
* requirements.txt: this file simply prescribes the packages on which this app will depend. 

## Things to improve
* allows the user to search the videos he downloaded
* allows to look the history
* put new functions such as add an immage on the video uploaded 


