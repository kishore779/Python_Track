from library.book import Book
from library.service import add_book, borrow_book, return_book, books
from library.validator import validate_book
from library.utils import display

book1 = Book(101, "Money matters", "kishore", 300, True)
book2 = Book(102,"MOneyyyyy", "Ace", 400, True)

print(validate_book(book1))
print(validate_book(book2))

add_book(book1)
add_book(book2)

print(borrow_book(book1))

display(books)

print(return_book(book1))

display(books)


