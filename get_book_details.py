from typing import Dict, Any
import requests
from bs4 import BeautifulSoup
from module.date_to_epoch import date_to_epoch

def get_book_details(book_link: str) -> Dict[str, Any]:
    response = requests.get(book_link)
    if response.status_code != 200:
        print(f"ERROR - Status code: {response.status_code} for URL: {book_link}")
        return {}
    
    content_html = response.text
    soup = BeautifulSoup(content_html, "html.parser")
    
    book_details = {
        "book_title": None,
        "book_rating": None,
        "book_ratings_number": None,
        "book_reviews_number": None,
        "book_pages_number": None,
        "book_publishing_date": None,
        "author": {
            "author_name": None,
            "author_written_books_number": None,
            "author_followers_number": None
        },
        "link": book_link
    }
    
    # Get book title
    book_title = soup.find("h1", class_="Text__title1")
    if book_title:
        book_details["book_title"] = book_title.text.strip()
    
    # Get book rating
    book_rating = soup.find("div", class_="RatingStatistics__rating")
    if book_rating:
        book_details["book_rating"] = float(book_rating.text.strip())
    
    # Get number of ratings
    book_ratings_number = soup.find("span", attrs={"data-testid": "ratingsCount"})
    if book_ratings_number:
        count_text = book_ratings_number.text.split()[0].replace(',', '')
        book_details["book_ratings_number"] = int(count_text)

    # Get number of reviews
    book_reviews_number = soup.find("span", attrs={"data-testid": "reviewsCount"})
    if book_reviews_number:
        reviews_text = book_reviews_number.text.split()[0].replace(',', '')
        book_details["book_reviews_number"] = int(reviews_text)

    # Get number of pages
    book_pages_number = soup.find("p", attrs={"data-testid": "pagesFormat"})
    if book_pages_number:
        try:
            pages_text = book_pages_number.text.split()[0]
            book_details["book_pages_number"] = int(pages_text)
        except:
            book_details["book_pages_number"] = -1

    # Get publishing date
    book_publishing_date = soup.find("p", attrs={"data-testid": "publicationInfo"})
    if book_publishing_date:
        book_details["book_publishing_date"] = date_to_epoch(' '.join(book_publishing_date.text.split()[2:]))
    
    # Get author name
    author_name = soup.find("span", class_="ContributorLink__name")
    if author_name:
        book_details["author"]["author_name"] = author_name.text.strip()

    # Get author's written books number
    author_written_books_number = soup.find("div", class_="FeaturedPerson__infoPrimary").find("span", class_="Text Text__body3 Text__subdued")
    if author_written_books_number:
        raw_written_books_number = author_written_books_number.text.split()[0]
        if ',' in raw_written_books_number:
            book_details["author"]["author_written_books_number"] = int(raw_written_books_number.replace(',', ''))
        elif 'k' in raw_written_books_number:
            book_details["author"]["author_written_books_number"] = float(raw_written_books_number[:-1]) * 1000
        else:
            book_details["author"]["author_written_books_number"] = int(raw_written_books_number)
    
    # Get author's followers number
    author_followers_number = soup.find("div", class_="FeaturedPerson__infoPrimary").find("span", class_="u-dot-before")
    if author_followers_number:
        raw_followers = author_followers_number.text.split()[0]
        if ',' in raw_followers:
            book_details["author"]["author_followers_number"] = int(raw_followers.replace(',', ''))
        elif 'k' in raw_followers:
            book_details["author"]["author_followers_number"] = float(raw_followers[:-1]) * 1000
        else:
            book_details["author"]["author_followers_number"] = int(raw_followers)
    
    return book_details 
