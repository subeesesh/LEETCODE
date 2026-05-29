// Last updated: 5/29/2026, 12:01:36 PM
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* ree) 
{
    int* result = (int*)malloc(2 * sizeof(int));
    for (int i=0;i<numsSize-1;i++)
    {
        for (int j=i+1;j<numsSize;j++)
        {
            if (nums[i]+nums[j]==target)
            {
                result[0]=i;
                result[1]=j;
                 *ree = 2;
                 return result;
            }
        }
    }    
    return *ree;
}