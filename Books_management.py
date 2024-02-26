'''
პროქტი შედგება ორი ძირითადი კლასისგან. 
Book კლასს აქვს ატრიბუტები სათაურის, ავტორისა და გამოცემის წლისთვის.
გააჩნია გეტერისა და სეტერის მეთოდები, როგორც თვისებები თითოეული ატრიბუტისთვის, რათა უზრუნველყოს ინკაფსულაცია.
BookManager კლასი მართავს წიგნების კოლექციას.
მას აქვს ახალი წიგნის დამატების, ყველა წიგნის ჩვენებისა და წიგნის სათაურის მიხედვით მოძებნის ფუნქციები.

ვალიდაციები:
- ახალი წიგნის დამატებისას პროგრამა ამოწმებს ცარიელია თუ არა სათაურის ველი
- ასევე უზრუნველყოფს, რომ ავტორის ველი ცარიელი არ იყოს.
- პროგრამა ამოწმებს გამოცემის წელიწადს, რათა დარწმუნდეს, რომ ის არის int ტიპის და არ არის მეტი მიმდინარე წელზე
- ახალი წიგნის დამატებამდე პროგრამა ამოწმებს, არის თუ არა სიაში წიგნი იგივე სათაურით

'''


from datetime import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self._title = title
        self._author = author
        self._publication_year = publication_year

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def publication_year(self):
        return self._publication_year

    @publication_year.setter
    def publication_year(self, value):
        self._publication_year = value

    def __str__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"


class BookManager:
    def __init__(self, default_books=None):
        self._books = []
        if default_books:
            self._books.extend(default_books)
    
    def add_book(self, title, author, publication_year):
        current_year = datetime.now().year # გამოვიყენებთ გამოცემის წელის ვალიდაციისთვის, რადგან თუ მომხმარებელი შეიყვანს წელს, რომელიც მეტია მიმდინარე წელზე, ის არ განიხილოს ვალიდურად
        
        # ამოწმებს არის თუ არა წიგნის სათაური ცარიელი
        if not title.strip():
            raise ValueError("Title cannot be empty.")
        
        # ამოწმებს უკვე არსებობს თუ არაა წიგნი იგივე სათაურით
        existing_titles = [book.title.lower() for book in self._books]
        if title.lower() in existing_titles:
            raise ValueError("A book with the same title already exists.")
        
        # არის თუ არა ავტორის ველი ცარიელი
        if not author.strip():
            raise ValueError("Author cannot be empty.")
                
        # ამოწმებს წიგნის გამოცემის წლის ვალიდურობას
        publication_year_int = int(publication_year)
        if publication_year_int > current_year:
            raise ValueError("Invalid publication year. Please enter a year before the current year.")
        
        # Book კლასის ობიექტის შექმნა და წიგნების სიაში დამატება
        book = Book(title, author, publication_year)
        self._books.append(book)
        print(f"Book '{title}' added successfully.")
    
    def show_books(self):
        if not self._books:
            print("No books in the list.")
        else:
            print("List of Books:")
            for i, book in enumerate(self._books, 1):
                print(f"{i}. {book}")

    def search_book(self, title):
        found_books = [book for book in self._books if book.title.lower() == title.lower()]
        if found_books:
            print(f"Book '{title}' found:")
            for book in found_books:
                print(book)
        else:
            print(f"Book '{title}' not found.")


def main():
    # შევქმნათ რამდენიმე ობიექტი Book კლასისთვის
    default_books = [
        Book("Norwegian Wood", "Haruki Murakami", "1987"),
        Book("One Hundred Years of Solitude", "Gabriel Garcia Marquez", "1967"),
        Book("Igi", "Jemal Karchkhadze", "1977")
    ]

    # შევქმნათ BookManager კლასის ობიექტი სადაც სიაში დამატებულია წინასწარ შექმნილი წიგნები
    manager = BookManager(default_books=default_books)

    while True:
        print("\nMenu:")
        print("1. Add a new book")
        print("2. View all books")
        print("3. Search for a book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # ახალი წიგნის დამატება
            while True:
                try:
                    title = input("Enter the title of the book: ")
                    author = input("Enter the author of the book: ")
                    publication_year = input("Enter the publication year of the book: ")
                    manager.add_book(title, author, publication_year)
                    break  
                except ValueError as e:
                    print(str(e))
        elif choice == "2":
            # ყველა წიგნის ჩვენება
            manager.show_books()

        elif choice == "3":
            # წიგნის ძებნა სათაურის მიხედვით
            title = input("Enter the title of the book you want to search for: ")
            manager.search_book(title)

        elif choice == "4":
            # პროგრამიდან გამოსვლა
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

main()