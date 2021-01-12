class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals_sorted = sorted(intervals, key=lambda x:x[0])
        
        solved = [intervals_sorted[0]]
        
        for interval in intervals_sorted[1:]:
            
            if interval[0] <= solved[-1][1]:
                
                # change end point
                solved[-1][1] = max(interval[1], solved[-1][1])
            
            else:
                
                solved.append(interval)
                
        return solved
                