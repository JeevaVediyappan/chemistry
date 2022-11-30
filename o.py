
#Arithmetic Operators
x= 4
y= 5
print(x + y)

#Comparison Operators
print('x > y  is',x>y)

#Assignment Operators

print ("Line 1 - Value of num1 : ", x)
print ("Line 2 - Value of num2 : ", y)

#compound assignment operator

res = x + y
res += x
print ("Line 1 - Result of + is ", res)

#Logical Operators

a = True
b = False
print('a and b is',a and b)
print('a or b is',a or b)
print('not a is',not  a)

#Membership Operators

list = [1, 2, 3, 4, 5 ];
if ( x in list ):
   print("Line 1 - x is available in the given list")
else:
   print("Line 1 - x is not available in the given list")
if ( y not in list ):
   print("Line 2 - y is not available in the given list")
else:
   print("Line 2 - y is available in the given list")

#Identity Operators
if ( x is y ):
    print("x & y have SAME identity")
if ( x is not y ):
    print("x & y have DIFFERENT identity")

#Operator precedence
v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;  
print("Value of (v+w) * x/ y is ",  z)

# Control Statement

# While Loop
lines=['Hi','I am']
while True:
    l =input()
    if l:
       lines.append(l.upper())
       break;
       print(lines)
    else:
        break;
        print(lines)
print('looping completed')

# for loop

for l in lines:
    print(l)

# elif loop

month=input("Input the month (e.g. January, February etc.): ")
day=int(input("Input the day: "))
if month in('January','February','March'):
    season='winter'
elif month in('April','May','June'):
    season='spring'
elif month in('July','August','September'):
    season='summer'
else:
    season ='autumn'

if(month =='March')and(day >19):
    season='spring'
elif(month =='June')and(day >20):
    season='summer'
elif(month =='September')and(day >21):
    season='autumn'
elif(month =='December')and(day >22):
    season='winter'
print("Season is",season) 

#String operations

str1 = "Periyar University"
print(str1)
print(str1[0])

#String Slicing
print (str1[1:11:3]) #my_string [start:stop:step]

#String Concatenation 

str2 = "Computer Science"
strcon = str1 +'  '+ str2 + '.'
print(strcon)
x = 3 *"Hi!" #x=3*str1
print(x)
print(str1.capitalize())
print(str2.lower())   
print(str2.upper())
print(str1.title())
print(str1.swapcase())
print(str1.count('e'))
print(str2.find('c'))
print(str1.isalnum())
print(str2.isalpha())
print(str2.isdigit())    # all are string basic function

#strip()
str1.lstrip()
str2.rstrip()
str1.strip()
print(str2)

#join()
newstr = ' '.join(['We', 'are', 'Coders'])
print(newstr)

#split()

l = 'we are coders'.split()
l = 'we are coders'.split('e')
print(l)
