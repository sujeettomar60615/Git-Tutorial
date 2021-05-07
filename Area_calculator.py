import shape

pi = 22/7
print("1. Circle")
print("2. Square")
print("3.Rectangle")
print("4.Parallelogram")
print("5.Ellipse")
print("6.Triangle")
print("7.Trapezium")
print("8.Cube")
print("9.Sphere")
print("choose Shape")
ch=int(input())
if ch==1: #All about Circle
    radius=int(input("Enter the value of radius:"))
    sur_area = pi * radius **2
    perimeter = pi * radius * 2
    print("Area of Circle is ",sur_area)
    print("Perimeter of Circle is ",perimeter)

elif ch==2: #All about Square
    side=int(input("Enter the value of side:"))     
    sur_area = side**2
    perimeter = 4 * side
    print("Area of Square is ",sur_area)
    print("Perimeter of Square is ",perimeter)

elif ch==3: #All about Rectangle
    length=int(input("enter the value of length:"))    
    breadth=int(input("enter the value of breadth:"))  
    sur_area = length * breadth
    perimeter = 2*(length+breadth)
    print("Area of Rectangle is ",sur_area)
    print("Perimeter of Rectangle is ",perimeter)

elif ch==4: #All about Parellelogram
    base=int(input("enter the value of base:"))    
    height=int(input("enter the value of height:"))  
    sur_area = base * height
    print("Area of Parellelogram is ",sur_area)

elif ch==5: #All about Ellipse
    radius1=int(input("enter the value of radius1:"))    
    radius2=int(input("enter the value of radius2:"))  
    sur_area = pi * radius1 * radius2
    print("Area of Ellipse is ",sur_area)
   
elif ch==6: #All about Triangle
    base=int(input("enter the value of base:"))    
    height=int(input("enter the value of height:"))  
    sur_area = 0.5 * base * height
    print("Area of Triangle is ",sur_area)

elif ch==7: #All about Trapezium
    base1=int(input("enter the value of base1:"))    
    base2=int(input("enter the value of base2:"))    
    height=int(input("enter the value of height:"))  
    sur_area = height * (base1 + base2) / 2
    print("Area of Trapezium is ",sur_area)

elif ch==8: #All about Cube
    side=int(input("Enter the value of side:"))     
    sur_area = 6 * side**2
    print("Area of Cube is ",sur_area)

elif ch==9: #All about Sphere
    radius=int(input("Enter the value of radius:"))
    sur_area = 4 * pi * radius **2
    print("Area of Sphere is ",sur_area)
  