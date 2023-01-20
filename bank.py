x=str(input("Enter the Account no. "))
y=len(x)
k=x.isnumeric()
if(12<=y<=16 and k== True):
    f=int(input("Enter the Account Balance Rs. "))
else:
    print("Your Account Number is incorrect")
    exit()
z=int(input("Enter the Total No. of employee you want to give salary, (Max 100)"))
if(0<z<=100):
    print("Salary of Manager is 50000 \nSalary of Developer is 40000 \nSalary of worker is 25000 ")
else:
        print("You are out of limit")
        exit()
a=int(input("Enter the No. of manager "))
b=int(input("Enter the No. of Developer "))
c=int(input("Enter the No. of Workers "))
if(a+b+c>100 or a+b+c!=z):
    print("You are out of limit")
    exit()
t=(50000*a)+(40000*b)+(25000*c)
print("Total amount you have given is Rs. "+str(t))
if(t>f):
    print("You don't have sufficient balance in your account ")
    d=t-f
    print("You have Rs. ",str(d),"less in your account")
else:
        
        l=f-t
        print("You have Rs. ",str(l),"left in your account")
        print("Salary will be credited to employees account")
    
