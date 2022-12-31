def LCS_Matrix(X, Y):
    '''
    Creating matrix of length common subsequences
    L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1]
    Complexity: O(m*n) in worst case, O(m+n), assuming the size of the alphabet is constant.
    :param X: first sequence
    :param Y: second sequence
    :return: a matrix of length common subsequences
    '''
    # Find the lengths of the two sequences
    m = len(X)  # number of rows
    n = len(Y)  # number of columns

    # Create the matrix for storing the DP values
    L = [[None] * (n + 1) for i in range(m + 1)]

    # Iterate over the rows and columns of the matrix
    for i in range(m + 1):
        for j in range(n + 1):
            # If either the current row or column is 0, set the element to 0
            if i == 0 or j == 0:
                L[i][j] = 0
            # If the elements in the current row and column match, set the element to the value in the previous row and column plus 1
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            # Otherwise, set the element to the maximum of the value in the previous row and the value in the previous column
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
 # Return the matrix and the length of the LCS for the entire sequences (stored in L[m][n])
       return L, L[m][n]
    
