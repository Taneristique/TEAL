import numpy as np
def mproduct(i:int,j:int)->np.matrix: 
    """This function creates two matrix and returns their product."""
    v=[]
    for _ in range(i):
         v+=[[float(input("give an integer or float to create matrix A\n")) for _ in range(j)]]
    A,v=np.matrix(v),[]
    for _ in range(j):
        v+=[[float(input("give an integer or float to create matrix B\n")) for _ in range(i)]]
    B=np.matrix(v)
    return print("A is \n",A,"\nB is \n",B,"\nC=A*B\n C is\n", A*B)
