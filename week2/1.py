class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        numss=[]
        isnum=[0 for i in range(202)]

        for i in nums:
            if isnum[i+100]==1:continue
            else:
                 isnum[i+100]=1
                 numss.append(i)

        for i in range(len(numss)):
            nums[i]=numss[i]
        return len(numss)