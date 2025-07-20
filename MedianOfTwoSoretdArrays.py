class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        array=[]
        i=j=0
        while i!=nums1.len or  j != nums2.len:
            if nums1[i] > nums2[j]:
                array.append(nums1)
            else:
                array.append(nums2)    
        
        while i != nums1.len:        
            array.append(nums1)
        while j != nums2.len:        
            array.append(nums2)
            
        return array[array.len/2]   