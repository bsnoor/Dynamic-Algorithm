def maxMaxDynamic(sequence):
    # Initialize the maximum element to the first element of the sequence
    max_element = sequence[0]

    # Initialize the second maximum element to the second element of the sequence
    second_max_element = sequence[1]

    # If the first element is greater than the second element, swap them
    if max_element < second_max_element:
        max_element, second_max_element = second_max_element, max_element

    # Create a matrix to store the maximum and second maximum elements at each step
    max_matrix = [[None] * 2 for _ in range(len(sequence))]
    max_matrix[0] = max_element, second_max_element

    # Iterate over the elements of the sequence
    for i in range(2, len(sequence)):
        # Update the maximum and second maximum elements based on the current element
        if sequence[i] > max_element:
            second_max_element = max_element
            max_element = sequence[i]
        elif sequence[i] > second_max_element:
            second_max_element = sequence[i]
        # Store the maximum and second maximum elements in the matrix
        max_matrix[i] = max_element, second_max_element

    # Return the two maximum elements for the entire sequence (stored in the last row of the matrix)
    return max_matrix[-1]
  
  
