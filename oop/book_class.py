
class Book:
    def __init__(self, title: str, author: str, year: int):
        """Initialize a Book instance with title, author, and publication year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: Called when the object is about to be destroyed."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation that can recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
