class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1,n2=len(s1),len(s2)
        if n2<n1:
            return False

        freq1,freq2=[0]*26,[0]*26

        for i in range(n1):
            freq1[ord(s1[i])-97]+=1
            freq2[ord(s2[i])-97]+=1

        for i in range(n2-n1):
            if freq1==freq2:
                return True
            freq2[ord(s2[i])-97]-=1
            freq2[ord(s2[i+n1])-97]+=1

        return freq1==freq2
