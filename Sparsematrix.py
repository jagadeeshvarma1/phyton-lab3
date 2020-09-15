sparseMatrix = [[0,0,2,0,42],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]] 

siz = 0
  
for i in range(4): 
    for j in range(5): 
        if (sparseMatrix[i][j] != 0): 
            siz += 1
  
rows, cols = (3, siz) 
compactMatrix = [[0 for i in range(cols)] for j in range(rows)] 
  
k = 0
for i in range(4): 
    for j in range(5): 
        if (sparseMatrix[i][j] != 0): 
            compactMatrix[0][k] = i 
            compactMatrix[1][k] = j 
            compactMatrix[2][k] = sparseMatrix[i][j] 
            k += 1
  
for i in compactMatrix: 
    print(i)
