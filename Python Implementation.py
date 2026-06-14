def matrixMult(arr, i, j, M):
    if(i+1 == j): 
        M[i][j] = (f"M{i}", 0)
        return M[i][j]
    if(i+2 == j): 
        M[i][j] = f"(M{i}.M{i+1})",arr[i]*arr[i+1]*arr[i+2]
        return M[i][j]
    if(M[i][j][1]!=-1): 
        return M[i][j]

    result = float('inf')
    brackets = ""

    for k in range(i+1, j):
        left = matrixMult(arr, i, k, M)
        right = matrixMult(arr, k, j, M)
        temp = left[1] + right[1] + (arr[i]*arr[j]*arr[k])
        if(temp<result): 
            result = temp 
            brackets = f"({left[0]}.{right[0]})"
    
    M[i][j] = (brackets, result)
    return M[i][j]

def matrixDisplay(arr):
    n = len(arr)
    if(n==0):
        print(f"Your array is empty")
        return
    if(n==1):
        print(f"Your array only contains one element and the construction of a matrix from this is not possible")
        return
    M = [[("",-1) for i in range(n)] for j in range(n)]
    order, cost = matrixMult(arr, 0, n-1, M)
    print(f"Minimum Cost: {cost}\nOrder: {order}")
    print("Memoization Table: ")
    for i in range(n):
        print([M[i][j][1] for j in range(n)])

arr = [4,1,2,3]
matrixDisplay(arr)

