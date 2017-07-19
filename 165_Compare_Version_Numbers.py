# 165. Compare Version Numbers

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        @logit:
        	1. split version by '.' to multiple parts
        	2. compare each part
        	3. for difference length of the version, add 0 for empty parts
		@note:
			1. 1 = 1.0 = 1.0.000.00 
			2. 1 = 01 = 000001
        """
        v1_list = version1.split('.')
        v2_list = version2.split('.')

        max_len = max(len(v1_list), len(v2_list))

        for i in range(0, max_len):
            v1 = int(v1_list[i]) if len(v1_list) > i else 0
            v2 = int(v2_list[i]) if len(v2_list) > i else 0
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            
        return 0
            
