# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create a hash table
        hash_table = {}
        
        for i, num in enumerate(nums):
            
            if (target - num) in hash_table.keys():
                
                first_index = i
                second_index = hash_table[target - num]
                
                return [first_index, second_index]
            
            hash_table[num] = i

     
        return []