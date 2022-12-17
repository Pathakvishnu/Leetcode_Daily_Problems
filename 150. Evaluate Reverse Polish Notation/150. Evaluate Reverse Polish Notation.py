from ast import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        store = list()

        for ele in tokens:
            to_push = None
            if ele in ["*","+","-","/"]:
                b = store.pop()
                a = store.pop()
                if ele=="+":
                    to_push = a + b
                elif ele=="-":
                    to_push = a - b
                elif ele=="*":
                    to_push = a * b
                elif ele=="/":
                    to_push = int(a / b)
            else:
                to_push = int(ele)
            
            store.append(to_push)

        # print(store)
        return store.pop()

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj = Solution()
print(obj.evalRPN(tokens))