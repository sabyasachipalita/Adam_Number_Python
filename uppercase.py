n=input("enter character:")
upper_case=""
for char in n:
           if "a" <=char <="z":
                   upper_case+=chr(ord(char)-32)
            
           else:       
                   upper_case+=char
print("upper string",upper_case) 



#convert lower case letter in to upper case letter
m=input("enter lower case letter:")
upper_name=""
for char in m:
        if "a" <=char <="z":
                upper_name+=chr(ord(char)-32)
        else:
                upper_name+=char
print("upper name",upper_name)
              
                       

                   
                          
