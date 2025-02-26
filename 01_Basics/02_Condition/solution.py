 #AGE GROUP CATEGROZATION

age = 60 
if age < 13 :
    print ("child")

elif age < 20 :
    print ("teenager")

elif age < 60 :
    print ("adult")
else :
    print ("senior")

 # MOVIE TICKETS PRICING

age = 17
day = "wednesday" or "tuesday"

price = 12 if age >= 18 else 8
if day == "tuesdy" or "wednesday":
    price -= 2

print ("Here is Your some special Disscount $",price)


# STUDENTS GRADE CALCULATOR

Marks = 50 

if Marks >= 90 :
    Grade = "A1"
elif Marks >= 80:
    Grade = "A+"
elif Marks >= 70:
    Grade = "A"
elif Marks >= 60:
    Grade = "b"
elif Marks >= 50:
    Grade = "c"
else :
    Grade = "Fail"

# STUDENTS GRADE MASSAGE

if Grade == "A1":
    print("exellent work shoaib")
elif Grade == "A+":
    print ("very Very Good Work Sohail")
elif Grade == "A":
    print("good work Ali")
elif Grade == "B":
    print("Do Hard Work")
elif Grade == "c" :
    print("Do More Hard Work")
else :
    print("Fail")