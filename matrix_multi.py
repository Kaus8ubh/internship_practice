##matix multiplication

R1 = int(input("Enter the number of rows"))
C1 = int(input("Enter the number of columns"))
arr1 = []
for i in range(R1):          
    a =[]
    for j in range(C1):      
         a.append(int(input()))
    arr1.append(a)

R2 = int(input("Enter the number of rows"))
C2 = int(input("Enter the number of columns"))
arr2 = []
for i in range(R2):          
    a =[]
    for j in range(C2):      
         a.append(int(input()))
    arr2.append(a)

if C1==R2:     ##condition for matrix multiplication
  result = [[0 for j in range(C2)] for i in range(R1)]
  for i in range(len(arr1)):
    for j in range(len(arr2[0])):
      for k in range(len(arr2)):
        result[i][j]+=arr1[i][k]*arr2[k][j]
  print(result)