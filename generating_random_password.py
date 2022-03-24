import string
import random


lowchar = string.ascii_lowercase
digchar = string.digits

l = int(input('Lowercase? '))
d = int(input('digits? '))
lowalpha = random.sample(lowchar, l)
dignum = random.sample(digchar, d)

passnum = lowalpha+dignum
print(passnum)
random.shuffle(passnum)
print(passnum)
password = ''.join(passnum)
print(password)
