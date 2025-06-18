import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "2b3e67bd9a5a447e877df3631b162ef8"
CLIENT_SECRET = "0399467ea186427daab32c7c54baf699"

# Initialize the spotify client

client_credential_manager = SpotifyClientCredentials