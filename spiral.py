#Задача вывести в консоль матрицу размерностью NxN заполненную числами по спирали.
#Размерность матрицы N вводится с клавиатуры.

N=int(input('Укажите размерность матрицы N\n'))
matrix=[[0]* N for i in range(N)]
m=int((N+1)/2)
s=1
for i in range(m): 
    for j1 in range(i,N-i): 
       matrix[i][j1] = s
       s=s+1
    for j2 in range(i+1,N-i): 
       matrix[j2][N-i-1] = s
       s=s+1
    for j3 in range(N-i-2,i,-1): 
       matrix[N-i-1][j3] = s
       s=s+1
    for j4 in range(N-i-1,i,-1): 
       matrix[j4][i] = s
       s=s+1
       

def printMatrix ( matrix ): 
   for i in range ( len(matrix) ): 
      for j in range ( len(matrix[i]) ): 
          print ( "{:4d}".format(matrix[i][j]), end = "" ) 
      print ()

printMatrix ( matrix )
