# Arcadia-Flight-Data
This is a responsive web app with phone and desktop view which shows in a table all arrival flights from the **Open Sky Api**. You can filter by airport and the duration from two different controls on the app. It has also a login which is needed in order to use the app and you can register for free.


## Backend

The backend part is an **API Rest** which is made of with flask rest python module which loads all data from the Open Sky Api and send it to the frontend web app. It has also an Api Key for security reasons in order to avoid not allowed connections.
- In order to use the endpoints manually you must specify a html header "api-key" with the api key provided on the backend folder:
	>```/exAir```  --> Returns name and ICAO of a set of airports on JSON format.
	
	>```/arrivals/\<airport\>/\<date\>``` --> Returns a JSON with formated data of the Open Sky Api of arrivals endpoint. You must specify the ICAO on of the airport "airport" and a date less or equal than today's date with this format '%d %B %Y'.


## Frontend

The web is also made with **Flask** and **Jinja2** templates in addition with css and javascript files to make all components and make the web responsive to all types of screens. It also provides a secure login with password encryption and a sqlite database for saving all data user.

The app lets the user to select an airport and a date in order to load all data from the Open Sky Api. Data retrieved is shown by a table with search, sorting and filtering which allows to search for specific data on the columns.

## Docker

There is a **Dockerfile** and a **docker-compose.yml** in order to port the app to a Docker container.

- To use this docker container, Docker ce and Docker compose must be installed on the local machine and then you can run this command on the app root folder.
	> If you are on the docker user:
	```docker-compose up```

	> If you are on local user:
	```sudo docker-compose up```
- When Docker finish install and start the services you can open your browser on port 80 of localhost to use the app: ```http://localhost```

## Local Run
If you do not have Docker on your computer you have to follow these steps:
> 1: Install Python3.9

> 2: Install modules of the frontend and backend with:<br/>
> ```pip3 install -r frontend/requirements.txt```<br/>
> ```pip3 install -r backend/requirements.txt```

> 3: Run the backend and frontend scripts:<br/>
> ```python3 backend/open_sky_apir.py```<br/>
> ```python3 frontend/arcadia_web.py```

The Api Rest starts on port 5005 in localhost: ```http://localhost:5005```<br/>
The App starts on port 80 broadcast and you can visit on localhost too: ```http://localhost```
