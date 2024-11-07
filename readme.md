To run the project:
1. Install docker
2. Change directory to the root file
3. Run the comand docker-compose up --build
4. Connect to http://localhost:8080

The project is created with a flask backend and a react front end.

Backend information:
The back end files are stored in the backend directory. This includes a dockerfile to set up the backend container.
The flask backend's main program is main.py and functions as the api that the frontend components interact with.
This api has three endpoints used in searching, recovering and deleting stored data.

Frontend information:
The front end files are stored in frontend directory. This includes a dockerfile to set up the frontend container.
The main program, app.jsx is located in the src folder and it imports the three main components that make up the frontend UI from the components subfolder.