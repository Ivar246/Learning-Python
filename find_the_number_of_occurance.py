def numberOfOccurance(list1, item):
    count = 0
    for data in list1:
        if data == item:
            count+=1
    print(count)


numlist = [1, 2, 3, 2, 4, 3, 4, 3, 5]
numberOfOccurance(numlist, 3)
