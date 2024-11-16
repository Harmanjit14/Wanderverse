# 🌍✨ **Wanderverse** ✨🌍  
**An immersive place-guessing game for the [Google Photorealistic 3D Maps Challenge](https://google3dmaps.devpost.com)**  

Welcome to **Wanderverse**, a Gemini-powered game that redefines exploration by blending competition, breathtaking 3D maps, and the power of AI. From iconic landmarks to hidden gems, **Wanderverse** delivers a thrilling, interactive journey.  

🌐 **Live Demo:** [Play Now](https://harmanjit14.pythonanywhere.com/home)  

---

## 🚀 **Overview**  
**Wanderverse** combines the **Google Maps Platform's Photorealistic 3D Maps** and **Gemini AI** to create a lifelike, engaging experience. Navigate real-world locations, solve AI-generated clues, and climb the leaderboard in this unique exploration game.  

---

## 🏗️ **Features & Tech Stack**  

### 🌟 **Key Features**  
- **Photorealistic 3D Maps:** Explore lifelike locations with Google Maps' cutting-edge visuals.  
- **Dynamic Animations:** Smooth transitions like **flyCameraTo** and **flyCameraAround** bring scenes to life.  
- **AI-Generated Clues:** Receive dynamic hints from **Gemini AI** to guide your guesses.  
- **Bounded Exploration:** Focus your search within defined areas for an immersive experience.  
- **Competitive Leaderboard:** Earn points based on guess accuracy and compete globally.  

### 🛠️ **Tech Stack**  
- **Google Maps Platform** (Photorealistic 3D Maps via Maps JavaScript API)  
- **Gemini AI** for clue generation  
- **Django Framework** for backend development  
- **Python 3.10** for implementation  

---

## 🎮 **How to Play**  
1. Visit the live demo: [Play Now](https://harmanjit14.pythonanywhere.com/home).  
2. Explore the 3D locations using intuitive controls.  
3. Solve AI-generated clues to guess the location.  
4. Submit your answer to earn points based on accuracy.  
5. Compete with players worldwide for the top leaderboard spot!  

---

## 📝 **Why Wanderverse?**  
The world is filled with incredible places waiting to be discovered. **Wanderverse** gamifies exploration, making it fun and educational by blending the latest mapping technology with artificial intelligence. We aim to inspire a deeper appreciation for geography and create an engaging learning experience for all.  

---

## 🔧 **Setup Guide**  

### 1. **Get API Keys**  
- **Google Maps API Key:** Follow this [Guide](https://console.cloud.google.com/).  
- **Gemini API Key:** Refer to the [Gemini API Documentation](https://gemini.google.com).  

### 2. **Install Python**  
Ensure Python 3.10 or later is installed. Download it [here](https://www.python.org/downloads/).  

### 3. **Clone the Repository**  
```shell
git clone https://github.com/Harmanjit14/Wanderverse.git
```

### 4. **Install Dependencies**  
Navigate to the project directory and install required dependencies:  
```shell
pip install -r requirements.txt
```

### 5. **Set Environment Variables**  
Set your API keys as environment variables:  
```shell
export GCP_GEMINI_API_KEY="YourGeminiAPIKey"
export GCP_MAPS_KEY="YourGoogleMapsAPIKey"
```
(For Windows, use `set` instead of `export`.)  

### 6. **Apply Migrations**  
Run the following commands to apply database migrations:  
```shell
python manage.py makemigrations
python manage.py migrate
```

### 7. **Start the Server**  
Launch the development server:  
```shell
python manage.py runserver
```

### 8. **Play the Game**  
Open your browser and visit:  
`http://localhost:8000`  

---

## 🌐 **Links & Resources**  
- **Devpost Challenge Page:** [Google Photorealistic 3D Maps Challenge](https://google3dmaps.devpost.com)  
- **Live Game Demo:** [Play Now](https://harmanjit14.pythonanywhere.com/home)  

---

## 🏆 **Join the Adventure**  
Rediscover the world with **Wanderverse**! Guess, compete, and explore lifelike 3D locations. Start your adventure today and experience the thrill of Wanderverse! 🌍✨  

---
