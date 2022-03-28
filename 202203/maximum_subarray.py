def maxSubArray(nums):
    if len(nums) == 1:
        return nums[0]

    """
    Time Limit Exceeded
    
    result = []
    for idx in range(len(nums)):
        div = idx + 1
        while div <= len(nums):
            temp = nums[idx:div]
            result.append(sum(temp))
            div += 1
    return max(result)
    """

    # Kadane’s Algorithm
    current_subarray = max_subarray = nums[0]

    for num in nums[1:]:

        current_subarray = max(num, current_subarray + num)
        max_subarray = max(max_subarray, current_subarray)

    return max_subarray


