
 # 🌍✨ **Wanderverse** ✨🌍  
**Submission for the [Google Photorealistic 3D Maps Challenge](https://google3dmaps.devpost.com)**

Welcome to **Wanderverse**, an immersive and Gemini-powered place guessing game that transforms the way you experience and explore the world. From iconic landmarks to hidden gems, Wanderverse combines the thrill of competition, the beauty of photorealistic 3D maps, and the power of AI to create an unforgettable journey.

🌐 **Deployed at:** [Play Now](https://harmanjit14.pythonanywhere.com/home)

---

## 🚀 **Project Overview**
**Wanderverse** uses the **Google Maps Platform's Photorealistic 3D Maps** and **Gemini AI** to provide an engaging and lifelike experience. Players navigate real-world locations in stunning 3D, using AI-generated clues to make accurate guesses and climb the leaderboard. Explore, compete, and discover the beauty of our world like never before!

---

## 🏗️ **Features & Tech Stack**

### 🌟 **Key Features:**
- **Stunning 3D Visuals:** Seamlessly explore lifelike locations using Google’s Photorealistic 3D Maps.
- **Smooth Animated Transitions:** With **flyCameraTo** and **flyCameraAround**, enjoy breathtaking visual animations that bring each scene to life.
- **Bounded Exploration:** Navigate within defined boundaries to search for clues and make your guesses.
- **AI-Powered Clue System:** Our AI, **Gemini**, generates dynamic hints tailored to your exploration, adding depth and challenge to the gameplay.
- **Competitive Play:** Rack up points based on guess accuracy and compete against other players for the highest score.

### 🛠️ **Tech Stack:**
- **Google Maps Platform Photorealistic 3D Maps** (via Maps JavaScript API)
- **AI Clue Generation** powered by **Gemini**
- **Django** for a robust and efficient backend framework
- **Python 3.10** to run everything

---

## 🎮 **How to Play**
1. Launch **Wanderverse** [here](https://harmanjit14.pythonanywhere.com/home).
2. Explore the provided 3D location using intuitive controls.
3. Use AI-generated clues to narrow down your guess.
4. Submit your answer and earn points based on accuracy.
5. Compete with friends and players around the world for the top spot on the leaderboard!

---

## 📝 **Why We Built This**
The world is filled with incredible places waiting to be discovered. We wanted to make exploration fun, interactive, and educational by combining the latest in mapping technology and artificial intelligence. By gamifying the experience, we hope to inspire a deeper appreciation for geography and make learning about our world both engaging and enjoyable.

---

## 🔧 How to Test **Wanderverse** (Step-by-Step)

Follow these easy steps to test **Wanderverse** on your computer!

---

### 1. **Get the Required Keys**
To set up **Wanderverse**, you will need two API keys:

#### a. **Google Maps Key**
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the **Maps JavaScript API** for your project.
4. Generate and copy the **API Key**.

#### b. **Gemini API Key**
1. Visit the [Gemini API documentation](https://gemini.google.com).
2. Follow the instructions to generate your **Gemini API Key**.
3. Save the key securely for later use.

---

### 2. **Install Python**
1. Check if Python is installed on your computer:
   - Open a command prompt or terminal and type:  
     ```bash
     python --version
     ```
   - If it shows a version number, Python is already installed.
2. If not, download Python from [python.org](https://www.python.org/downloads/).
3. Install Python, ensuring that the **Add Python to PATH** option is selected during installation.

---

### 3. **Download the Project Files**
1. Visit the [Wanderverse GitHub Repository](https://github.com/Harmanjit14/Wanderverse).
2. Clone the repository using Git:
   ```bash
   git clone https://github.com/Harmanjit14/Wanderverse.git
   ```
   OR
3. Download the repository as a ZIP file, then extract it to a folder on your computer.

---

### 4. **Open Command Prompt or Terminal**
1. Navigate to the folder where you cloned or extracted the project files.
2. Open a command prompt (Windows) or terminal (Mac/Linux) in that folder.

---

### 5. **Install Project Dependencies**
1. Install all required dependencies by running the following command:
   ```bash
   pip install -r requirements.txt
   ```
2. Ensure the installation completes without errors.

---

### 6. **Set Your API Keys**
1. Set the API keys as environment variables by typing the following commands (replace `YourGeminiAPIKey` and `YourGoogleMapsAPIKey` with your actual keys):
   ```bash
   export GCP_GEMINI_API_KEY="YourGeminiAPIKey"
   export GCP_MAPS_KEY="YourGoogleMapsAPIKey"
   ```
2. On Windows, use `set` instead of `export`:
   ```bash
   set GCP_GEMINI_API_KEY=YourGeminiAPIKey
   set GCP_MAPS_KEY=YourGoogleMapsAPIKey
   ```

---

### 7. **Set Up Database Migrations**
1. Apply database migrations by running the following commands:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

### 8. **Start the Game**
1. Start the development server by running:
   ```bash
   python manage.py runserver
   ```
2. This will launch the server locally and display the URL where the game can be accessed.

---

### 9. **Open the Game in Your Browser**
1. Open a web browser.
2. Go to the following URL:  
   `http://localhost:8000`

---

### Enjoy Testing **Wanderverse**!
Feel free to explore the application, test features, and report any issues or feedback. Have fun!

---

## 🌐 **Links & Resources**
- **Challenge Page:** [Google Photorealistic 3D Maps Challenge](https://google3dmaps.devpost.com)
- **Deployed Game:** [Play Now](https://harmanjit14.pythonanywhere.com/home)

---

## 🏆 **Join the Adventure**
Explore, guess, and compete in **Wanderverse**! Experience the world like never before, and let the games begin. Happy exploring! 🌍✨
