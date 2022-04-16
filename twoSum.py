class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        visited = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement not in visited:    
                visited[num] = i
            else:
                result.append(i)
                result.append(visited[complement])
                
        return(result)