print("Hello world")
print("")class Solution:
    def precedence(self, x):
        if x == "^":
            return 3
        elif x in ["*", "/"]:
            return 2
        elif x in ["+", "-"]:
            return 1
        elif x in ["(", ")"]:
            return -1
        else:
            return 0
    # Function to convert an infix expression to a postfix expression.

    def InfixtoPostfix(self, exp):
        arr = []
        ans = ""
        for ele in exp:
            val = self.precedence(ele)
            if val == 0:
                ans += ele
                continue
            else:
                if ele == "(":
                    arr.append(ele)
                elif ele == ")":
                    while(len(arr) != 0 and arr[-1] != "("):
                        var = arr.pop()
                        ans += var
                    if len(arr) != 0 and arr[-1] == "(":
                        arr.pop()
                else:
                    while(len(arr) != 0 and self.precedence(arr[-1]) >= val):
                        temp = arr.pop()
                        ans += temp
                    arr.append(ele)
        while(len(arr) != 0):
            temp = arr.pop()
            ans += temp
        return ans

a=Solution()
res=a.InfixtoPostfix("a+b*(c^d-e)^(f+g*h)-i")
print(res)