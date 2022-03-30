import os


# file = open("ravi.txt", "w")
# text = input("Enter some line of text>")
# print(file.write(text))
# file.close()

# file = open('ravi.txt', 'r')
# print(file.read())
# file.close()

# file = open('ravi.txt', 'a')
# print(file.writelines(['ravi', '\nshrestha']))
# file.close()


# file = open('ravi.txt', 'r')
# for line in file:
#    print(file.readlines())
# file.close()
file = open('file.txt', 'x')

file_name= input('file_name > ')
if os.path.exists(file_name):
    os.remove(file_name)
else:
    print('file does not exist..')