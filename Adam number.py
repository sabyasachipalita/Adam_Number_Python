n=int(input("enter number"))                      
def reverse(n):
            s=str(n)
            r=s[::-1]
            return int(r)
x=n**2
y=reverse(n)**2
if(x==reverse(y)):
        print("adam number")
else:
        print("not adam number")        


                   
                          
