import numbers


class Solution(object):
    def removeDuplicates(self, nums):
        PrevElm=-101
        k=0
        while k < len(nums):
            if nums[k]==PrevElm:
              nums.pop(k)
            else:
                PrevElm=nums[k]
                k+=1
        return k

  

nums = [0,0,1,1,1,2,2,3,3,4]
print(len(nums))
print(nums)
p=Solution()
print(p.removeDuplicates(nums))
print(nums)