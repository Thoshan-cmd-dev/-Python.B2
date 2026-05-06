name= input ("name:")
DOB= input ("DOB:")
regno= input ("regno:")
dep= input ("dep:")

m1= int(input("m1:"))
m2= int(input("m2:"))
m3= int(input("m3:"))
m4= int(input("m4:"))
m5= int(input("m5:"))
total = m1+m2+m3+m4+m5
per = total/500*100
print("Name:", name )
print("DOB:", DOB )
print("Regno:", regno )
print("Department:", dep )
print("Total:", total )
print("Percentage:", per )
if per >=50:
    print("Result : pass" )
else: 
    print ("Result : Fail")    