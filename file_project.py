# File managment
name="jamal"
family="azizbeygi"
f=open("D://project/Python/School/text_me.txt","a")
f.write(f"   my name is {name} and my family is {family}")
f.close()



f=open("D://project/Python/School/text_me2.txt","w")
f.write(f"   my name is {name}{family}")
f.close()

f2=f=open("D://project/Python/School/text_me.txt","r")
print(f2.read())


