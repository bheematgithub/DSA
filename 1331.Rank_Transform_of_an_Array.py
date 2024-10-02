class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sl=sorted(list(set(arr)))
        dic={}
        for i in range(len(sl)):
            dic[sl[i]]=i+1
        for i in range(len(arr)):
            arr[i]=dic[arr[i]]
        return arr
