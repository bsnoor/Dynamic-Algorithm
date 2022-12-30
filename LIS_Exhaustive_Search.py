def isSorted(arr):
    '''
    * Check if a list is sorted in increasing order
    :param arr: list to check
    :return: True if sorted in increasing order, False otherwise
    '''
    # Loop through each element in the list, starting from the second element
    for i in range(1, len(arr)):
        # If the previous element is greater than the current element, the list is not sorted in increasing order
        # so return False
        if arr[i - 1] > arr[i]:
            return False
    # If the loop completes without returning False, the list is sorted in increasing order, so return True
    return True
  
  
  
def allCombinations(X):
    '''
    * Find all subsequences in the sequence
	* Complexity: O(2^n), n=X.length()
    :param X: the sequence
    :return: list of all subsequences in the sequence
    '''
    # Get the length of the input list
    n = len(X)
    # Calculate the number of possible subsequences (2^n - 1, since the empty list is not considered a valid subsequence)
    count = int(pow(2, n)) - 1
    # Initialize a list to store the subsequences
    list_all = [] * count
    # Initialize a list of 0s with length n to use as a binary counter
    bin_list = [0] * n
    # Loop through all possible values of the binary counter
    for i in range(count):
        # Increment the binary counter
        plus1(bin_list)
        # Initialize a temporary list to store the current subsequence
        temp = []
        # Loop through each element in the input list
        for j in range(n):
            # If the binary counter has a 1 at the current index, add the corresponding element from the input list
            # to the temporary list
            if bin_list[j] == 1:
                temp.append(X[j])
        # Add the temporary list to the list of all subsequences
        list_all.insert
        
        
 def exhaustiveSearch(arr):
    '''
    * Solution 2.1 (First Version): The Full Search Algorithm - Exhaustive Search
    * Complexity: O(2^n*n)
    :param arr: number sequence
    :return: increasing sequence
    '''
    # Initialize variables to store the answer and the maximum length of an increasing subsequence found so far
    ans, max_len = "", 0

    # Generate all possible subsequences of the input list
    all_sublist = allCombinations(arr)

    # Loop through each subsequence
    for i in range(len(all_sublist)):
        # Get the length of the current subsequence
        len_ = len(all_sublist[i])
        # If the current subsequence is sorted in increasing order and its length is greater than the maximum length
        # found so far, update the maximum length and store the current subsequence as the answer
        if isSorted(all_sublist[i]) and len_ > max_len:
            max_len = len_
            ans = all_sublist[i]
    # Return the answer
    return ans





