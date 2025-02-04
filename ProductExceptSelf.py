"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

def productExceptSelf(nums):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        answer = []
        for j in range(len(nums)):
            tmp_product = 1
            for i, numero in enumerate(nums):
                if i != j:
                    tmp_product = tmp_product * numero
            answer.append(tmp_product)
        return answer


if __name__ == '__main__':

        nums = [1,2,3,4]
        answer = productExceptSelf(nums)
        print(answer)
        