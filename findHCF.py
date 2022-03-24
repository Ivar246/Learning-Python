a = int(input('Enter a >'))
b = int(input('Enter b >'))

def gcd(a,b):
    if b==0:
        return a
    elif a==0:
        return b
    else:
        c = a % b
        if c==0:
            return b
        else:
            a = b
            b = c
            return gcd(a,b)

result = gcd(a,b)
print(result)