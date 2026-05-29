# Last updated: 5/29/2026, 12:01:25 PM
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        list1=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                list1.append(nums1[i])
                i+=1
            else:
                list1.append(nums2[j])
                j+=1
        while(j<len(nums2)):
            list1.append(nums2[j])
            j+=1
        while(i<len(nums1)):
            list1.append(nums1[i])
            i+=1
        mid=len(list1)/2
        if len(list1)%2==0:
            return (list1[mid]+list1[mid-1])/2.0
        else:
            return list1[mid]