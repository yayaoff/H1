import numpy as np

m,n = 4,4

A = np.array([[2,3,4,5],[6,7,2,1],[1,5,8,9],[3,4,1,3]])

def gradient_f_l(X):
    
    X = X.astype(np.float32)  # Convert X to a higher precision type
    #Y_l = Y_l.astype(np.float32)  # Convert Y_l to a higher precision type
    g = np.zeros((m,n),dtype=np.float32)
    for i in range(1, m-1):
        for j in range(1, n-1):
            g[i, j] = 2 * ((X[i,j] - X[i+1,j]) + (X[i,j] - X[i,j+1])) \
                       - 2 * ((X[i-1,j] - X[i,j]) + (X[i,j-1] - X[i,j]))
    # for i in range(1,m):
    #     for j in range(1,n):
    #         if i>1 and j >1 and j<n-1 and i<m-1:
    #             g[i][j] += (2*(X[i][j]-X[i-1][j]) + 2*(X[i][j]-X[i][j-1]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))
    #         elif i==1 and j>1 and j<n-1:
    #             g[i][j] += (2*(X[i][j]-X[i][j-1]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j])) 
    #         elif i>1 and j==1 and i<m-1:
    #             g[i][j] += (2*(X[i][j]-X[i-1][j]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))  
    #         elif i==m-1 and j<n-1 and j>=1 :
    #             g[i][j] += (2*(X[i][j]-X[i-1][j]))
    #         elif j==m-1 and i<m-1 and i>=1 :
    #             g[i][j] += (2*(X[i][j]-X[i][j-1]))
    #         elif i==1 and j==1:
    #             g[i][j] += ((-2)*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))

    return g

g = gradient_f_l(A)
print(g)