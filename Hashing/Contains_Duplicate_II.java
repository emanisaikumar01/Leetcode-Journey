class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
     Map<Integer, Integer> lastSeen = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            if (lastSeen.containsKey(num)) {
                if (i - lastSeen.get(num) <= k) {
                    return true;
                }
            }
            lastSeen.put(num, i);
        }
        
        return false;
    
    }
}
