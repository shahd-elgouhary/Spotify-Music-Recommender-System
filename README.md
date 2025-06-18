# 🎵 Music Recommender System

This is a simple music recommender web app built using **Streamlit** and **Spotify API**. It suggests songs based on a selected track using a content-based recommendation approach.

## 🔍 Features

- Suggests 5 similar songs based on the selected track.
- Fetches song metadata and album covers from Spotify.
- Clean and interactive web interface with Streamlit.

## 🚀 Demo

You can try the deployed version of the app [here](#) *(Add Streamlit Cloud link once deployed)*.

## 🧠 How It Works

- The app loads a dataset of songs and uses pre-computed cosine similarity values.
- When a user selects a song, it recommends the top 5 similar tracks.
- Album cover images are fetched using the Spotify API.

## 📦 Dependencies

Make sure you have these Python libraries installed:

pip install streamlit spotipy pandas scikit-learn

## 🛠️ How to Run Locally

1. Clone the repository:
git clone https://github.com/YOUR_USERNAME/spotify-music-recommender-system.git
cd spotify-music-recommender-system

2. Install the required packages:
pip install -r requirements.txt
د
3. Run the app:
streamlit run app.py

## 📁 Files

- `app.py` – The main Streamlit app script.
- `spotify_millsongdata.csv` – The dataset of songs and lyrics.
- `df.pkl` – Pickled version of the dataset.
- `similarity.pkl` – Pickled cosine similarity matrix (must be generated).
- `README.md` – This file.

## 🔑 Spotify API Setup

To use the Spotify API, set up your credentials:

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Create an app to get your **Client ID** and **Client Secret**.
3. Replace the credentials in `app.py`:


CLIENT_ID = "your_client_id"
CLIENT_SECRET = "your_client_secret"

## ✨ Future Improvements
1. Improve recommendation logic (e.g., using lyrics similarity).
2. Add genre filtering.
3. Deploy to HuggingFace or Streamlit Cloud.

## 👩‍💻 Developed by
 Shahd Elgouhary
```python
