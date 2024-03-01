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
- როდესაც მომხმარებელს სთხოვენ შეიყვანოს თავისი არჩევანი მთავარ მენიუში, პროგრამა ამოწმებს, რომ მისი არჩევანი მოქმედი დიაპაზონის ფარგლებშია (1-4)

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

    def add_book(self):
        current_year = datetime.now().year # გამოვიყენებთ გამოცემის წელის ვალიდაციისთვის, რადგან თუ მომხმარებელი შეიყვანს წელს, რომელიც მეტია მიმდინარე წელზე, ის არ განიხილოს ვალიდურად
        
        # მოითხოვს შევიყვანოთ წიგნის სათაური
        while True:
            title = input("Enter the title of the book: ")
            # ამოწმებს არის თუ არა წიგნის სათაური ცარიელი
            if not title.strip():
                print("Title cannot be empty. Please try again.")
                continue

            # ამოწმებს უკვე არსებობს თუ არა წიგნი იგივე სათაურით
            existing_titles = [book.title.lower() for book in self._books]
            if title.lower() in existing_titles:
                print("A book with the same title already exists. Please try again.")
                continue
            
            # მოითხოვს შევიყვანოთ ავტორი
            while True:
                author = input("Enter the author of the book: ")
                # ამოწმებს არის თუ არა ავტორის ველი ცარიელი
                if not author.strip():
                    print("Author cannot be empty. Please try again.")
                    continue
                break
            
            # მოითხოვს შევიყვანოთ გამოცემის წელი
            while True:
                publication_year = input("Enter the publication year of the book: ")
                # ამოწმებს არის თუ არა გამოცემის წელი ცარიელი
                if not publication_year.strip():
                    print("Publication Year cannot be empty. Please try again.")
                    continue
                try:
                    # ამოწმებს არის თუ არა გამოცემის წელი int ტიპის
                    publication_year_int = int(publication_year)
                    # ამოწმებს აღემატება თუ არა გამოცემის წელი მიმდინარე წელს
                    if publication_year_int > current_year:
                        print("Invalid publication year. Please enter a year before the current year.")
                        continue
                    break
                except ValueError:
                    print("Invalid input for publication year. Please enter a valid year.")
                    continue

            # Book კლასის ობიექტის შექმნა და წიგნების სიაში დამატება
            book = Book(title, author, publication_year)
            self._books.append(book)
            print(f"Book '{title}' added successfully.")
            break
    
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

        # ახალი წიგნის დამატება
        if choice == "1":
            manager.add_book()

        # ყველა წიგნის ჩვენება
        elif choice == "2":
            manager.show_books()

        # წიგნის ძებნა სათაურის მიხედვით
        elif choice == "3":
            title = input("Enter the title of the book you want to search for: ")
            manager.search_book(title)

        # პროგრამიდან გამოსვლა
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

main()