#User function Template for python3

class Solution:
    def removeStudents(self, H, N):
        
        def binary_search(A, l, r, key):
            while (r - l > 1):
             
                m = l + (r - l)//2
                if (A[m] >= key):
                    r = m
                else:
                    l = m
            return r
        
        LIS = [0 for i in range(N + 1)]
        max_len = 0 
      
        LIS[0] = H[0]
        max_len = 1
        for i in range(1, N):
         
            if (H[i] < LIS[0]):
    
                LIS[0] = H[i]
      
            elif (H[i] > LIS[max_len-1]):
    
                LIS[max_len] = H[i]
                max_len+= 1
      
            else:
                LIS[binary_search(LIS, -1, max_len-1, H[i])] = H[i]
                
        return N-max_len


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        H=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.removeStudents(H,N))
# } Driver Code Ends