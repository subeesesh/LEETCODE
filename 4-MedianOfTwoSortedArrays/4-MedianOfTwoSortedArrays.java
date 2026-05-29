// Last updated: 5/29/2026, 12:01:30 PM
class Solution {
    public int[] merge(int[] nums1,int[] nums2){
        int n=nums1.length;
        int m=nums2.length;
        int[] arr=new int[n+m];
        int i=0,j=0,k=0;
        while(i<n&&j<m){
            if(nums1[i]<nums2[j]){
                arr[k]=nums1[i];
                i++;
            }
            else{
                arr[k]=nums2[j];
                j++;
            }
            k++;
        }
        while(i<n){
            arr[k++]=nums1[i++];
        }
        while(j<m){
            arr[k++]=nums2[j++];
        }
        return arr;
    }
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int [] arr=merge(nums1,nums2);
        int low=0,high=arr.length;
        int mid=((high-low)/2) -1 ;
        double result=0;
        if(arr.length%2==0){
            return result=(arr[mid]+arr[mid+1])/2.0;
        }
            return result=arr[mid +1 ];

        
    }
}