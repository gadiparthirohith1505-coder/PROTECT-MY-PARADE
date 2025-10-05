Protect My Parade 🌦️ A dynamic, voice-enabled weather forecasting application that provides real-time rain probability to help you plan your outdoor events.

[Live Deployed Website URL:https://protect-my-parade.vercel.app/] | [Link to YouTube Demo Video Here]

The Problem:

Planning an outdoor event, be it a parade, a picnic, or a party, always comes with a nagging uncertainty: "Will it rain?" Constantly checking different weather apps can be tedious, and they often don't provide a simple, clear probability for a specific future date, leaving you to guess. This makes it difficult to plan with confidence.

Our Solution:

Protect My Parade is our answer to this uncertainty. We have built a web application that uses live weather forecast data to provide a straightforward rain probability for any city on any given date. The application's interface is not just informative but also immersive, with animated backgrounds that change to reflect the forecast, making the experience intuitive and engaging.

Our AI Voice Assistant The application features a voice-enabled assistant that allows for hands-free interaction. Users can simply ask questions like, "What's the weather in Hyderabad tomorrow?" and receive a spoken response along with the updated visual forecast. This is powered by the browser's built-in Web Speech API for recognition and synthesis.

Live Data & Dynamic UI Our application connects to a real-time weather API (Open-Meteo) to fetch up-to-date forecast data. This data is then processed by our Python backend, which feeds the results to the frontend. The user interface responds instantly, updating the animated background, prediction text, and temperature, providing a rich and seamless user experience.

Features

🔮 AI-Powered Voice Control: Ask for the weather in any city for any date using natural language and get an instant vocal and visual response.

📍 Automatic & Manual Location: The app can automatically find your current location or you can search for any city in the world.

🗓️ Date-Specific Forecasts: Use the interactive calendar to select a specific date for your event and get a tailored rain forecast.

🎨 Dynamic Animated Backgrounds: The website's background comes to life with animations for sunny, cloudy, rainy, snowy, and nighttime conditions based on the forecast.

🧳 Trip Planner: Get suggestions on what to pack for your event based on the weather prediction.

🌓 Light/Dark Mode: Switch between themes for your viewing comfort.

Technology Stack

Backend: Python, Flask, Vercel Serverless Functions

Frontend: HTML5, JavaScript, Tailwind CSS, DaisyUI

Collaboration: Git & GitHub

How to Run This Project Locally
Prerequisites

Python 3.8+

Node.js v16+ (which includes npm)

Git

1. Clone the Repository
First, clone the project from GitHub to your local machine.

git clone https://github.com/gadiparthirohith1505-coder/PROTECT-MY-PARADE

cd PROTECT MY PARADE

2. Setup the Backend

Install Dependencies

This command will install Flask and other necessary Python packages for the backend.

pip install -r requirements.txt

3. Setup the Frontend

Install Vercel CLI

The frontend is served using the Vercel Command Line Tool, which creates a local environment that mirrors the final deployed website. If you don't have it, install it globally.

npm install -g vercel

(There are no other frontend dependencies to install.)

4. Run the Project

Run the Development Server

Use the vercel dev command from the main project folder. This single command starts both the frontend and the Python backend at the same time.

vercel dev

Your application will now be running and accessible at http://localhost:3000.

👥 Team Members

Rohith

Jithin

Dhanush

Karthik

Banu

Bhavani


