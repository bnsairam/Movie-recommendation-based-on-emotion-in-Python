Tamil Movie Scraper

Overview

This Python script fetches Tamil movie titles from IMDb based on a user-specified genre (Drama, Action, Comedy, Horror, or Crime). It uses web scraping techniques with the requests and BeautifulSoup libraries to extract movie titles from IMDb's search results.

Features





Supports five genres: Drama, Action, Comedy, Horror, and Crime.



Fetches movie titles from IMDb's genre-specific search pages for Tamil movies.



Limits the output to a maximum of 14 titles per genre (or 12 for invalid genres).



Handles HTTP errors and invalid inputs gracefully.



Uses a user-agent header to mimic a browser request for better compatibility with IMDb.

Requirements

To run this script, you need the following Python libraries:





requests: For making HTTP requests to fetch web pages.



beautifulsoup4: For parsing HTML content and extracting movie titles.



re: For regular expression matching to filter movie title links.

Install the required libraries using pip:

pip install requests beautifulsoup4

Usage





Run the script: Execute the script in a Python environment:

python tamil_movie_scraper.py



Input a genre: When prompted, enter one of the supported genres: Drama, Action, Comedy, Horror, or Crime. The input is case-insensitive.



Output: The script will display up to 14 Tamil movie titles for the specified genre, fetched from IMDb. If no titles are found or an error occurs, an appropriate message is displayed.

Example

Enter the genre (Drama, Action, Comedy, Horror, Crime): Comedy

Tamil Comedy Movies:
1. Vasool Raja MBBS
2. Panchatanthiram
3. Anbe Sivam
4. Michael Madana Kamarajan
...

Code Structure





URLS Dictionary: Maps genres to their corresponding IMDb search URLs for Tamil movies.



main(emotion): Core function that:





Retrieves the URL for the given genre.



Sends an HTTP GET request with a user-agent header.



Parses the HTML response using BeautifulSoup.



Extracts movie titles using a regular expression to match IMDb title links.



Returns a list of movie titles.



Driver Function: Prompts the user for a genre, calls main(), and prints up to 14 movie titles.

Error Handling





Invalid Genre: If the user enters an unsupported genre, the script prints an error message and returns an empty list.



HTTP Errors: If the IMDb request fails (e.g., network issues), the script catches the exception, prints an error message, and returns an empty list.



No Titles Found: If no movie titles are found for the given genre, a message is displayed.

Limitations





The script relies on IMDb's current HTML structure. Changes to IMDb's website may break the scraping logic.



It fetches only the first page of search results, which may not include all movies for a genre.



The script limits output to 14 titles to avoid overwhelming the user, but this can be adjusted by modifying the max_titles variable.

Future Improvements





Add pagination support to fetch more movie titles.



Include additional movie details (e.g., release year, rating).



Support more genres or languages.



Add error logging for debugging.



Implement caching to reduce repeated requests to IMDb.
