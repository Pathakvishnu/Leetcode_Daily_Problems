class Solution:
    def average(self, salary: List[int]) -> float:

        min_sal = 1e7
        max_sal = 1e3
        tot = 0
        n = 0
        for sal in salary:
            n+=1
            if sal>max_sal:
                max_sal=sal
            if sal<min_sal:
                min_sal=sal
            tot+=sal
        
        return ((tot-min_sal-max_sal)/(n-2))

salary = [4000,3000,1000,2000]
obj = Solution()
obj.average(salary)


