# Counting Positive Numbers
numbers = [1 , 2 , -3 , -4 , 5 , 6 , -7 , 8 , 9]
Positive_Number_Counts = 0
for num in numbers:
    if num > 0 :
        Positive_Number_Counts += 1

print("Final Number Counts" ,Positive_Number_Counts)

 #PASSWORD CHECKER

Password = input()
Password_length = len(Password)

if  len (Password) < 6 :
        strength = ("week") 
    
 
elif len(Password) <= 10 :
    strength = "Good"
else :
    strength ="strong"

print("this is", strength, "password try another  password" )

# RELOAD PASSWORD IF WEAK

while True :
    passwd = input()
    if len (passwd) >= 7:
        print ("strong password")
        break
    else  :
        print("try again")

