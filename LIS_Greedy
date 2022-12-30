def LIS_Greedy(arr):
    #Edge case : if the input array is empty ,
    # return an empty list
    if (len(arr)<0):
        return []

    #Initializing the result list to store the elemnts
    # of the longest increasing subsequence
    res=[arr[0]]

    #Initializing the counter to 0
    k=0

    #Iterating through the input array
    for i in range(1,len(arr)):

        #If the current elemnt is larger than the last elemnt
        # in the result list , append it
        if(arr[i]>res[k]):
            k+=1
            res.insert(k,arr[i])

     #Returing the result list and the length of the list
    return [res , len(res)]
