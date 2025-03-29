try :
    n1 , n2 = eval(input("enter two number seprated by comma"))
    result = n1/n2
    print(result)

except ZeroDivisionError  :
    print("here is zero division error")

except SyntaxError :
    print("Error is you did not enter numbers seprated by commas")

except :
    print("Wrong input")

else :
    print("no error")

finally :
    print("I will always print")