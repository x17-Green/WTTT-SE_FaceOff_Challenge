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