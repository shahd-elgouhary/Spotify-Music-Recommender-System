import pickle
import streamlit as st
import requests

@st.cache_data
def get_song_album_cover_url(song_name, artist_name):
    try:
        response = requests.get(
            "https://itunes.apple.com/search",
            params={
                "term": f"{song_name} {artist_name}",
                "media": "music",
                "entity": "song",
                "limit": 10
            }
        )
        results = response.json().get("results", [])

        if not results:
            return "https://i.imgur.com/8RKXAIV.jpg"

        # Try to find exact match first
        for result in results:
            track = result.get("trackName", "").lower()
            artist = result.get("artistName", "").lower()

            song_match = song_name.lower() in track or track in song_name.lower()
            artist_match = artist_name.lower() in artist or artist in artist_name.lower()

            if song_match and artist_match:
                return result["artworkUrl100"].replace("100x100", "500x500")

        # Try song name only if artist didn't match
        for result in results:
            track = result.get("trackName", "").lower()
            if song_name.lower() in track or track in song_name.lower():
                return result["artworkUrl100"].replace("100x100", "500x500")

        # Last resort: return first result
        return results[0]["artworkUrl100"].replace("100x100", "500x500")

    except Exception as e:
        print(f"Error for {song_name} - {artist_name}: {e}")
        return "https://i.imgur.com/8RKXAIV.jpg"


def recommend(song):
    index = music[music['song'] == song].index[0]
    distance = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_music_names = []
    recommended_music_posters = []

    for i in distance[1:6]:
        artist = music.iloc[i[0]].artist
        song_name = music.iloc[i[0]].song
        recommended_music_names.append(song_name)
        recommended_music_posters.append(get_song_album_cover_url(song_name, artist))

    return recommended_music_names, recommended_music_posters


# ── UI ──────────────────────────────────────────────────────────────────────
st.header('🎵 Music Recommender System')

music = pickle.load(open('df.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

selected_music = st.selectbox(
    "Type or select a song from the dropdown",
    music['song'].values
)

if st.button('Show Recommendation'):
    with st.spinner('Finding recommendations...'):
        recommended_music_names, recommended_music_posters = recommend(selected_music)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(recommended_music_names[i])
            st.image(recommended_music_posters[i])