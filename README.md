## 🚀 Projet de Scraping - GOODREADS
# Description
Ce projet de scraping a pour objectif de collecter et d'analyser des données provenant de [https://www.goodreads.com/shelf/show/classics?page=1] afin de réaliser un projet en classe.

Projet réalisé en bînome avec Guillaume REDARES, ainsi que Matthieu Larboullet, intervenant et conducter de nos travaux.  

Les données extraites seront utilisées pour réaliser une analyse statistique sur les classiques de la littérature.

# 📋 Fonctionnalités principales
Extraction des données depuis [VS-Code, et Cursor].
Nettoyage et transformation des données pour obtenir un format structuré[JSON, HTML, CSS].
Stockage des données dans JSON.

# 🛠️ Technologies utilisées
Langage : Python
Librairies : BeautifulSoup4, times, requests
Librairy Envisagée : thread.pool 
Formats de stockage : CSV, JSON
et l'IA avec : claude 3.0, GTP4.o mini.

# 📦 Structure du projet
```py
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
 
        elif 'k' in raw_followers:
            book_details["author"]["author_followers_number"] = float(raw_followers[:-1]) * 1000
        else:
            book_details["author"]["author_followers_number"] = int(raw_followers)
    
    return book_details 
```

# ⚙️ Installation et utilisation
Prérequis
Python 3.x : Assurez-vous que Python est installé.
Modules requis : Installables via le terminal MAC OS.
Installation

# 🔍 Résultats attendus
Les données collectées seront disponibles dans le dossier data/processed au format JSON, puis convertis en CSV et pour finir en xlsx. 

# 🧪 Tests
Pour exécuter les tests :
```py
import requests
from module import (
    get_book_details,
    get_all_book_links,
    save_to_json
)

def main():
    all_books_data = [] 
    total_pages = 25

    # Save the data to a JSON file
    save_to_json(all_books_data, "goodreads_books.json")
    print(f"\nSaved data for {len(all_books_data)} books to goodreads_books.json")

if __name__ == "__main__":
    main() 
```
    
    
    


# 📦  Difficulté type rencontré
Pour exécuter les tests :
```py
def normalize_date(date_string: str) -> str :
    date_list = date_string.split()
    year = int(date_list[-1])
    date_list [-1] = f"{year:04d}"
    date_string = ' '.join(date_list)
    return date_string
```

Pour obtenir le résultat d'une date au bon format en tenant compte des années, c'est fonction c'est vue être spontnée mais à la fois essentiel. 

# 🛡️ Avertissement légal
L'utilisation de ce script doit respecter les conditions d'utilisation des sites web ciblés. Ce projet est destiné à des fins éducatives et ne doit pas être utilisé pour des pratiques non éthiques ou illégales.

Mon bînome et moi même rendons ce code libre de droit à tout usage. 

# 📧 Contact
Pour toute question ou suggestion, contactez-moi à sjomie@eugeniaschool.com.

Je remercie mon bînome Guillaume, et mMattheu LARBOULLET sans qui ce résultat n'aurait jamais pu être obtenu. 




