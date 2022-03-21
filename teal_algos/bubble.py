import time
start=time.time()
def bubble(x):
    """Function takes list element x as parameter which is consist of numbers"""
    for i in range(len(x)-1): #number of the loops 
        for j in range(1,len(x)): #number of the comperations
            if x[j-1]>x[j]: #swap i[j] with i[j-1]
                chg=x[j]
                x[j]=x[j-1]
                x[j-1]=chg 
            if x[j-1]==x[j] or x[j-1]<x[j]: #do nothing if two elements are equal or first element little than second one.
                pass          
            print('step ',i+1 ,x)
bubble([29,32,4,11,2,3])
end=time.time()
print(f'Runtime of algorithm : {end-start}')