#list -> index start from 0 like that in arryy:element are kept inside big bracket
#.append()                ->add object in the last of the list
# .clear()                ->clear all the objectof the lsit
# .insert(index, object), ->insert object in the specified index of list
# .remove(object)         -> it takes exactly one argument 
# .pop(index)             ->remove the object of given index
#.sort()                  -> sort the list element in ascending order
#.reverse()               -> sort in reverse order
#len()                    ->this print the number of element of list     
#.copy()                  ->it copy the element in another list
#.count(element)          ->count the frequency (no of times of repeatition)

mark = [50, 20, 60, 80, 70, 63, 14]
print(mark)
print(mark[0:3])
print(mark[-3])
mark[1]= 100
print(mark)  

mark.remove(80)       #mark remove takes exactly one argument
print(mark)

mark.pop()       #->if we did not specified index in list then pop() remove last element of the list
print(mark)

mark.sort()
print(mark)

print(len(mark))

