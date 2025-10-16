import requests
from bs4 import BeautifulSoup
import re

# Dictionary to map emotions to IMDb URLs for Tamil movies
URLS = {
    "Drama": 'https://www.imdb.com/search/title/?title_type=feature&genres=drama&languages=ta',
    "Action": 'https://www.imdb.com/search/title/?title_type=feature&genres=action&languages=ta',
    "Comedy": 'https://www.imdb.com/search/title/?title_type=feature&genres=comedy&languages=ta',
    "Horror": 'https://www.imdb.com/search/title/?title_type=feature&genres=horror&languages=ta',
    "Crime": 'https://www.imdb.com/search/title/?title_type=feature&genres=crime&languages=ta',
}

def main(emotion):
    url = URLS.get(emotion)
    print("Fetching URL:", url)
    if not url:
        print("Invalid emotion. Please choose from: Drama, Action, Comedy, Horror, Crime")
        return []

    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP errors
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

    soup = BeautifulSoup(response.text, "lxml")

    # Extract movie titles
    titles = [a.get_text().strip() for a in soup.find_all('a', href=re.compile(r'/title/tt\d+/')) if a.get_text().strip()]
    return titles

# Driver Function
if __name__ == '__main__':
    emotion = input("Enter the genre (Drama, Action, Comedy, Horror, Crime): ").strip().capitalize()
    movie_titles = main(emotion)

    if not movie_titles:
        print("No Tamil movie titles found for the given genre.")
    else:
        max_titles = 14 if emotion in ["Drama", "Action", "Comedy", "Horror", "Crime"] else 12
        print(f"\nTamil {emotion} Movies:")
        for i, title in enumerate(movie_titles[:max_titles], 1):
            print(f"{i}. {title}")
