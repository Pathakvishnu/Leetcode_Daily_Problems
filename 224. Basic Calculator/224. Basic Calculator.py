class Solution:
    def calculate(self, s: str) -> int:
        stack, pt = [],0
        num = 0
        sign = '+' # by default 

        def update_stack(n,s):
            if s=="+":
                stack.append(n)
            if s=="-":
                stack.append(-n)

        while pt<len(s):
            if s[pt]==" ":
                pt+=1
                continue

            elif s[pt].isdigit():
                num = num*10 + int(s[pt])
            
            elif s[pt] in ['+','-']:
                update_stack(num,sign)
                num = 0 # reset num 
                sign = s[pt]

            # whenever we will encounter the start of bracket we will invoke calculate fn again 
            # as you can see a string inside bracket is a complete different sub problem all together.
            elif s[pt]=='(':
                num,i = self.calculate(s[pt+1:])
                pt = pt+i
            
            elif s[pt]==')':
                # this update is to push element before ) into stack
                # as in example 3 (4+5+2)
                # now 2 is stored in num but not stored in stack, so at the end we will get 
                # wrong answer we don't do it
                update_stack(num,sign) 
                return sum(stack),pt+1

            pt+=1

        update_stack(num,sign)
        return sum(stack)


s = "(1+(4+5+2)-3)+(6+8)"
obj = Solution()
print(obj.calculate(s))

