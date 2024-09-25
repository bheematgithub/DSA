class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i=res=0
        count = {"T":0,"F":0}
        for j in range(len(answerKey)):
            count[answerKey[j]] += 1
            while count["T"] > k and count["F"] > k:
                count[answerKey[i]] -= 1
                i += 1
            res= max(res,j-i + 1)
        return res
