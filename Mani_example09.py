def isprime(n):
    if n<=1:
        #print('inside if function of isprime')
        return False
    for x in range(2,n):
        #print('in for loop')
        if n % x == 0:
            #print('inside second if loop')
            return False
        else:
            #print('in else loop')
            return True


n = 5

if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')
