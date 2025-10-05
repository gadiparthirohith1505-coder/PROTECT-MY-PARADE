Protect My Parade 🌦️
A dynamic, voice-enabled weather forecasting application that provides real-time rain probability to help you plan your outdoor events.

[Live Deployed Website URL https://protect-my-parade.vercel.app/] | [Link to YouTube Demo Video Here]

The Problem
Planning any outdoor event, from a local parade to a family picnic, is often overshadowed by a simple question: "Will it rain?" The sheer volume of available weather data can make getting a straightforward, reliable prediction for a specific future date a challenging task, leaving plans at the mercy of uncertainty.

Our Solution
Protect My Parade is our answer to this uncertainty. We have built a web application that uses live meteorological data to automatically analyze and forecast the probability of rain for any given location and date. The application's interface is not just informative but also immersive, with animated backgrounds that change to reflect the forecast, making the experience intuitive and engaging.

✨ Features:
AI-Powered Voice Control: Interact with the application hands-free. Simply ask for a forecast using natural language to get an instant vocal and visual response.

Clear Results: View a clear rain probability percentage and a straightforward message, removing all guesswork from your planning.

Dynamic Visual Feedback: The application’s background instantly transforms with animations that reflect the weather forecast (Sunny, Rainy, Cloudy, etc.).

Simple & Intuitive UI: A clean and accessible design that makes complex weather data easy to understand at a glance.

Trip Planner: Get suggestions on what to pack for your event based on the weather prediction.

Light/Dark Mode: Switch between themes for your viewing comfort.

🛠️ Tech Stack

Backend: Python, Flask

Frontend: HTML5, JavaScript, Tailwind CSS, DaisyUI

Collaboration: Git & GitHub

🚀 How to Run This Project Locally
Prerequisites
Python 3.8+

Node.js v16+

Git

1. Clone the Repository:
First, clone the project from GitHub to your local machine.

git clone https://github.com/your-username/your-repository-name.git

cd your-repository-name

2. Setup the Backend:
You will need one terminal for the backend.

Navigate to the backend folder

cd backend

Create a virtual environment

python -m venv venv
source venv/bin/activate
Note: On Windows, the activation command is venv\Scripts\activate

Install dependencies

pip install -r requirements.txt
Run the Flask server

python app.py

Your backend is now running on http://localhost:5000. Keep this terminal open.

3. Setup the Frontend:
You will need a second, separate terminal for the frontend.

Open a new terminal and navigate to the project's root folder again.

Run the Frontend with Live Server
The easiest way to run the index.html file is with the "Live Server" extension in VS Code.

Open the project folder in VS Code.

Right-click on the frontend/index.html file.

Select "Open with Live Server".

Your browser will open the application, and it will be able to communicate with your running backend.
