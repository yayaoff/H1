from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sc

lmd = 50
eps = 0.1
L = 1 + 4*lmd     # A verifier
MAX = 10


img = Image.open('son_goku.png')        # type: ignore
img_array = np.array(img)
if img_array.shape[-1] == 4:            # RGBA
    img_array = img_array[:, :, :3]     # Remove the alpha channel (keep only RGB)

# Split the image into Red, Green, and Blue channels
Y_1 = img_array[:, :, 0]         # Red matrix
Y_2 = img_array[:, :, 1]         # Green matrix
Y_3 = img_array[:, :, 2]         # Blue matrix
m,n = Y_1.shape

bounds_0 = np.full((m, n), 0)
bounds_1 = np.full((m, n), 255)

def gradient_f_l(X,Y_l):
    g = X - Y_l  # Gradient of the data fidelity term
    
    # Horizontal finite differences
    g[1:, :] += 2 * (X[1:, :] - X[:-1, :])  # Differences with the row below
    g[:-1, :] -= 2 * (X[1:, :] - X[:-1, :])  # Differences with the row above
    
    # Vertical finite differences
    g[:, 1:] += 2 * (X[:, 1:] - X[:, :-1])  # Differences with the column to the right
    g[:, :-1] -= 2 * (X[:, 1:] - X[:, :-1])  # Differences with the column to the left
    
    return g

# def gradient_f_l(X,Y_l):
    
#     X = X.astype(np.float32)               # Convert X to a higher precision type
#     Y_l = Y_l.astype(np.float32)           # Convert Y_l to a higher precision type
#     g = np.zeros((m,n))

#     for i in range(1,m):
#         for j in range(1,n):
#             if i>1 and j >1 and j<n-1 and i<m-1:
#                 g[i][j] += (2*(X[i][j]-X[i-1][j]) + 2*(X[i][j]-X[i][j-1]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))
#             elif i==1 and j>1 and j<n-1:
#                 g[i][j] += (2*(X[i][j]-X[i][j-1]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j])) 
#             elif i>1 and j==1 and i<m-1:
#                 g[i][j] += (2*(X[i][j]-X[i-1][j]) - 2*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))  
#             elif i==m-1 and j<n-1 and j>=1 :
#                 g[i][j] += (2*(X[i][j]-X[i-1][j]))
#             elif j==m-1 and i<m-1 and i>=1 :
#                 g[i][j] += (2*(X[i][j]-X[i][j-1]))
#             elif i==1 and j==1:
#                 g[i][j] += ((-2)*(X[i+1][j]-X[i][j]) - 2*(X[i][j+1]-X[i][j]))

#     g *= lmd
#     g += X-Y_l

#     return g

# def projection(Z):

#     Z_flat = Z.flatten()
#     f = lambda Y : np.sum((Y - Z_flat)**2)
#     Y_0 = Z_flat.copy()
#     result = sc.minimize(f,Y_0,bounds=bounds, method='BFGS')

#     return result.x.reshape((m,n))

def projected_gradient_method(Y_l):
    X_k = np.copy(Y_l)
    criterion = True
    it = 0
    while(criterion):
        g = gradient_f_l(X_k,Y_l)
        Z = X_k - g / L
        # X_next = projection(Z)
        X_next = np.clip(Z,bounds_0,bounds_1)
        G_L = np.linalg.norm(g/L,'fro')
        print(G_L)
        if G_L <= eps:
            criterion = False
        X_k = X_next
        it+=1
    return X_next

X_1_opt = projected_gradient_method(Y_1)
X_2_opt = projected_gradient_method(Y_2)
X_3_opt = projected_gradient_method(Y_3)
# print(X_1_opt)
# print(X_2_opt)
# print(X_3_opt)

rgb_image_array = np.stack([X_1_opt, X_2_opt, X_3_opt], axis=-1)
# Convert to uint8 to avoid the type error
rgb_image_array = rgb_image_array.astype(np.uint8)

# Convert back to an image and display
rgb_image = Image.fromarray(rgb_image_array)
rgb_image.show()