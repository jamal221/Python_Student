class Rectangle:
    def __init__(self, width=0, height=0):
        self.width=width
        self.height=height
    def mohit(self):
        m=(self.width+self.height)*2
        return m
    def masaht(self):

        s=self.width*self.height
        return s
    def __str__(self):
        # return "Override the bultin function"
       
        return(f"the rectangle width is : {self.width} and the height is: {self.height}\n"+
        f"and mohit is: {self.mohit()}\n"+
        f" and masahat is: {self.masaht()}")
    def __len__(self):
        # print ("your shape is rectangle with 4 edges")
        return 4

    
    
    
    
 
# ایجاد نمونه از کلاس اصلی
w=int(input("please insert the width"))
h=int(input("please insert the height"))
rect1=Rectangle(w,h)
# print(rect1)
print(f"the rectangle has {len(rect1)} edges")

# print(f"the rectangle width is : {rect1.width} and the height is: {rect1.height}\n"+
#       f"and mohit is: {rect1.mohit()}\n"+
#       f" and masahat is: {rect1.masaht()}")