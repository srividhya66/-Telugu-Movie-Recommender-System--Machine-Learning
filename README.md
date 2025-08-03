# 🎬 Telugu Movie Recommender System - Machine Learning

This is a simple and interactive movie recommendation system built using **Python**, **Pandas**, **Scikit-learn**, and **Streamlit**. It recommends similar Telugu movies based on content similarity (using title and overview metadata).

## 🔍 Features

- 📚 Content-based filtering using TF-IDF
- 🎞 Recommends similar Telugu movies
- 🚀 Streamlit web app UI
- 🧠 NLP-based similarity matrix creation
- ✅ Clean, minimal UI for demo purposes

## 📁 Project Structure

telugu-movie-recommender/
│
├── app.py # Streamlit UI
├── model.py # ML logic: data loading, similarity matrix, recommend()
├── data/ # Movie dataset (CSV)
│ └── telugu_movies.csv
├── requirements.txt # Required Python packages
└── README.md # You're here!

---

## ⚙️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/srividhya66/-Telugu-Movie-Recommender-System--Machine-Learning.git
cd telugu-movie-recommender
2. Install Dependencies
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv env
source env/bin/activate   # or use `env\Scripts\activate` on Windows
Install required packages:

bash
Copy
Edit
pip install -r requirements.txt
3. Run the App
bash
Copy
Edit
streamlit run app.py
Open http://localhost:8501 in your browser.

📊 Dataset Info
Format: CSV

Columns used: title, overview

You can add more columns for improved recommendations (genre, cast, etc.)

🧠 ML/NLP Techniques Used
TF-IDF Vectorizer: To convert movie overviews into feature vectors

Cosine Similarity: To compute similarity scores between movies

🛠 Future Improvements
Add genre/cast-based filtering

Use collaborative filtering for user-personalized results

Deploy on cloud (e.g., Streamlit Cloud, Heroku)

Add IMDb ratings integration

🧑‍💻 Author
Srividhya Badampudi

✨ GitHub: srividhya66

💼 LinkedIn: Sri Vidhya Badampudi



