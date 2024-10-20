import numpy as np

lmd = 0.2
eps = 0.1
L = 1 + 4*lmd        # A verifier

m,n = 4,4
A = np.array([[1,35,90,53],[10,23,55,240],[41,32,5,163],[21,16,58,250]])

def gradient_f_l(X,Y_l):
    Y_l = Y_l.astype(np.float32)  # Convert Y_l to a higher precision type
    g = np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            if i>1 and j >1 and j<n-1 and i<m-1:
                print("1 : ", i,j)
                # print(X[i,j])
                g[i][j] += lmd * (2*(X[i][j]-X[i-1][j]) + 2*(X[i][j]-X[i][j-1]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))
            elif i==1 and j>1 and j<n-1:
                print("2 : ", i,j)
                g[i][j] += lmd * (2*(X[i][j]-X[i][j-1]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j])) 
            elif i>1 and j==1 and i<m-1:
                print("3 : ", i,j)
                g[i][j] += lmd * (2*(X[i][j]-X[i-1][j]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))  
            elif i==m-1 and j<n-1 and j>=1 :
                print("4 : ", i,j)
                g[i][j] += lmd * (2*(X[i][j]-X[i-1][j]))
            elif j==m-1 and i<m-1 and i>=1 :
                print("5 : ", i,j)
                g[i][j] += lmd * (2*(X[i][j]-X[i][j-1]))
            elif i==1 and j==1:
                print("6 : ", i,j)
                g[i][j] += lmd * ((-2)*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))
    return g

def projected_gradient_method(Y_l):
    # X_prev = np.zeros_like(Y_l,dtype=np.float32)
    X_prev = np.copy(Y_l)
    criterion = True
    while(criterion):
        g = gradient_f_l(X_prev,Y_l)
        print(g)
        nxt = X_prev - g / L
        X_next = np.clip(nxt,0.0,255.0)
        if (L*np.linalg.norm((X_prev-X_next))) <= eps:
            criterion = False
        X_prev = X_next
    return X_next

A_opt = projected_gradient_method(A)