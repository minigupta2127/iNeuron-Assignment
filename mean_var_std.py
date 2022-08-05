
import numpy as np
def calculate(lst):
    if len(lst)!=9:
        raise ValueError("List must conatin 9 elements")
    arr=np.array([lst])
    #Conversion of list to 3*3 matrix
    arr_2d = np.reshape(arr, (3, 3))
    print(arr_2d)
        
    var1=np.var(arr_2d,axis=0)  
    var2=np.var(arr_2d,axis=1)
    var3=np.var(arr_2d)

    std1=np.std(arr_2d,axis=0)
    std2=np.std(arr_2d,axis=1)
    std3=np.std(arr_2d)
#print(std1,std2,std3)
    min1=np.min(arr_2d,axis=0)
    min2=np.min(arr_2d,axis=1)
    min3=np.min(arr_2d)

    max1=np.max(arr_2d,axis=0)
    max2=np.max(arr_2d,axis=1)
    max3=np.max(arr_2d)

    mean1=np.mean(arr_2d,axis=0)
    mean2=np.mean(arr_2d,axis=1)
    mean3=np.mean(arr_2d)

    sum1=np.sum(arr_2d,axis=0)
    sum2=np.sum(arr_2d,axis=1)
    sum3=np.sum(arr_2d)

    thisdict = {
        "Mean": [mean1.tolist(),mean2.tolist(),mean3],
        "Variance": [var1.tolist(),var2.tolist(),var3],
        "Standard Deviation": [std1.tolist(),std2.tolist(),std3],
        "Max":[max1.tolist(),max2.tolist(),max3],
        "Min":[min1.tolist(),min2.tolist(),min3],
        "Sum":[sum1.tolist(),sum2.tolist(),sum3]
        }
    

    
        
   
    
   
    return thisdict


lst=[int(i) for i in input("Enter the values separated by a space").split(" ")]
print(lst)
a=calculate(lst)
print(a)