a = int(input(">"))

if a > 1:
    for x in range(2, a):
        if a%x == 0:
            print(f"{a} is a prime number.")
        else: 
            print(f"{a} is not a prime number.")
else: 
    print("is not prime.")