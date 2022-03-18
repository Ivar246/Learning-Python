digits = input('Enter the digits > ')
digits_mapping = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four"
}
output = ""
for ch in digits:
    output +=digits_mapping.get(ch, '!') + " "
print(output)

