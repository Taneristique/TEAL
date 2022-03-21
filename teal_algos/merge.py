import time
start=time.time()
def merge_sort(arr):
    if len(arr)>1:
        right_array=arr[len(arr)//2:]
        left_array=arr[:len(arr)//2]

        #recursion
        merge_sort(right_array)
        merge_sort(left_array)
        
        #merge 
        i=0 #right array index
        j=0 #left array index
        k=0 #merge index

        while i<len(right_array) and j<len(left_array):
            if left_array[j]<right_array[i]:
                arr[k]=left_array[j]
                j+=1
            else:
                arr[k]=right_array[i]
                i+=1
            k+=1
        while i<len(right_array):
            arr[k]=right_array[i]
            i+=1
            k+=1
        while j<len(left_array):
            arr[k]=left_array[j]
            j+=1
            k+=1
        print(arr)
    return arr
test=[29,32,4,11,2,3]
a=merge_sort(test)
print(a)
end=time.time()
print(f'Runtime of program : {end-start}')