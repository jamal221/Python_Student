import tkinter as tk
import turtle

def draw_pattern():
    shape_z = int(entry_sides.get())
    shape_num = int(entry_shapes.get())

    angle1 = 360 / shape_z
    angle2 = 360 / shape_num

    t1 = turtle.Turtle()
    t1.width(5)
    t1.speed(0)

    colors = ["red", "blue"]

    for i in range(shape_num):
        t1.color(colors[i % 2])
        for j in range(shape_z):
            t1.forward(100)
            t1.left(angle1)
        t1.left(angle2)

# ------------------- Tkinter Window ------------------- #
root = tk.Tk()
root.title("Shape Drawer")

tk.Label(root, text="Number of sides:").grid(row=0, column=0)
entry_sides = tk.Entry(root)
entry_sides.grid(row=0, column=1)

tk.Label(root, text="Number of shapes:").grid(row=1, column=0)
entry_shapes = tk.Entry(root)
entry_shapes.grid(row=1, column=1)

btn = tk.Button(root, text="Draw", command=draw_pattern)
btn.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
