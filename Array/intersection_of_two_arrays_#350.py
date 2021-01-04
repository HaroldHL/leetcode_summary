# 排序 + 双指针
def intersect(nums1, nums2):
        if not nums1 or not nums2:
            return []

        nums1.sort()
        nums2.sort()

        res = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            
        return res

print(intersect([1,2,2,1],[2,2]))