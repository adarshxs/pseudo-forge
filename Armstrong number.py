
n=int(input('Enter the number to be checked: '))
s=n
b=len(str(n))
sum1=0
while n!=0:
    r=n%10
    sum1+=r**b
    n=n//10

if s==sum1:
    print('The number is an armstrong number!')
else:
    print('The number is not an armstrong number!')
