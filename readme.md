# Tamil Movie Scraper

## Overview
This Python script fetches Tamil movie titles from IMDb based on a user-specified genre (Drama, Action, Comedy, Horror, or Crime). It uses web scraping techniques with the `requests` and `BeautifulSoup` libraries to extract movie titles from IMDb's search results.

## Features
- Supports five genres: Drama, Action, Comedy, Horror, and Crime.
- Fetches movie titles from IMDb's genre-specific search pages for Tamil movies.
- Limits the output to a maximum of 14 titles per genre (or 12 for invalid genres).
- Handles HTTP errors and invalid inputs gracefully.
- Uses a user-agent header to mimic a browser request for better compatibility with IMDb.
