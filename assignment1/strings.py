var = 'Hello World!'
print ("var      --> ", var)
print ("var[0]   --> ", var[0])
print ("var[1:5] --> ", var[1:5])
print ("var[:-5] --> ", var[:-5])


var = 'Hello World!'
print ("String --> ", var)
print ("Length --> : ", len(var))
print ("Upper  --> : ", var.upper())
print ("Lower  --> : ", var.lower())

name=input("Enter your name: ")
age=int(input("Enter your age : "))
price=float(input("Enter the book price: "))
s="\nYour name is %s, age is %d and book price is %f" %(name.upper(),age,price)
print (s)

var =" Indian   Army    "

print("String    --> ", var)
print("Length    --> ", len(var))
print("var strip --> ", var.strip())
print("Length of var after strip --> ", len(var.strip()))


var =" Indian,   Army    "

print("String    --> ", var)
print("Length    --> ", len(var))
print("var split --> ", var.split())
print("var split --> ", var.split(' '))
print("var split --> ", var.split(','))

# Strip + Split
print("var split --> ", var.strip().split(','))


var="Indian Army"
print ("String    --> ", var)
print ("var[::1]  --> ", var[::1])
print ("var[::2]  --> ", var[::2])
print ("var[::-1] --> ", var[::-1])
print ("var[::-2] --> ", var[::-2])

var=var[::-1]
print ("var after reverse --> ", var)



s1="Indian Army"
s2="malayalam"
s3="madam"
s4="teacher"
print ("s1 --> ", s1==s1[::-1])
print ("s2 --> ", s2==s2[::-1])
print ("s3 --> ", s3==s3[::-1])
print ("s4 --> ", s4==s4[::-1])