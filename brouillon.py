    # for i in range(m):
    #     for j in range(n):
            # g[i][j] += X[i][j] - Y_l[i][j]
            # print(g[i][j])
            # print("i= ",i," j= ",j)
            # if i>2 and j >2 and j<n-1 and i<m-1:
            #     g[i][j] += lmd * (2*np.absolute(X[i][j]-X[i-1][j]) + 2*np.absolute(X[i][j]-X[i][j-1]) - 2*np.absolute(X[i+1][j]-X[i][j]) - 2*np.absolute(X[i][j+1]-X[i][j]))
            # elif i==2 and j>2 and j<n-1:
            #     g[i][j] += lmd * (2*np.absolute(X[i][j]-X[i][j-1]) - 2*np.absolute(X[i+1][j]-X[i][j]) - 2*np.absolute(X[i][j+1]-X[i][j])) 
            # elif i>2 and j==2 and i<m-1:
            #     g[i][j] += lmd * (2*np.absolute(X[i][j]-X[i-1][j]) - 2*np.absolute(X[i+1][j]-X[i][j]) - 2*np.absolute(X[i][j+1]-X[i][j]))  
            # elif i==m-1 and j<n-1 :
            #     g[i][j] += lmd * (2*np.absolute(X[i][j]-X[i-1][j]))
            # elif j==m-1 and i<m-1 :
            #     g[i][j] += lmd * (2*np.absolute(X[i][j]-X[i][j-1]))
            # elif i==2 and j==2:
            #     g[i][j] += lmd * ((-2)*np.absolute(X[i+1][j]-X[i][j]) - 2*np.absolute(X[i][j+1]-X[i][j]))
            # if i>2 and j >2 and j<n-1 and i<m-1:
            #     g[i][j] += lmd * (2*(X[i][j]-X[i-1][j]) + 2*(X[i][j]-X[i][j-1]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))
            # elif i==2 and j>2 and j<n-1:
            #     g[i][j] += lmd * (2*(X[i][j]-X[i][j-1]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j])) 
            # elif i>2 and j==2 and i<m-1:
            #     g[i][j] += lmd * (2*(X[i][j]-X[i-1][j]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))  
            # elif i==m-1 and j<n-1 :
            #     g[i][j] += lmd * (2*(X[i][j]-X[i-1][j]))
            # elif j==m-1 and i<m-1 :
            #     g[i][j] += lmd * (2*(X[i][j]-X[i][j-1]))
            # elif i==2 and j==2:
            #     g[i][j] += lmd * ((-2)*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))
                # Regularization term (Laplacian-like term)
    # for i in range(2, m-1):
    #     for j in range(2, n-1):
    #         g[i, j] += lmd * (2 * (X[i, j] - X[i-1, j]) +
    #                           2 * (X[i, j] - X[i, j-1]) -
    #                           2 * (X[i+1, j] - X[i, j]) -
    #                           2 * (X[i, j+1] - X[i, j]))

    # # Handling the boundaries explicitly
    # # Top row (i == 2)
    # for j in range(2, n-1):
    #     g[2, j] += lmd * (2 * (X[2, j] - X[2, j-1]) -
    #                       2 * (X[3, j] - X[2, j]) -
    #                       2 * (X[2, j+1] - X[2, j]))

    # # Left column (j == 2)
    # for i in range(2, m-1):
    #     g[i, 2] += lmd * (2 * (X[i, 2] - X[i-1, 2]) -
    #                       2 * (X[i+1, 2] - X[i, 2]) -
    #                       2 * (X[i, 3] - X[i, 2]))

    # # Bottom row (i == m-1)
    # for j in range(2, n-1):
    #     g[m-1, j] += lmd * 2 * (X[m-1, j] - X[m-2, j])

    # # Right column (j == n-1)
    # for i in range(2, m-1):
    #     g[i, n-1] += lmd * 2 * (X[i, n-1] - X[i, n-2])

    # # Corner case (i == 2, j == 2)
    # g[2, 2] += lmd * (-2 * (X[3, 2] - X[2, 2]) - 2 * (X[2, 3] - X[2, 2]))
        # Regularization term: Gradient of R(X)
    # for i in range(1, m-1):
    #     for j in range(1, n-1):
    #         g[i, j] += lmd * (2 * (X[i, j] - X[i-1, j]) +
    #                              2 * (X[i, j] - X[i, j-1]) -
    #                              2 * (X[i+1, j] - X[i, j]) -
    #                              2 * (X[i, j+1] - X[i, j]))
    
    # # Handle boundary conditions for top row, bottom row, left column, right column
    # # Top row (i = 1)
    # for j in range(1, n-1):
    #     g[1, j] += lmd * (2 * (X[1, j] - X[0, j]) -
    #                          2 * (X[2, j] - X[1, j]) -
    #                          2 * (X[1, j+1] - X[1, j]) +
    #                          2 * (X[1, j] - X[1, j-1]))
    
    # # Bottom row (i = m-2)
    # for j in range(1, n-1):
    #     g[m-2, j] += lmd * (2 * (X[m-2, j] - X[m-3, j]) -
    #                            2 * (X[m-1, j] - X[m-2, j]) -
    #                            2 * (X[m-2, j+1] - X[m-2, j]) +
    #                            2 * (X[m-2, j] - X[m-2, j-1]))

    # # Left column (j = 1)
    # for i in range(1, m-1):
    #     g[i, 1] += lmd * (2 * (X[i, 1] - X[i, 0]) -
    #                          2 * (X[i, 2] - X[i, 1]) -
    #                          2 * (X[i+1, 1] - X[i, 1]) +
    #                          2 * (X[i, 1] - X[i-1, 1]))

    # # Right column (j = n-2)
    # for i in range(1, m-1):
    #     g[i, n-2] += lmd * (2 * (X[i, n-2] - X[i, n-3]) -
    #                            2 * (X[i, n-1] - X[i, n-2]) -
    #                            2 * (X[i+1, n-2] - X[i, n-2]) +
    #                            2 * (X[i, n-2] - X[i-1, n-2]))


# def R(X):

#     diff_h = (X[1:, :] - X[:-1, :]) ** 2  # Differences between rows
#     diff_v = (X[:, 1:] - X[:, :-1]) ** 2  # Differences between columns

#     return np.sum(diff_h) + np.sum(diff_v)

# f_1 = lambda X : np.linalg.norm(X-Y_1)**2 + lmd * R(X)
# f_2 = lambda X : np.linalg.norm(X-Y_2)**2 + lmd * R(X)
# f_3 = lambda X : np.linalg.norm(X-Y_3)**2 + lmd * R(X)