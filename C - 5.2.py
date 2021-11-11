'''
5.2 Write a program that repeatedly prompts a user for integer numbers
until the user enters 'done'. Once 'done' is entered, print out the
largest and smallest of the numbers. If the user enters anything other
than a valid number catch it with a try/except and put out an
appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4
and match the output below.

l=[]
b=input()
if type(b)==int:
    l=b.split()
elif b=="Done":
    print(max(l))


'''

#by using while loop
largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        n = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None or largest < n:
        largest = n
    elif smallest is None or smallest > n:
        smallest = n
    elif n < smallest:
        smallest = n

print('Maximum is',largest)
print('Minimum is',smallest)