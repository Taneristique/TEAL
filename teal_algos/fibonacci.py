import time
response=int(input("Which elementh of the fibonacci series would you want to return?(repond as integer!)\n"))
start = time.time_ns()
def f(x):
    """   
    This function gets an integer value x from user as parameter to return the xth elementh of fibonacci series.  
    """
    if x<=2:
        return 1
    else:
        fibo=f(x-2)+f(x-1)
        return fibo 
print(str(response)+" th element of the fibonacci series  is ",f(response),".\nCalculated by recursive functions.")
end = time.time_ns() 
print(f"Runtime of the program is {end - start},starting moment : {start},ending moment : {end} p_time:",time.process_time())
launch = time.time_ns() 
a,b=0,1
for i in range(response):
    c=a+b
    b=a 
    a=c
print(str(response)+" th element of the fibonacci series  is ",c,".\nCalculated by iteration.")
finish=time.time_ns() 
print(f"Runtime of the program is {finish-launch},starting moment:{launch},ending moment:{finish} p_time:",time.process_time())