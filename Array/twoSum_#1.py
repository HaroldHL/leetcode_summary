# 暴力求解
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
        return res

# 遍历数组，首先用hashmap保存数组结果，数字的值为key，索引为value
# 遍历数组，使用hashmap的get方法 验证两数之和

def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx,val in enumerate(nums):
            hashmap[val] = idx
        for i, val in enumerate(nums):
            j = hashmap.get(target - val)
            if j is not None and i != j: 
                return [i,j]  