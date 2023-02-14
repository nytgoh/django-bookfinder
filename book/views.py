# takes a request -> response
# action or request handler

from django.shortcuts import render
from .forms import BookForm
from .models import Book

import requests


# Summary: Receives a search string and uses the google book REST api to find and
# display the top 10 books relevant to the search
def book_search(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            books = []
            results = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + form.cleaned_data["searchText"])
            for b in results.json()["items"]:
                volumeinfo = b["volumeInfo"]
                books.append(Book(title=volumeinfo["title"],
                                  description=volumeinfo["description"] if "description" in volumeinfo else "None Found",
                                  authors=", ".join(volumeinfo["authors"]) if "authors" in volumeinfo else "None Found",
                                  pub_date=volumeinfo["publishedDate"] if "publishedDate" in volumeinfo else "None Found",
                                  avg_rating=volumeinfo["averageRating"] if "averageRating" in volumeinfo else "None Found",
                                  rating_count=volumeinfo["ratingsCount"] if "ratingsCount" in volumeinfo else "None Found",
                                  ))
    else:
        form = BookForm()

    context = {
        'form': form,
        'totalItems': (results.json()["totalItems"] if 'results' in vars() or 'results' in globals() else ""),
        'books': (books if 'books' in vars() or 'books' in globals() else ""),
        'bookKeys': ["title", "description", "authors", "pub_date", "avg_rating", "rating_count"]
    }

    return render(request, 'booksearch.html', context)
