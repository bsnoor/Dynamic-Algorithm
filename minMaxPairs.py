def minMaxPairs(arr):
    # Initialize variables for minimum and maximum values
    comparisons = 0
    maximum = arr[1] if arr[0] < arr[1] else arr[0]
    minimum = arr[0] if arr[0] < arr[1] else arr[1]

    # Iterate over pairs of elements in the array
    for i in range(2, len(arr) - 1, 2):
        comparisons += 1
        # Compare the elements in each pair and update minimum and maximum values as necessary
        if arr[i] < arr[i + 1]:
            comparisons += 2
            if arr[i] < minimum:
                minimum = arr[i]
            if arr[i + 1] > maximum:
                maximum = arr[i + 1]
        else:
            comparisons += 2
            if arr[i + 1] < minimum:
                minimum = arr[i + 1]
            if arr[i] > maximum:
                maximum = arr[i]

    # If number of elements is odd, check the last element
    if len(arr) % 2 != 0:
        comparisons += 1
        # Update minimum and maximum values if necessary
        if arr[len(arr) - 1] > maximum:
            maximum = arr[len(arr) - 1]
        else:
            comparisons += 1
            if arr[len(arr) - 1] < minimum:
                minimum = arr[len(arr) - 1]

    # Print and return results
    print("min= ", minimum, ", max =", maximum)
    return int(comparisons)
  
  
  
  def minMaxPairs(arr):
    if len(arr) == 0:
        return (None, None)
    elif len(arr) == 1:
        return (arr[0], arr[0])
    else:
        return (min(arr), max(arr))
