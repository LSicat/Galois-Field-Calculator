import copy
a = raw_input("A(x):")
b = raw_input("B(x):")
p = raw_input("P(x):")

print "Choose your Operation"
print "1. A(x) + B(x)"
print "2. A(x) - B(x)"
print "3. A(x) x B(x)"
print "4. A(x) / B(x)"
print "1 for addition, 2 for subtraction, 3 for multiplication, 4 for division"

choice = raw_input()

operation = "+"
if choice == "1":
	operation = "+"
	print "You chose addition"
elif choice == "2":
	operation = "-"
	print "You chose subtraction"
elif choice == "3":
	operation = "x"
	print "You chose multiplication"
elif choice == "4":
	operation = "/"
	print "You chose division"
else:
	print "No operation was chosen. Default to addition"


a = [int(n) for n in a.split()]
b = [int(n) for n in b.split()]
p = [int(n) for n in p.split()]
m = len(p)

print 
print "Your Galois Field is: GF(2^" + str(m) + ")"


def inputcheck(a,b,m):
	for x in a:
		if x >= m:
			print "Coefficient can only have max of m-1"
			print "m: " + str(m)
			print "coefficient: " + str(x)
			return 0
	for x in b:
		if x >= m:
			print "Coefficient can only have max of m-1"
			print "m: " + str(m)
			print "coefficient: " + str(x)
			return 0
	return 1

def addition(a,b,p,sign):
	if sign == "+":
		print "Performing Addition:", a ,"+", b
	else:
		print "Performing Subtraction:", a ,"-", b
	c = ""
	if len(a) > len(b):
		temp = [0]*(len(a)-len(b))
		b = temp + b
	else:
		temp = [0]*(len(b)-len(a))
		a = temp + a
	print "XOR each coefficient from leftmost"
	for x in range(max(len(a),len(b))):
		print a[x], "^", b[x] , "=", a[x]^b[x]
		c += str(a[x]^b[x]) + " "
	print ""
	print "--------------------------------------------"
	print "Result of the Addition", c
	print "--------------------------------------------"

def bitaddition(a,b,p):
	print "Performing Addition ", a , "+", b
	if len(a) > len(b):
		temp = [0]*(len(a)-len(b))
		b = temp + b
	else:
		temp = [0]*(len(b)-len(a))
		a = temp + a
	for x in range(max(len(a),len(b))):
		a[x] = a[x]^b[x]
	print "Result of Addition: ", a
	return a


def multiplication(a,b,p):
	total = []
	print "Performing Multiplication: ", a, "x" ,b
	for x in range(len(b)):
		temp = []
		if b[(-x-1)] == 0:
			temp = [0]*(x+len(b))
		else:
			temp = [0]*x
			temp = a + temp

		total = bitaddition(total,temp,p)
	print "--------------------------------------------"
	print "Result of Multiplication (without modulo) is ", total
	print "--------------------------------------------"
	return modulo(total,p)

def modulo(a,p):

	while(len(a) >= len(p)):
		#print "Modulo"
		#print "a:", a
		#print "p:", p
		temp = p+[0]*(len(a)-len(p))
		

		a = bitaddition(a,temp,a)
		while(a[0] == 0 and len(a) > 1):
			a.pop(0)
	print "--------------------------------------------"
	print "We modulo the result and get", a
	print "--------------------------------------------"
	return a
		

def inverse(a,g):

	s = g
	v = []
	r = a
	u = [1]

	o = 0
	count = 7
	print "Table:", r, s, u, v, o
	while len(r) != 1:
		
		o = len(s) - len(r)
		
		if o < 0:

			temp = s
			s = r
			r = temp
			temp = v
			v = u
			u = temp
			o = -o


		rtemp = copy.copy(r) 
		utemp = copy.copy(u)
		
		if o > 0:
			for x in range(o):
				rtemp.append(0)
				utemp.append(0)
		else:
			pass

		s = bitaddition(s,rtemp,p)
		v = bitaddition(v,utemp,p)
		while(s[0] == 0 and len(s) > 1):
			s.pop(0)
		while(v[0] == 0 and len(v) > 1):
			v.pop(0)

		print "Table:", r, s, u, v, o
		return u



def division(a,b,p):
	print "Peforming Division", a, "/", b
	print "We get the inverse of", b
	b = inverse(b,p)
	c = multiplication(a,b,p)
	print "--------------------------------------------"
	print "Result of the Division is ", c
	print "--------------------------------------------"


	
	




if inputcheck(a,b,m):
	if operation == "+":
		addition(a,b,p,operation)
	if operation == "-":
		addition(a,b,p,operation)
	if operation == "x":
		multiplication(a,b,p)
	if operation == "/":
		division(a,b,p)
