def greatThenMedian(arr, check):
    '''
    Find a max element in the array that is greater than the median of the first "check" elements
    :param arr: an array of random numbers
    :param check: a number of first elements in the array to test
    :return: a max element in the array that is greater than the median of the first "check" elements, or None if no such element exists
    '''
    # Initialize the maximum element to the first element of the array
    max_element = arr[0]

    # Iterate over the first "check" elements of the array
    for i in range(check):
        # Update the maximum element if necessary
        if max_element < arr[i]:
            max_element = arr[i]

    # Check if the maximum element is greater than the median of the first "check" elements
    if max_element > median(arr[:check]):
        # Return the maximum element if it is greater than the median
        return max_element
    else:
        # Return None if no such element exists
        return None
      
      
