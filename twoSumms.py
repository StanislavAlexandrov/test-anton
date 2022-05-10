class Solution(object):
    def __init__(self, nums, target,output):
        self.nums=nums
        self.target=target
        self.output=output
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x]+nums[y]==target:
                    output[0]=x
                    output[1]= y
                    break
       
        
p1=Solution([2,7,11,15],13,[0,0])
print(p1.output)
