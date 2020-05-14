class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        s_list = []
        t_list = []

        for s in S:
            if s == "#" and s_list:
                s_list.pop()
            elif s != "#":
                s_list.append(s)

        for t in T:
            if t == "#" and t_list:
                t_list.pop()
            elif t != "#":
                t_list.append(t)
        return s_list == t_list


if __name__ == "__main__":
    S = "ab#c"
    T = "ad#c"
    print(Solution().backspaceCompare(S, T))
    S = "ab##"
    T = "c#d#"
    print(Solution().backspaceCompare(S, T))
    S = "a##c"
    T = "#a#c"
    print(Solution().backspaceCompare(S, T))
    S = "a#c"
    T = "b"
    print(Solution().backspaceCompare(S, T))
