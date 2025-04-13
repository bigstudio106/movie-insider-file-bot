import os
import requests
from utils.verification import generate_verification_link, is_user_verified
from database.db_connection import db
from utils.logger import send_log  # Add logger

def handle_user_query(user_id, query):
    # Log the query
    await send_log(f"📥 Query from [{user.first_name}](tg://user?id={user.id}) (`{user.id}`): `{message.text}`")
    
    # Check if user is verified
    if not is_user_verified(user_id):
        verification_link = generate_verification_link(user_id)
        return f"Please verify your account by clicking on the link: {verification_link}"
    
    # Search for movie/series
    movie = search_movie_series(query)
    if movie:
        return display_movie_details(movie)
    else:
        return handle_error("Movie/Series not found.")

def search_movie_series(query):
    # External API or MongoDB search logic
    # Example: Search through external API or MongoDB
    return {"title": "Movie Example", "genre": "Action", "release_year": "2023"}  # Example response

def display_movie_details(movie):
    # Return formatted movie details
    return f"Title: {movie['title']}\nGenre: {movie['genre']}\nRelease Year: {movie['release_year']}"

def handle_error(error_message):
    return f"Error: {error_message}"
