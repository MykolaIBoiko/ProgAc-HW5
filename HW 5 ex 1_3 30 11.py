#1.Lucky ticket
a = input('Enter 4 digit number:')
a=list(map(int, str(a)))
if sum(a[0:2]) == sum(a[2:5]):
    print('Lucky')
else:
    print('Not lucky')

#1.1 lucky ticket
a = input('Enter number:')
a = list(map(int, str(a)))
m = int(len(a) / 2)
if sum(a[m:]) == sum(a[:m]):
    print('Lucky ticket')
else:
    print('try again ;-)')

#2 Paliandrone
a=str(input('enter:'))
b = a[::-1]
print(b)
if a == b:
    print('Paliandrone')
else:
    print('Not paliandrone')


#2.1 Palindrome
a = list(input('Enter number or text:'))
m = int(len(a) / 2)
f = a[:m]
s = a[m:]
s.reverse()
if f == s:
    print('Palindrome')
else:
    print('Not palindrome')

#3. X&Y coordinate points for the circle with radius equals 4
x=float(input('Enter x point'))
y=float(input('Enter y point'))
r=4
if x**2+y**2 <= r**2:
    print('In the circle')
else:
    print('Out of the circle')