class Solution:
    def checkValidString(self, s: str) -> bool:
        open_stack = []
        star_stack = []

        for i in range(len(s)):
            if s[i] == "*":
                star_stack.append(i)
            elif s[i] == "(":
                open_stack.append(i)
            else:
                if len(open_stack) > 0:
                    open_stack.pop()
                elif len(star_stack) > 0 and star_stack[-1] < i:
                    star_stack.pop()
                else:
                    return False

        for open_par in reversed(open_stack):
            if len(star_stack) > 0 and open_par < star_stack[-1]:
                open_stack.pop()
                star_stack.pop()
            else:
                return False
        return True


if __name__ == "__main__":
    my_str = "("
    print(Solution().checkValidString(my_str))
