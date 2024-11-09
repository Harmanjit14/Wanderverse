
 # 🌍✨ **Wanderverse** ✨🌍  
**Submission for the [Google Photorealistic 3D Maps Challenge](https://google3dmaps.devpost.com)**

Welcome to **Wanderverse**, an immersive and AI-powered place guessing game that transforms the way you experience and explore the world. From iconic landmarks to hidden gems, Wanderverse combines the thrill of competition, the beauty of photorealistic 3D maps, and the power of AI to create an unforgettable journey.

🌐 **Deployed at:** [Play Now](https://harmanjit14.pythonanywhere.com/home)

---

## 🚀 **Project Overview**
**Wanderverse** uses the **Google Maps Platform Photorealistic 3D Maps** to provide an engaging and lifelike experience. Players navigate real-world locations in stunning 3D, using AI-generated clues to make accurate guesses and climb the leaderboard. Explore, compete, and discover the beauty of our world like never before!

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

## 🔧 **Testing Instructions**
Follow these steps to set up and run **Wanderverse** on your local environment:

1. **Generate Gemini API Key and export it:**
   ```bash
   export GCP_GEMINI_API_KEY="GEMINI_KEY_EXAMPLE"
   export GCP_MAPS_KEY="GCP_MAPS_KEY_EXAMPLE"
   ```
2. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   ```
3. **Navigate to the Project Folder:**
   ```bash
   cd <folder-name>
   ```
4. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
5. **Set Up Database Migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

Visit `http://localhost:8000` in your browser to start exploring **Wanderverse** locally!

---

## 🌐 **Links & Resources**
- **Challenge Page:** [Google Photorealistic 3D Maps Challenge](https://google3dmaps.devpost.com)
- **Deployed Game:** [Play Now](https://harmanjit14.pythonanywhere.com/home)

---

## 🏆 **Join the Adventure**
Explore, guess, and compete in **Wanderverse**! Experience the world like never before, and let the games begin. Happy exploring! 🌍✨

---

Feel free to tweak the instructions based on your specific requirements or environment setup!