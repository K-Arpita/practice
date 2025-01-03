# Task 6: Create a program for interactive web scraping.

# Objective: Fetch data from a website and  present it in a user-friendly way using a simple web scraping library.

import requests
from bs4 import BeautifulSoup

def fetch_and_display_data(url):
    """
    Fetches data from the given URL and displays it in a user-friendly format.

    Args:
        url (str): The URL of the website to scrape.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

   
        soup = BeautifulSoup(response.text, 'html.parser')

        headlines = soup.find_all(['h1', 'h2', 'h3'])  

        if not headlines:
            print("No headlines found on the website.")
            return

        print("\nHeadlines:")
        for idx, headline in enumerate(headlines, start=1):
            print(f"{idx}. {headline.get_text(strip=True)}")

    except requests.exceptions.MissingSchema:
        print("Invalid URL format. Please include http:// or https://")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """Main function to handle user interaction."""
    print("Welcome to the Interactive Web Scraper!")
    while True:
        url = input("Enter the URL of the website you want to scrape (or type 'exit' to quit): ").strip()

        if url.lower() == 'exit':
            print("Exiting the scraper. Goodbye!")
            break

        fetch_and_display_data(url)

if __name__ == "__main__":
    main()
