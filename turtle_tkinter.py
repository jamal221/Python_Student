
import turtle
import tkinter as tk
# shape_z: تعداد ضلع
# shape_num: تعداد شکل
def draw_pattern():
    # clear()
    # Call or use Entry
    shape_z=int(shape_z_entry.get())
    shape_num=int(shape_num_entry.get())
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


# کد های tkinter
root=tk.Tk()

root.title("Make Shape based on edge and shape number")

tk.Label(root, text="Edge number:  ").grid(row=0, column=0, pady=10)
shape_z_entry=tk.Entry(root)
shape_z_entry.grid(row=0, column=1, pady=10)

tk.Label(root, text="Shape number:  ").grid(row=1, column=0, pady=10)
shape_num_entry=tk.Entry(root)
shape_num_entry.grid(row=1, column=1, pady=10)

btn=tk.Button(root, text="Drawing", command=draw_pattern)
btn.grid(row=2, column=1, pady=10)
root.mainloop()



