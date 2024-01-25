import numpy as np 

J_x = 10
J_y = 10

def s(i,j):
    if j == -1:
        return i
    elif j == J_y + 1:
        (J_x + 1) + (J_x + 3)*(J_y + 1) + i
    else:
        return (J_x + 1) + i + (J_x + 3)*j
    
def f_test(x,y):
    return x**2 + y**2
    
def create_F_array(f):
    F = np.zeros(((J_x + 1)*(J_y + 1) + 2*(J_x + J_y + 2),1))
    for i in range(J_x + 1):
        for j in range(J_y + 1):
            F[s(i,j)] = f(i,j)
    return F

A = np.zeros((J_x + 1)*(J_y + 1) + 2*(J_x + J_y + 2), (J_x + 1)*(J_y + 1) + 2*(J_x + J_y + 2))

def update_A_omega(A):
    for i in range(J_x + 1):
        for j in range(J_y + 1):
            A[s(i,j),s(i,j)] = 4
            A[s(i,j),s(i,j-1)] = -1
            A[s(i,j),s(i,j+1)] = -1
            A[s(i,j),s(i-1,j)] = -1
            A[s(i,j),s(i+1,j)] = -1
    return A

    