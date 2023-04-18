class Solution {
    public int firstMissingPositive(int[] nums) {
        Arrays.sort(nums);
        int res =1;
        for(int i=0;i<nums.length;i++){
            if(res==nums[i]){
                res=res+1;
            }
        }
        return res;
    }
}