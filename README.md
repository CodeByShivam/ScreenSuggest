# 🎬 Movie Recommendation System

A personalized **Movie Recommendation System** built using **Python**, **Streamlit**, and the **TMDB API**.  
The system suggests movies based on user preferences using **Content-Based Filtering** and **Collaborative Filtering** techniques.

---

## 🚀 Features
- 🔍 **Search movies** and get detailed information (title, genre, overview, rating, etc.)  
- 🎯 **Personalized recommendations** based on user preferences  
- 🧠 **Machine Learning techniques** applied:
  - Content-Based Filtering (recommend movies with similar features like genre, cast, etc.)  
  - Collaborative Filtering (recommend movies based on user behavior patterns)  
- 🎨 **User-friendly Streamlit interface** with dynamic background image support  
- ⚡ **Real-time data fetching** from TMDB API  

---

## 🛠️ Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)  
- **Backend**: Python  
- **API**: [TMDB API](https://developer.themoviedb.org/)  
- **Libraries**:  
  - `pandas`, `numpy` → data processing  
  - `scikit-learn` → machine learning  
  - `requests` → API calls  

---

## 📂 Project Structure

📦 movie-recommendation-system
┣ 📂 data/ # Movie dataset (if applicable)
┣ 📂 images/ # Background or poster images
┣ 📜 app.py # Main Streamlit app
┣ 📜 recommender.py # Recommendation logic
┣ 📜 requirements.txt # Python dependencies
┣ 📜 README.md # Project documentation


---

## ⚙️ Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system

2. Create virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # for Linux/Mac
venv\Scripts\activate      # for Windows

3. Install dependencies

pip install -r requirements.txt

4. Get TMDB API Key

-> Create an account at TMDB

-> Navigate to Settings > API > Create API Key

-> Copy the key and add it in your code (config.py or directly in API calls)

5. Run the application

streamlit run app.py
