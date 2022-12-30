def lcsMaxSequence(s1, s2):
    '''
    * Find the longest common subsequence (LCS) of two strings
    * Complexity: O(m*n), m=len(s1), n=len(s2)
    :param s1: first string
    :param s2: second string
    :return: longest common subsequence of s1 and s2 as a list of characters
    '''
    # Initialize a matrix of zeros with dimensions len(s1)+1 by len(s2)+1
    matrix = [[0] * (len(s2) + 1) for i in range(len(s1) + 1)]
    # Loop through the rows and columns of the matrix
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            # If at the first row or column, set the value to 0
            if i == 0 or j == 0:
                matrix[i][j] = 0
            # If s1[i-1] (the current character in s1) is equal to s2[j-1] (the current character in s2),
            # add 1 to the value in the matrix at [i-1][j-1] (the value for the LCS of the substrings
            # of s1 and s2 without the current characters)
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            # If s1[i-1] and s2[j-1] are not equal, take the maximum of the values in the matrix at
            # [i-1][j] and [i][j-1] (the values for the LCS of the substrings of s1 and s2 without the
            # current characters in s1 and s2, respectively)
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

    # Get the length of the LCS by looking at the value in the bottom right corner of the matrix
    seq_length = matrix[len(matrix) - 1][len(matrix[0]) - 1]
    # Initialize a list to store the LCS
    result = [0] * seq_length
    # Set the starting position at the bottom right corner of the matrix
    i = len(matrix) - 1
    j = len(matrix[0]) - 1
    # While not at the top left corner of the matrix
    while i > 0 and j > 0:
        # If s1[i-1] is equal to s2[j-1]
        if s1[i - 1] == s2[j - 1]:
            # Add s1[i-1] to the LCS and move diagonally up and to the left in the matrix
            result[seq_length - 1] = s1[i - 1]
            seq_length -= 1
            i -= 1
            j -= 1
        # If s1[i-1] is not equal to s2[j-1]
        else:
                       # If the value in the matrix at [i-1][j] is greater than the value at [i][j-1], move up in the matrix
       elif matrix[i - 1][j] > matrix[i][j - 1]:
                i -= 1
            # Otherwise, move to the left in the matrix
            else:
                j -= 1
    # Return the LCS
    return result


