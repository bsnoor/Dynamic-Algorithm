def AdaptiveAlgorithm(arr):
    # Initialize variables for the scores of Alice and Bob
    alice_result = 0
    bob_result = 0

    # Initialize variables for the beginning and end of the array
    begin = 0
    end = len(arr) - 1

    # Initialize variables for the sums of the even- and odd-indexed elements
    odd_sum = 0
    even_sum = 0
    for i in range(0, len(arr), 2):
        even_sum += arr[i]
        odd_sum += arr[i + 1]

    # Determine whether Alice should choose even- or odd-indexed elements
    even = True if even_sum > odd_sum else False

    # Initialize a step counter
    step = 1

    # Print a message indicating the start of the game
    print("*********** THIS IS A GAME **********")
    print(arr)

    # Continue playing until there are no more elements in the array
    while end > begin:
        # Determine whether Alice should choose even- or odd-indexed elements
        even = True if even_sum > odd_sum else False

        # Print information about the current step
        print("******* step #", step, "*******")
        print("****** even #", even, ", begin #", begin, ", end #", end, " *****")

        # ***** First player ( Alice ) choice *****

        # Print the remaining portion of the array
        print(arr[begin:end + 1])

        # If Alice should choose an even-indexed element and the current first element is even-indexed, or if Alice should choose an odd-indexed element and the current first element is odd-indexed, choose the first element. Otherwise, choose the last element.
        if (even and begin % 2 == 0) or (even != True and begin % 2 != 0):
            # Update the sum of the even- or odd-indexed elements, depending on the current element
            if even:
                even_sum -= array[begin]
            else:
                odd_sum -= array[begin]

            # Print the element that Alice is choosing and add it to her score
            print("ALICE: I take the first:", arr[begin])
            alice_result += arr[begin]

            # Move the beginning of the array to the next element
            begin += 1
        else:
            # Update the sum of the even- or odd-indexed elements, depending on the current element
            if even:
                even_sum -= array[end]
            else:
                odd_sum -= array[end]

            # Print the element that Alice is choosing and add it to her score
            print("ALICE: I take the last:", arr[end])
            alice_result += arr[end]

            # Move the end of the array to the previous element
            end -= 1

        # ***** Second player ( Bob ) choice *****

        # Print the remaining portion of the array
        print(arr[begin:end + 1])

        # If the first element is larger than the last element, choose the first element. Otherwise, choose the last element.
        if arr[begin] > arr[end]:
          # Print the element that Bob is choosing and add it to his score
            print("BOB: I take the first:", arr[begin])
            if begin % 2 == 0:
                even_sum -= array[begin]
            else:
                odd_sum -= array[begin]
            bob_result += arr[begin]

            # Move the beginning of the array to the next element
            begin += 1
        else:
            # Print the element that Bob is choosing and add it to his score
            print("BOB: I take the last:", arr[end])
            if end % 2 == 0:
                even_sum -= array[end]
            else:
                odd_sum -= array[end]
            bob_result += arr[end]

            # Move the end of the array to the previous element
            end -= 1

        # Increment the step counter
        step += 1

        # Print the current scores for Alice and Bob
        print("Sum - ALICE:", alice_result, ", BOB:", bob_result)

    # Print a message indicating the end of the game and the final scores for Alice and Bob
    print("Congratulations! ALICE =", alice_result, ", BOB =", bob_result)
    
    
    
