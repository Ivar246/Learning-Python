
def CheckPlindrome(str1):
    str2  = str1[::-1]
    if str2  == str1:
        return True
    else:
        return False


inputstr = input('Enter the string:> ')

if(CheckPlindrome(inputstr)):
    print(f"{inputstr} is palindrom.")
else: 
    print(f"{inputstr} is not a palindrom.")