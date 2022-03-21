#This algorithm gives the sum of the rows and columns of any square matrix 
import numpy as np
def RowColSum(N:int): #creates a NxN matrix and calculates its row and col sums.
	B,C=[0 for _ in range(N)],[0 for _ in range(N)] 
	m_a=[] #an empty list to store matrix A's values 
	for i in range(N):
		m_a+=[[float(input("give an integer or float\n")) for _ in range(N)]] #list comprehension to get values for matrix A
	A=np.matrix(m_a) #create Matrix A with m_list
	for i in range(N): 
		for j in range(N): 
			B[i]+=A[i,j] #get rows' sum
			C[i]+=A[j,i] #get cols' sum 
	for i in range(N):
		print("Sum of rows : ",B[i],"\n Sum of columns : ",C[i])
