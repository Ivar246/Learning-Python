banks = [ 'NAB Bank', 'NAZ Bank', 'CWA Bank']

Principal = float(input('Enter principal: '))
interest = float(input('Enter rate of interesst: '))
period = float(input('Enter time period: '))

print("Available Bank: ")
index = 0
for bank in banks:
    index +=1 
    print(f'{index}. {bank}')

is_choice = False
while is_choice == False:
    choice = int(input("Please select the prefered bank index:  "))
    if choice >= 1 and choice <= 3:
        print('valid choice...')
        is_choice = True
        print(f'you have selected {banks[choice - 1]}')
    else: 
        print('invalid choice..\nPlease select the valid index..')

APY1 = (1+0.08/2)**2-1
APY2 = (1+0.08/4)**4-1
APY3 = (1+0.08/1)**1-1

if APY1 > APY2 and APY1 > APY3:
    FV = Principal * (1+APY1/2)**2
    print(f'APY1 : {APY1} and FV = {FV}')
elif APY2 > APY1 and APY2 > APY3:
    FV = Principal * (1+APY2/4)**4
    print(f'APY1 : {APY1} and FV = {FV}')
elif APY3 > APY2 and APY3 > APY1:
    FV = Principal * (1+APY3/1)**1
    print(f'APY1 : {APY1} and FV = {FV}')
