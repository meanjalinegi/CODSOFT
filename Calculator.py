import mymodule

Number1 = float(input("Enter First Number:"))
Number2 = float(input("Enter Second Number: "))
print("""Some of the Arithmetic operations are::
      1. Addition
      2. Difference
      3. Product
      4. Division
      5. Floor Division""")
while True:
    choice=int(input("Choose the operation you want to perform:)"))
    print("1. Addition"
          "2. Difference"
          "3. Product"
          "4. Division"
          "5. Floor Division")
    if choice ==1:
        mymodule.add(Number1,Number2)
    elif choice ==2:
        mymodule.diff(Number1,Number2)
    elif choice ==3:
        mymodule.mul(Number1,Number2)
    elif choice ==4:
        mymodule.div(Number1,Number2)
    elif choice ==5:
        mymodule.floordiv(Number1,Number2)
    else:
        print("Invalid input. please try again")
