class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num_sum = self.makeSum(n)
        rem_nums = [num_sum]
        while num_sum != 1:
            num_sum = self.makeSum(num_sum)
            if num_sum in rem_nums:
                return False
            else:
                rem_nums.append(num_sum)
        return True

    def makeSum(self, num):
        sum_digits = 0
        while num:
            last_digit = num % 10
            sum_digits += last_digit ** 2
            num //= 10
        return sum_digits


if __name__ == "__main__":
    print(Solution().isHappy(19))
