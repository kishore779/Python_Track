from .book import Book
books = []
def add_book(book : Book):

    books.append(book)
    return book

def borrow_book(book : Book):

    if book.available:
        book.available = False
        return "You can borrow it"
    
    return "Book not available"

def return_book(book : Book):
        if book.available:
             return "Book already returned"
        
        book.available = True
        return "Book returned successfully"