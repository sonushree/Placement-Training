def smallest(a,b,c):
    
    if (a<b)and(a<c):
        mysmallest=a
    elif (b<a) and (b<c):
        mysmallest=b
    else:
        mysmallest=c
    print("Smallest numbe3r in function is %d"%(mysmallest,))
    return mysmallest
x = int(input("enter a:"))
y = int(input("enter b:"))
z = int(input("enter c:"))
print("the smallest number is %d "%(smallest(x,y,z)))
