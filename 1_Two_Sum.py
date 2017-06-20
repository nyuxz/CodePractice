# 1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        @logit
        1. hash table (dictionary)
        2. the key point of using dict: value as dict-key and index as dict-value
        """
        if len(nums) < 1:
            return 'Error'
        
        dict = {}
        
        for i in range(len(nums)):
            
            x = nums[i]
            
            # condition on if index in dict 
            if target-x in dict:
                return (dict[target-x], i)
            else:
                dict[x] = i 

    def twoSum_2(self, nums, target):
        '''
        @logit
        1. two pointers, one from beginning of the array to the end, and the other reverse direction.
        2. both pointers move towards to each other.
        3. comparing with twoSum, twoSum_2 can print all index list having the target sum.
        '''
        index_initial = []
        index = [0,0]
        index_list = []
        asc_nums = sorted(nums, key=int)
        #des_nums = sorted(nums, key=int, reverse = True)

        # specify the initial position of the pointers
        i = 0
        j = len(nums) - 1

        while i < j:
            if asc_nums[i] + asc_nums[j] == target:
                for k in range(0, len(nums)):
                    if nums[k] == asc_nums[i]:
                        index[0] = k
                        print (k)
                        break

                for k in range(len(nums)-1, -1, -1):
                    if nums[k] == asc_nums[j]:
                        index[1] = k
                        print(k)
                        break

                i = i + 1
                j = j - 1 

                index_list.append([index[0],index[1]])

            elif asc_nums[i] + asc_nums[j] > target:
                j = j - 1
            elif asc_nums[i] + asc_nums[j] < target:
                i = i + 1

        return index_list

print(Solution().twoSum([1,2,3,0,6,3,4,5], 6))
print(Solution().twoSum_2([1,2,3,0,6,3,4,5], 6))