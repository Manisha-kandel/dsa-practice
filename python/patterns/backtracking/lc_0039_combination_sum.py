#39. Combination Sum - 20 minutes
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, remain, comb):
            #base cases
            if remain == 0:                  #if we reached target, valid comb -> append it
                res.append(comb.copy())
                return
            if i == len(candidates) or remain < 0:  #invalid, don't append
                return        

            #Now, 2 cases for dfs.  
            # include candidates[i] (can reuse it — stay at same i)
            comb.append(candidates[i])      
            dfs(i, remain - candidates[i], comb)
            comb.pop()

            # skip candidates[i] entirely — move to i+1
            dfs(i + 1, remain, comb)

        dfs(0, target, [])
        return res