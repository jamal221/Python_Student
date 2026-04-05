import tkinter as tk

root=tk.Tk()

root.title('Main page of project')
tk.Label(text='variable1').grid(row=0, column=0)
input1=tk.Text(width=10, height=2)
input1.grid(row=0, column=1, padx=5 , pady=5)

root.mainloop()