from .book import Book

def validate_book(data : Book):
    if not data.author:
        return "Author name is empty"
    
    if not data.title:
        return "Book title needed"
    
    if data.price <= 0:
        return "Price should be in Positive"
    
    return "Book Valid"