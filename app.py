def two_sum(nums, target):
    """
    Returns the indices of the two numbers in the array `nums` that add up to `target`.

    :param nums: List[int] - A list of integers.
    :param target: int - The target sum.
    :return: List[int] - Indices of the two numbers.
    """
    # Dictionary to store the index of the numbers we have seen so far
    index_map = {}
    
    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement of the current number
        complement = target - num
        
        # Check if the complement exists in the hash map
        if complement in index_map:
            # Return the indices of the complement and the current number
            return [index_map[complement], i]
        
        # Store the index of the current number
        index_map[num] = i
    
    # Return an empty list if no solution is found (though the problem guarantees a solution)
    return []

# Example usage
nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))  # Output: [0, 1]
