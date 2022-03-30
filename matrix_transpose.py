X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

transpose_X = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

for i in range(len(X)):
    for j in range(len(X[0])):
        transpose_X[i][j] = X[j][i] 
        
print(transpose_X)
