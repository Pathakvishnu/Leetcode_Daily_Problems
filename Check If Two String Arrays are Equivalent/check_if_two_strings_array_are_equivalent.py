from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    w1,w2 = 0,0 # iterate word in wordlist
    i,j = 0,0 # iterate char in word
    
    wlen1 = len(word1)    
    wlen2 = len(word2)
    
    while w1<wlen1 and w2<wlen2:
        
        if word1[w1][i]!=word2[w2][j]:
            return False
        i+=1
        j+=1
        # print(i,j)

        if i>=len(word1[w1]):
            i=0
            w1+=1
            
        if j>=len(word2[w2]):
            j=0
            w2+=1
            
    return w1==wlen1 and w2==wlen2