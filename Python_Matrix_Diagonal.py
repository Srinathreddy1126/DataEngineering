primary_diagonal =0
secondary_diagonal =0
print("Enter no of rows and columns for a square matrix")
n= int(input())
if n<=1:
    print("Sorry, Matrix size should be greater than 1")
    exit()
matrix=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(int(input()))
    matrix.append(a)
print(matrix)

for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            primary_diagonal+=matrix[i][j]
        if ((i + j) == (n - 1)):
            print(i," I ",j," J ",n," N")
            secondary_diagonal += matrix[i][j]
         
print("Primary Diagonal:", primary_diagonal)
print("Secondary Diagonal:", secondary_diagonal)
            