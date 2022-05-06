#1(a)
str='Python is a case sensitive language'
print(len(str))

#1(b)
rev=str[::-1]
print(rev)

#1(c)
c=str[10:35]
print(c)

#1(d)
obj=str.replace('a case sensitive language','object oriented')
print(obj)

#1(e)
idx=str.index('a')
print(idx)

#1(f)
spc=str.replace(' ','')
print(spc)

#2
str="Hey,{name} Here! My SID is 2110{SID},I am from {dep} department and my CGPA is {CGPA}"
print(str.format(name='Pratham Sharma',SID='7031',dep='Mechanical Engineering',CGPA='9.9'))

#3
a=56
b=10
print("a&b:",a&b )
print("a|b:",a|b)
print("a^b",a^b)
print("a<<2:",a<<2,"\tb<<2:",b<<2)
print("a>>2:",a>>2,"tb>>2:",b>>4,end="\n")

#4
str=input("Enter the string:")
if 'name' in str:
  print("Yes")
else:
  print("No")

#5
def check_traingle(a,b,c):
    result = 'Form a traingle'
    sides = [a, b, c]
    for side in sides:
        if side >= sum([sides[i] for i in range(len(sides)) if i != sides.index(side)]):
            result = 'Does not form a triangle'
            break
        return result
a=int(input("First side length :"))
b=int(input("Second side length :"))
c=int(input("Third side length:"))
print(a, b, c, check_traingle(a, b, c))

#6
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
n=a^b
count=0
while n:
 n=n&(n-1)
 count=count+1
count
print("Required number of bits to be flipped:",count)
