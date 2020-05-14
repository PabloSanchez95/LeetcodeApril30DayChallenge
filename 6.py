class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anas_dict = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in anas_dict.keys():
                anas_dict[sorted_word].append(word)
            else:
                anas_dict[sorted_word] = [word]
        return list(anas_dict.values())


if __name__ == "__main__":
    anas = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # anas = ["", "b", ""]
    print(Solution().groupAnagrams(anas))
