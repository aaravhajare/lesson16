def age (age) :
    
    if age < 0 :
        raise ValueError ("Ony positive values are allowed")
    
    if age%2==0 :
        print("The age is even")

    else :
        print("age is odd")

try :
    n = int(input("enter your age"))
    age(n)

except ValueError :
    print("only positive values are allowed")

except :
    print("wrong input")