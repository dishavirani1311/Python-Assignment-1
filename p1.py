'VARIABLES'

'1. Create variables to store name, age, and city and display them.'
name='Disha'
age=20
city='Surat'
print('Name:',name)
print('Age:',age)
print('City:',city)

print('   ')

'2. Swap the values of two variables.'
a=5
b=10
a,b=b,a
print('after swap a:',a)
print('after swap b:',b)

print('   ')

'3. Calculate the area of a rectangle using variables.'
legth=10
width=20
area=legth*width
print('the area of rectangle is :',area)

print('   ')

'4. Calculate simple interest using variables.'
amount=int(input("Enter amount:"))
interest=int(input("Enter rate of interest:"))
year=int(input("Enter total year:"))

si=(amount*interest*year)/100
ans=amount+si
print("Simple interest =",ans)


p=1000
r=5
n=2
si=(p*r*n)/100
print(si)

#5. Convert Celsius temperature to Fahrenheit.

c=25
f=(c*9/5)+32
print(f)
