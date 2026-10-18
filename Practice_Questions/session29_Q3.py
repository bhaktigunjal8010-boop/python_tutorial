class LibraryManager:
  def __init__(self):
    self.books =[]
    self.show_menu()

  def show_menu(self):
   choice = input("""
  1.Add Book
  2.Remove Book
  3.Show All books
  4.Exit
  choose your choice : """)
   if choice =="1":
    self.add_book()
   elif choice == "2":
    self.remove_book()
   elif choice == "3":
    self.show_books()
   elif choice == "4":
    print("Thankyou for visiting Library!")
   else:
    print("Invalid choice")

  def add_book(self):
    name = input("Enter Book Name to Add : ")
    self.books.append(name)
    print("Book Added sucessfully!")
    self.show_menu()

  
  def remove_book(self):
   name = input("Enter Book Name to Remove : ")

   if name in self.books:
    self.books.remove(name)
    print("Book Removed Sucessfully!")
   else:
    print("Book not found")
    self.show_menu()
  
  def show_books(self):
    if len(self.books) == 0:
      print("No Books Available")
    else:
      print("Books in Library : ")

      for book in self.books:
        print(book)

library = LibraryManager()          



