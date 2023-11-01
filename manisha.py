#find the are of the triangle =(s*(s-a)*(s-b)*(s-c)-1/2)
a=float(input('enter first side'))
b=float(input('enter second side'))
c=float(input('enter 3rd side'))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.1
print('the area of the triangele is %0.2f'%area)  