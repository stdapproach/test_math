
class Book:
    def __init__(self, authors: list, title: str, copyright: str, isbn: str):
        self.authors = authors
        self.title = title
        self.copyright = copyright
        self.isbn = isbn

    def __str__(self):
        return f"{self.authors[0]} '{self.title}'"

#container of books mentioned at tests for ode
books = {
    'Alan': Book(
        ["Alan, Jeffrey"], "Advanced Engineering Mathematics", "Copyright @ 2002 by HARCOURT/ACADEMIC PRESS", "0-12-382592-X"
    ),
}

# QQQ_Bird, John
# Higher Engineering Mathematics, Sixth Edition
# ISBN: 978-1-85-617767-2
