class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        low = m-1
        high = n-1
        k = m+n-1 
        while low>=0 and high >=0:
            if nums1[low]>nums2[high]:
                nums1[k]=nums1[low]
                low-=1
            else:
                nums1[k]=nums2[high]
                high-=1
            k-=1
        while high>=0:
            nums1[k]=nums2[high]
            high-=1
            k-=1

