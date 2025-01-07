##matix multiplication
arr1=[[23,48,92],[8,5,6]]
arr2=[[40,2],[60,4],[60,6]]
result=[[0,0],[0,0]]
for i in range(len(arr1)):
  for j in range(len(arr2[0])):
    for k in range(len(arr2)):
      result[i][j]+=arr1[i][k]*arr2[k][j]
print(result)