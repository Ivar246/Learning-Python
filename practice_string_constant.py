import string

lowchar = string.ascii_lowercase
upchar = string.ascii_uppercase
letchar = string.ascii_letters
digchar = string.digits
hexadigits = string.hexdigits
octdigits = string.octdigits
punchar = string.punctuation
whitespace = string.whitespace
printable = string.printable

txt = input('Text : ')
error = False

for i in txt:
    if i in digchar:
        error = True
    else:
        continue

if error == True:
    print("oops, there is number..")
else:
    print("No number")