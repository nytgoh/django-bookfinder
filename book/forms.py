from django import forms

# To take in the search input from the user 
class BookForm(forms.Form):
    searchText = forms.CharField(label='Book Search', max_length=100)