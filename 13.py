class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count_dict = {}
        count_dict[0] = -1
        maxlen = 0
        count = 0
        for i in range(len(nums)):
            count += 1 if nums[i] else -1
            if count in count_dict.keys():
                maxlen = max(maxlen, i - count_dict[count])
            else:
                count_dict[count] = i
        return maxlen


#         public class Solution {

#     public int findMaxLength(int[] nums) {
#         Map<Integer, Integer> map = new HashMap<>();
#         map.put(0, -1);
#         int maxlen = 0, count = 0;
#         for (int i = 0; i < nums.length; i++) {
#             count = count + (nums[i] == 1 ? 1 : -1);
#             if (map.containsKey(count)) {
#                 maxlen = Math.max(maxlen, i - map.get(count));
#             } else {
#                 map.put(count, i);
#             }
#         }
#         return maxlen;
#     }
# }


if __name__ == "__main__":
    arr1 = [0, 1, 0, 1, 0]  # should return 4
    print(Solution().findMaxLength(arr1))
