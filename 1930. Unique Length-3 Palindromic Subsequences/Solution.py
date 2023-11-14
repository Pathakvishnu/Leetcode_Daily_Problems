class Solution:
  def countPalindromicSubsequence(self, s: str) -> int:
      first_occ = [-1]*26
      last_occ = [-1]*26
  
      for i in range(len(s)):
          idx = ord(s[i])-ord('a')
          if first_occ[idx]==-1:
              first_occ[idx] = i
          last_occ[idx] = i
  
      ans = 0
      for ch in dict.fromkeys(s):
          curr = ord(ch)-ord('a')
          if first_occ[curr]==-1:
              continue
          
          between  = set()
          for j in range(first_occ[curr]+1,last_occ[curr]):
              between.add(s[j])
          ans+=len(between)
  
      return ans
