str1 = input('Enter the string:> ')

def CheckPlindrome(str1):
    for i in range(int(len(str1)/2)):
        if(str1[i] != str1[len(str1)-1-i]):
            return False;
    return True

if(CheckPlindrome(str1)):
    print(f"{str1} is palindrom.")
else: 
    print(f"{str1} is not a palindrom.")