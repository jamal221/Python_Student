import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# -----------------------------
#  DATA MODEL CLASSES
# -----------------------------
class Book:
    def __init__(self, name, author, language, pages):
        self.name = name
        self.author = author
        self.language = language
        self.pages = pages

    def __str__(self):
        return (
            f"Book name: {self.name}\n"
            f"Author: {self.author}\n"
            f"Language: {self.language}\n"
            f"Pages: {self.pages}"
        )

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def get_all_books(self):
        """Return list of all Book objects."""
        return self.books


# ------------------------------------
#  Tkinter GUI Application
# ------------------------------------
lib1 = Library()

root = tk.Tk()
root.title("Library System")
root.geometry("400x300")

# --- Labels and Entry Fields ---
tk.Label(root, text="Book Name:").grid(row=0, column=0, pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Author:").grid(row=1, column=0, pady=5)
entry_author = tk.Entry(root, width=30)
entry_author.grid(row=1, column=1)

tk.Label(root, text="Language:").grid(row=2, column=0, pady=5)
entry_language = tk.Entry(root, width=30)
entry_language.grid(row=2, column=1)

tk.Label(root, text="Pages:").grid(row=3, column=0, pady=5)
entry_pages = tk.Entry(root, width=30)
entry_pages.grid(row=3, column=1)

# --- Functions (Commands) ---
def add_book_command():
    """Add a book from entry fields."""
    name = entry_name.get().strip()
    author = entry_author.get().strip()
    language = entry_language.get().strip()
    pages_text = entry_pages.get().strip()

    if not (name and author and language and pages_text):
        tk.messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        pages = int(pages_text)
    except ValueError:
        tk.messagebox.showerror("Error", "Pages must be a number.")
        return

    new_book = Book(name, author, language, pages)
    lib1.add_book(new_book)

    tk.messagebox.showinfo("Added", f'"{name}" added successfully!')
    entry_name.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_language.delete(0, tk.END)
    entry_pages.delete(0, tk.END)

def show_books_command():
    """Open a new window showing all books."""
    window = tk.Toplevel(root)
    window.title("All Books")
    window.geometry("500x300")

    # Treeview = Table-like widget
    tree = ttk.Treeview(window, columns=("Author", "Language", "Pages"), show="headings")
    tree.heading("Author", text="Author")
    tree.heading("Language", text="Language")
    tree.heading("Pages", text="Pages")

    tree.column("Author", width=150)
    tree.column("Language", width=100)
    tree.column("Pages", width=60)

    tree.pack(pady=10, fill=tk.BOTH, expand=True)

    # Fill rows
    for book in lib1.get_all_books():
        tree.insert("", tk.END, values=(book.author, book.language, book.pages), text=book.name)

    # Optional: show book name in first column
    tree["columns"] = ("Name", "Author", "Language", "Pages")
    tree.heading("Name", text="Name")
    tree.column("Name", width=150)

    # Clear and refill with correct format
    for child in tree.get_children():
        tree.delete(child)
    for book in lib1.get_all_books():
        tree.insert("", tk.END, values=(book.name, book.author, book.language, book.pages))


# --- Buttons ---
btn_add = tk.Button(root, text="Add Book", command=lib1.add_book)
btn_add.grid(row=4, column=0, pady=15)

btn_show = tk.Button(root, text="Show All Books", command=show_books_command)
btn_show.grid(row=4, column=1, pady=15)

root.mainloop()
