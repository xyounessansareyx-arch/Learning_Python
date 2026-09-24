# Let's see how Python's arithmetic works

a = 181
b = 23
c1 = a / b
print('c1 = ', c1)
c2 = a // b # this will do the devision but only returns the integer value of answer
print('c2 = ', c2)
c3 = a % b
print('c3 = ', c3)

x = 3
y = 4
z1 = x * y
print('z1 = ', z1)
z2 = x ** y
print('z2 = ', z2)

# Order of the operations
number = (3.1415 + 6.2831) // 4 + 3.1415 * 8.8541
print('Number = ', number)