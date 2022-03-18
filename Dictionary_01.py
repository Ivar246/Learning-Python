myDict = {
    "Name" : "Ravi Shrestha",
    "age" : 22,
    "Mobile Number" : 965822,
    "email" : "ravistha869@gmail.com"
}
a = myDict["Name"]
b = len(myDict)            #this print the number of element inside the dictionray
print(a)
print(b)

print(myDict.get("age"))
print(myDict.get("email"))
