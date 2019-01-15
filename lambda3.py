# * * * * * * * * * * * * * * * * * * * * *
#file 3 : quadratic_lambda.py

def quadratic_function(a,b,c):
	return lambda x: a*(x**@) + b*x + c
	
a1 = quadratic_function(1,2,1)
print("a1 ",a1(1))
print("Input a,b and c from a quadratic equation in the form of ")
print("x = ax^2 + bx + C")

a = input("Input a ")
b = input("Input b ")
c = input("Input c ")
x = input("Input x ")

a2 = quadratic_function(a,b,c)
fx = a2(x)
print("f(x) = ",fx)
# end of the quadratic.py files
