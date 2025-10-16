# Tamil Movie Scraper

## Overview
This Python script fetches Tamil movie titles from IMDb based on a user-specified genre (Drama, Action, Comedy, Horror, or Crime). It uses web scraping techniques with the `requests` and `BeautifulSoup` libraries to extract movie titles from IMDb's search results.

## Features
- Supports five genres: Drama, Action, Comedy, Horror, and Crime.
- Fetches movie titles from IMDb's genre-specific search pages for Tamil movies.
- Limits the output to a maximum of 14 titles per genre (or 12 for invalid genres).
- Handles HTTP errors and invalid inputs gracefully.
- Uses a user-agent header to mimic a browser request for better compatibility with IMDb.

## Requirements
To run this script, you need the following Python libraries:
- `requests`: For making HTTP requests to fetch web pages.
- `beautifulsoup4`: For parsing HTML content and extracting movie titles.
- `re`: For regular expression matching to filter movie title links.

Install the required libraries using pip:
```bash
pip install -r requirements.txt
