# 新建一个索引来记录零的位置
# 每次循环的时候进行交换

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j],nums[i] = nums[i],nums[j]
                j += 1

print(moveZeroes([0,1,0,3,12]))