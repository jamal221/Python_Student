import random
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from PIL import Image, ImageTk



class book:
    def __init__(self,name, outhor, langauge, pages, status):
        self.name=name
        self.outhor=outhor
        self.language=langauge
        self.pages=pages
        self.status=status
    def __str__(self):
        return(
            f"The book name: {self.name}\n"
            f"The book outhor: {self.outhor}\n"
            f"The book main Language:  {self.language}\n"
            f"The book pages:  {self.pages}\n"
            f"The Book status is: {self.status}"
        )




# print(book1)

class library:
    def __init__(self):
        self.books=[]
    def add_book(self,book):
        self.books.append(book)
    def make_book_random(self):
        ch=['a','b','c','d','e','f', 'A','B','C','D','E','F']
        lang=['Farsi', 'English', 'Kurdish','Turkish','Arabic']
        statusList=['old','new']
        # قرار: اسم کتاب 6 حرفی باشه
        # 2: نام نویسنده 8 حرفی باشه
        bookName=''
        outhorName=''
        for i in range(6):
            index=random.randint(0, len(ch)-1)
            bookName+=ch[index]
        for j in range(8):
            index=random.randint(0, len(ch)-1)
            outhorName+=ch[index]
        index=random.randint(0, len(lang)-1)
        langName=lang[index]
        bookPage=random.randint(10,500)
        bookStatus=statusList[random.randint(0,1)]
        book1=book(bookName,outhorName,langName,bookPage,bookStatus)
        return book1

    
    
    def search_by_name(self,name):
        result=[]
        for book in self.books:
            if book.name.lower()==name.lower():
                result.append(book)
        return result
    def search_by_pages(self,pages):
        result=[]
        for book in self.books:
            if book.pages>pages:
                result.append(book)
        return result
    def show_result_search(self, name):
        index=1
        res=self.search_by_name(name)
        if len(res)!=0:

            for i in range(len(res)):
                print(f"{index}:  \n")
                # The print below has been override
                print(res[i])
                index+=1
        else:
            print("Nothing is to show for the search result..")
    def show_result_search_indexes(self, name):
        index=0
        resIndex=[]
        for book in self.books:
            if name.lower()==book.name.lower():
                resIndex.append(index)
            index+=1
        return resIndex

    def show_result_search_by_pages(self, pages):
        index=1
        res=self.search_by_pages(pages)
        for i in range(len(res)):
            print(f"{index}:  \n")
            # The print below has been override
            print(res[i])
            index+=1
    def show_all_items(self):
        index=1
        res=self.books
        result=''
        if len(res)!=0:

            for i in range(len(res)):
                # result+=(f"{index}:  \n")
                print(f"{index}:  \n")
                # The print below has been override
                # result+=(res[i])
                print(res[i])
                index+=1
            # return result
            # resultLabel.configure(text=result)
        else:
            return "Nothing is to show for the search result.."
            # resultLabel.configure(text="Nothing is to show for the search result..")

    def delBook(self, listIndex):
        for index in sorted(listIndex, reverse=True):
            self.books.pop(index)

    def Delete_by_name(self):
        #1:  گرفتن اسم کتاب
        bookName=input('Please insert the book name to delete: ')
        #2:  مشاهده لیست کتاب بر اساس نام
        print('The result search is:  \n')
        self.show_result_search(bookName)
        #3:  پیدا کردن اندیکس از نام کااب داده شده
        resIndex=self.show_result_search_indexes(bookName)
        #4:  حذف ایتم با توجه به اندیسک پیدا شده
        self.delBook(resIndex)
        #5:  دوباره مل سیستم مشاهده بشه تا حذف تایید بشه
        print('The final list items are:  \n')
        self.show_all_items()
    def update_book_name(self):
        # گرفتن اسم کتاب
        bookName=input('Please insert the book name to update: ')
        # گرفتن اسم دوم کتاب
        bookName2=input('Please insert the book name to set in libraray: ')
        # گرفتن اندیکس کتاب ها
        resIndexes=self.show_result_search_indexes(bookName)
        # بروزرسانی اسم کتاب
        if len(resIndexes)==0:
            print("There is nothing to update in db:....")
        else:
            for index in resIndexes:
                self.books[index].name=bookName2
    def add_book_by_tkinter(self):
        try:
            # گرفتن مقادیر از فرم tkinter
            name=entry_name.get().strip()
            author=entry_author.get().strip()
            language=entry_language.get().strip()
            page=int(entry_pages.get().strip())
            bookStatus=selected_status.get()
            # ایجاد کلاس کتاب در کتابخانه
            book1=book(name,author,language,page,bookStatus)
            self.add_book(book1)
            messagebox.showinfo(title='success', message=f'The book {name}  added successfuly, .....')
            entry_name.delete(0, tk.END)
            entry_author.delete(0, tk.END)
            entry_language.delete(0, tk.END)
            entry_pages.delete(0, tk.END)
        except:
            messagebox.showerror(title='error in system', message='There is an error in your code...')
    def show_data_by_tkinter(self):
        dataWindow=tk.Toplevel(root)
        dataWindow.title('Show data...')
        
        table=ttk.Treeview(dataWindow,columns=("Name","Author","Language","Page", "Status"), show="headings")
        table.heading("Name", text="Name")
        table.heading("Author", text="Author")
        table.heading("Language", text="Language")
        table.heading("Page", text="Page")
        table.heading("Status", text="Status")


        table.column("Name", width=120)
        table.column("Author", width=120)
        table.column("Language", width=80)
        table.column("Page", width=60)
        table.column("Status", text=60)


        for book in self.books:
            table.insert("","end",values=(book.name, book.outhor, book.language, book.pages, book.status))

        table.pack(padx=2, pady=10, fill=tk.BOTH, expand=True)
    def make_random_by_btn_tkinter(self):
        dataWindowRandom=tk.Toplevel(root)
        dataWindowRandom.title('Show data...')

        tk.Label(dataWindowRandom, text="number make random item:").grid(row=0, column=0, pady=5)
        self.entry_random_number = tk.Entry(dataWindowRandom, width=30)
        self.entry_random_number.grid(row=0, column=1)

        btn_random=tk.Button(dataWindowRandom, text='Make RandomItems', command=self.get_random_and_make_items)
        btn_random.grid(row=2, column=0, pady=5)


    def get_random_and_make_items(self):
        # How to get entry_random_number and store in num
        num=int(self.entry_random_number.get())
        # messagebox.showinfo(title='show number..', message=num)
        num=int(self.entry_random_number.get())

        for i in range(num):
            newItem=self.make_book_random()
            self.add_book(newItem)
        messagebox.showinfo(title='number data added...', message=f"number {num} items added to Library, please show all of them")


lib1=library()
root=tk.Tk()
root.title('The Library class...')
root.geometry("800x600")

# Load and resize the image (PIL makes this easy)
img = Image.open("background.jpg")
img = img.resize((800, 600), Image.Resampling.LANCZOS)
bg = ImageTk.PhotoImage(img)

tk.Label(root, text='Book Name: ').grid(row=0, column=0, pady=5)
entry_name=tk.Entry(root, width=30)
entry_name.grid(row=0, column=1, pady=5)

tk.Label(root, text="Author:").grid(row=1, column=0, pady=5)
entry_author = tk.Entry(root, width=30)
entry_author.grid(row=1, column=1)

tk.Label(root, text="Language:").grid(row=2, column=0, pady=5)
entry_language = tk.Entry(root, width=30)
entry_language.grid(row=2, column=1)

tk.Label(root, text="Pages:").grid(row=3, column=0, pady=5)
entry_pages = tk.Entry(root, width=30)
entry_pages.grid(row=3, column=1)

selected_status = tk.StringVar(value="old")  # default selected

btn_old = tk.Radiobutton(root, text="Old",  variable=selected_status, value="old")
btn_old.grid(row=4, column=0)

btn_new = tk.Radiobutton(root, text="New",  variable=selected_status, value="new")
btn_new.grid(row=4, column=1)

btn_add=tk.Button(root, text='Add Book', command=lib1.add_book_by_tkinter)
btn_add.grid(row=5, column=0, pady=5)

btn_show=tk.Button(root, text='Show Books', command=lib1.show_data_by_tkinter)
btn_show.grid(row=6, column=1, pady=5)

btn_make_random=tk.Button(root, text='random Books', command=lib1.make_random_by_btn_tkinter)
btn_make_random.grid(row=7, column=0, pady=5)



root.mainloop()

# lib1.show_all_items()
        









