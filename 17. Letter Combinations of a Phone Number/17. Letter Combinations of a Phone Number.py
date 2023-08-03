class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        num_to_let = {"1":[],
        "2":["a","b","c"],
        "3":["d","e","f"],
        "4":["g","h","i"],
        "5":["j","k","l"],
        "6":["m","n","o"],
        "7":["p","q","r","s"],
        "8":["t","u","v"],
        "9":["w","x","y","z"]}

        n = len(digits)
        if n==1:
            return list(num_to_let[digits])
        ans = []
        def get_combination(idx, path):
            if idx>=n:
                ans.append(path)
                return
            
            letter = num_to_let[digits[idx]]

            for a in letter:
                get_combination(idx+1,path+a)

        get_combination(0,"")
        return ans
        
digits = "234"
obj = Solution()
obj.letterCombinations(digits)
        
        
