def moveZeroes(nums : list[int]) -> None: 
    """ Do not return anything, modify nums in-place instead"""
    for i in nums : 
        if i == 0 : 
            nums.remove(0)
            nums.append(0)