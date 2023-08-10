class Solution {
    public static int removeDuplicates(int[] nums) {
        int uniqueInts = 0;
        for (int x = 0; x < nums.length; x++){
            if(x < nums.length -1 && nums[x] == nums[x+1]){
                continue;
            }
            nums[uniqueInts] = nums[x];
            uniqueInts +=1;
        }
        return uniqueInts;
    }

    public static void main(String[] args) {
        int[] nums = {0,0,1,1,1,2,2,3,3,4};
        int num = removeDuplicates(nums); 
        System.out.println(num);
    }
}
