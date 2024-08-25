# **Project Title:** Web Tic Tac Toe

**Project Overview:** The Web Tic Tac Toe project aims to create a browser-based game that allows users to play Tic Tac Toe against the computer or with other players in real-time. The game will be built using basic web development technologies like HTML, CSS, and JavaScript, with the option to utilize complex frameworks to enhance the development process. The project will also incorporate user data persistence, SOCKET.IO for multiplayer mode, and a mobile-friendly approach to ensure a seamless user experience.

**Project Objectives:**

1. Create a playable Tic Tac Toe game that can be played against the computer or with other players.
2. Implement user data persistence to store account information, wins, losses, and other relevant data.
3. Utilize SOCKET.IO to enable real-time multiplayer mode.
4. Develop a mobile-friendly front-end to ensure a responsive and user-friendly experience.
5. Implement a clean and organized directory structure.
6. Utilize version control systems to maintain a professional and collaborative development process.

**Team Members:**

- **Project Lead:** Engineer Green
    - Role: Oversees project progress, ensures timely delivery, and manages resources.
    - Reason: Green has experience in managing projects and ensuring timely delivery.
- **QA Engineer:** Engineer Mercy
    - Role: Tests the game platform, identifies bugs, and ensures quality assurance.
    - Reason: Mercy has experience in QA engineering and has worked on projects requiring thorough testing.
- **Back-end Developers:** 
	- Engr. Nebiyou Belaineh
	    - Role: Develops the back-end architecture, and database schema.
	    - Reason: Nebiyou Belaineh has expertise in backend development and has worked on similar projects.
	- Engineer Chymezy
		- Role: Develop the backend routing API and the console
		- Reason: John has blah blah bah has expertise in developing the backend routing API and has worked on similar projects.
- **Frontend Developer:** Engr. Mohamed Eladly
    - Role: Creates the user interface, implements real-time communication, and integrates with the backend.
    - Reason: Mohamed has experience in frontend development and has worked on projects requiring real-time communication.
- **UX/UI Designer:** Engr. Uzo 
    - Role: Designs the user interface, creates prototypes, and ensures a seamless user experience.
    - Reason: Uzo has expertise in UX/UI design and has worked on projects requiring user-centered design.

**How to Use and Install Guide for Web Tic Tac Toe**

**Prerequisites:**

- Node.js (version 14 or higher)
- Python (version 3.8 or higher)
- Flask (version 2.0 or higher)
- Flask-SQLAlchemy (version 2.5 or higher)
- SOCKET.IO (version 4.5 or higher)
- MongoDB (version 4.4 or higher)
- Git (version 2.30 or higher)

**Step 1: Clone the Repository**

1. Open a terminal or command prompt and navigate to the directory where you want to clone the repository.
2. Run the command `git clone https://github.com/x17-Green/WTTT-SE_FaceOff_Challenge.git` to clone the repository.
3. Navigate into the cloned repository by running `cd WTTT-SE_FaceOff_Challenge`.

**Step 2: Install Dependencies**

1. Run `npm install` to install the client-side dependencies.
2. Run `pip install -r requirements.txt` to install the server-side dependencies.

**Step 3: Set up the Database**

1. Create a new MongoDB database by running `mongo` in your terminal or command prompt.
2. Create a new collection by running `use WTTT-SE_FaceOff_Challenge` in the MongoDB shell.
3. Create a new user by running `db.createUser({ user: "your-username", pwd: "your-password", roles: ["readWrite"] })` in the MongoDB shell.

**Step 4: Configure the Server**

1. Create a new file called `config.py` in the `server` directory.
2. Add the following code to the `config.py` file:
```
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://your-username:your-password@localhost:27017/WTTT-SE_FaceOff_Challenge'
```

3. Replace `your-secret-key`, `your-username`, and `your-password` with your own values.

**Step 5: Run the Server**

1. Run `python app.py` to start the server.
2. Open a web browser and navigate to `http://localhost:5000` to access the game.

**Step 6: Run the Client**

1. Run `npm start` to start the client-side application.
2. Open a web browser and navigate to `http://localhost:3000` to access the game.

**Troubleshooting:**

- If you encounter any issues during the installation process, refer to the error messages for more information.
- If you encounter any issues while running the game, check the console logs for more information.

**Deployment:**

- To deploy the game to a production environment, refer to the deployment engineering tasks outlined in the README file.
- Make sure to update the `config.py` file with the production environment settings.

**Testing:**

- To run the tests, refer to the testing engineering tasks outlined in the README file.
- Make sure to update the `test_game_board.js` and `test_game_cell.js` files with the correct test cases.

By following these steps, you should be able to install and run the Web Tic Tac Toe game successfully. If you encounter any issues, refer to the troubleshooting section for more information.


**Technical Requirements:**

1. Front-end:
    - HTML5 for structuring the game interface
    - CSS3 for styling and layout
    - JavaScript for game logic and interactivity
2. Back-end:
    - Python as the server-side programming language
    - Flask as the micro web framework for handling requests and responses
    - Flask-SQLAlchemy as the ORM library for interacting with the database
3. Database:
    - MongoDB as the non relational database management system for storing user data
4. SOCKET.IO:
    - Utilize SOCKET.IO to enable real-time communication between clients and the server
5. Version Control:
    - Utilize Git as the version control system for maintaining a collaborative and professional development process
	    - Branches
		    - Main Branch - deployment branch - Engineer Green
		    - Staging Branch - development branch - Engineer Mercy
		    - Dev Branches
			    - Back End Branch - 
					- Engineer 1 Branch - Engineer Nebiyou
					- Engineer 2 Branch - Engineer Chymezy
			    - Front End Branch - 
				    - Engineer 3 Branch - Engineer Mohamed
				    - Engineer 4 Branch - Engineer Uzo
			    - 

**Project Timeline:**

The project will be completed within 4 weeks, with the following milestones:

Day 1: Planning and setup

- Define project scope and objectives
- Set up the development environment
- Create a GitHub repository and initialize the project structure

Day 2: Front-end development

- Design and implement the game interface using HTML, CSS, and JavaScript
- Implement game logic and interactivity
- Optional: Utilize a front-end scaffolding framework to enhance development efficiency

Day 3: Back-end development

- Design and implement the back-end API using Flask and Flask-SQLAlchemy
- Implement user data persistence using SQLite
- Optional: Utilize a back-end framework to enhance development efficiency

Day 4: SOCKET.IO implementation and testing

- Implement SOCKET.IO to enable real-time communication between clients and the server
- Test the multiplayer mode to ensure seamless gameplay
- Debug and refine the game to ensure a smooth user experience

**Submission Requirements:**

1. Submit the link to the GitHub repository with a well-written README on how to set it up locally.
2. Record and submit a video walkthrough of the project, demonstrating the game's features and functionality.
3. **Bonus:** Provide a link to the deployed website, showcasing the game in a live environment.

**Evaluation Criteria:**

The project will be evaluated based on the following criteria:

1. The project's usage of front-end scaffolding frameworks like Vite, Webpack, Parcel, or ESBuild.
2. The project's usage of back-end frameworks like Flask.
3. Utilization of DBMS for storing various user data like account information, wins, losses, etc.
4. Mobile-friendly approach to the front-end.
5. Cleanliness of directory structure.
6. Professionalism in using version control systems.

By following this project proposal, I aim to deliver a high-quality Web Tic Tac Toe game that meets the challenge requirements and showcases my skills in web development, SOCKET.IO, and version control.


**Engineering Tasks Outline:**

**Client-side Engineering Tasks:**

1. **Create Game Board Component**:
    - Create `GameBoard.js` component to render the game board.
    - Implement game logic to handle user interactions (e.g., clicking on cells).
    - Use CSS to style the game board.
2. **Create Game Cell Component**:
    - Create `GameCell.js` component to render individual game cells.
    - Implement logic to handle cell clicks and update game state.
3. **Implement Game Logic**:
    - Create `Game.js` model to manage game state and logic.
    - Implement game rules (e.g., winning conditions, drawing).
4. **Implement User Interface**:
    - Create `index.html` to render the game interface.
    - Use CSS to style the interface.
5. **Implement SOCKET.IO**:
    - Create `script.js` to handle SOCKET.IO connections and events.
    - Implement real-time communication between clients and server.

**Server-side Engineering Tasks:**

1. **Create Flask App**:
    - Create `app.py` to define the Flask app.
    - Configure Flask to use SQLite database.
2. **Define Database Models**:
    - Create `game.py` and `player.py` models to define database schema.
    - Use Flask-SQLAlchemy to interact with the database.
3. **Implement Game Routes**:
    - Create `game_routes.py` to define routes for game-related API endpoints.
    - Implement API endpoints to handle game creation, updating, and retrieval.
4. **Implement Player Routes**:
    - Create `player_routes.py` to define routes for player-related API endpoints.
    - Implement API endpoints to handle player creation, updating, and retrieval.
5. **Implement SOCKET.IO**:
    - Create `socketio.py` to handle SOCKET.IO connections and events.
    - Implement real-time communication between clients and server.

**Testing Engineering Tasks:**

1. **Client-side Testing**:
    - Create `test_game_board.js` and `test_game_cell.js` to test client-side components.
    - Use Jest or Mocha to write unit tests.
2. **Server-side Testing**:
    - Create `test_game_routes.py` and `test_player_routes.py` to test server-side API endpoints.
    - Use Pytest or Unittest to write unit tests.

**Deployment Engineering Tasks:**

1. **Create Deployment Script**:
    - Create `deploy.sh` script to automate deployment process.
    - Use Git to deploy the project to a remote repository.
2. **Configure Production Environment**:
    - Configure Flask app to use production environment settings.
    - Use a WSGI server (e.g., Gunicorn) to run the Flask app.

**Files and Descriptions:**

- `client/public/index.html`: The main HTML file for the client-side application.
- `client/public/style.css`: The CSS file for styling the client-side application.
- `client/public/script.js`: The JavaScript file for handling client-side logic and SOCKET.IO connections.
- `client/components/GameBoard.js`: The React component for rendering the game board.
- `client/components/GameCell.js`: The React component for rendering individual game cells.
- `client/models/Game.js`: The JavaScript model for managing game state and logic.
- `client/utils/constants.js`: The JavaScript file for defining constants used throughout the client-side application.
- `client/utils/helpers.js`: The JavaScript file for defining helper functions used throughout the client-side application.
- `server/app.py`: The Python file for defining the Flask app.
- `server/config.py`: The Python file for configuring Flask app settings.
- `server/models/game.py`: The Python file for defining the game model using Flask-SQLAlchemy.
- `server/models/player.py`: The Python file for defining the player model using Flask-SQLAlchemy.
- `server/routes/game_routes.py`: The Python file for defining routes for game-related API endpoints.
- `server/routes/player_routes.py`: The Python file for defining routes for player-related API endpoints.
- `server/socketio.py`: The Python file for handling SOCKET

