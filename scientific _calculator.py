import math

def scientific_calculator():
    print("scientific calculator")
    print("1.sin 2.cos 3.tan 4.sqrt ")

    choice=int(input("enter the choice:"))
    num=float(input("enter the number:"))

    if choice == 1:
        result=math.sin(math.radians(num))
        print("results:",result)
    elif choice == 2:
        result=math.cos(math.radians(num))
        print("results:",result)
    elif choice == 3:
        result=math.tan(math.radians(num))
        print("results:",result)
    elif choice == 4:
        result=math.sqrt(num)
        print("results:",result)
    
    else:
        print("invalid choice")
scientific_calculator()
