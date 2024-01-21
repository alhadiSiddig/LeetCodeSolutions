'''two conditions must be satisfied :
1. the sum of two larger than the third
2. teh difference between two is less than the third   '''
def largestPerimeter(nums : list[int]) -> bool : 
    nums.sort(reverse = True ) 
    for i in range(len(nums) -2 ): 
        if sum(nums [i : i + 3 ]) >  2 * nums[i]: 
            return sum(nums[i : i + 3]) 
    return 0 