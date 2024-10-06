class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        l1,l2=sentence1.split(),sentence2.split()
        n1,n2=len(l1),len(l2)
        l,h=0,0

        if n1<n2:
            l1,l2=l2,l1
            n1,n2=n2,n1

        while l<n2 and l1[l] == l2[l]:
            l+=1

        while h<n2 and l1[n1 - h - 1] == l2[n2 - h -1]:
            h+=1

        return l+h >= n2
