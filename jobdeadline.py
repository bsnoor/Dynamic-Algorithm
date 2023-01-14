def getAverageTime(times):
    # Sort the input list of times in ascending order
    sorted_times = sorted(times)
    # Print the "Optimal order of times"
    print("Optimal order of times:",sorted_times)
    # Initialize two variables to store the time spent on each task and the total time spent
    time_client, sum_times = 0.00, 0.00
    # Iterate through the sorted list of times
    for t in sorted_times:
        # Add the current time to the time spent on the task
        time_client += t
        # print the time_client 
        print("time_client =",time_client)
        # Add the time spent on the task to the total time
        sum_times += time_client
    # Print the total time
    print("Time total:", sum_times)
    # Return the average time by dividing the total time by the number of tasks
    return sum_times/len(times)

# sample input array of times
array_times = [1,10,8]
# pass the array to the function and print the result
print("for array times is %s, average time is %f" % (array_times, getAverageTime(array_times)))
