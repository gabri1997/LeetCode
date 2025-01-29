"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.

"""

def removeElement(nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        for element in nums:
                if element != val:
                        nums[index] = element
                        index += 1
        return index, nums[:index]


if __name__ == '__main__':

        nums = [1,2,3,4,5,6,1,1]
        val = 1
        k, vals = removeElement(nums, val)
        print('Numero di elementi: ', k)
        print('Il vettore è diventato: ', vals)