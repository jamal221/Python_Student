class book:
    def __init__(self, name='', outhor='', language='',pages=0):
        self.name=name
        self.outhor=outhor
        self.language=language
        self.pages=pages
    def __len__(self):
        return self.pages

    def __str__(self):
        return (
                f"The book name: {self.name} has {self.pages} pages\n"+
                f"And the outhor is {self.outhor} wich the origin language is: {self.language}"
                )

book1=book('book1','jamal','english',250)
book2=book('book2','aziz','persian',100)
book3=book('book3','kamal','kurdish',300)
# print(book1)

class library:
    def __init__(self, books):
        self.books=books
    def searchByBookName(self):
        bookName=input("please insert the book name to serach:  ")
        resultSearch=[]
        for book in self.books:
            if bookName==book.name:
                resultSearch.append(book)
        return resultSearch
    def addBookToLibrary(self):
        name=input("please insert the book name:  ")
        outhor=input("please insert the book outhor:  ")
        language=input("please insert the book language: ")
        pages= int(input("please insert the book pages:  "))
        newBook=book(name,outhor,language,pages)
        self.books.append(newBook)
        
          
lib = library([book1, book2, book3])
lib.addBookToLibrary()
result = lib.searchByBookName()
index=1
for b in result:
    print(f"{index}:  {b}\n")
    index+=1