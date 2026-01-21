class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n=s.length();
        int maxlen=0;
       int left =0;
        HashSet<Character> set = new HashSet<>();
         for(int right=0;right< n;right++){

           char c= s.charAt(right);

           while(set.contains(c)){
            set.remove(s.charAt(left));
            left++;
           }

           set.add(c);
           maxlen=Math.max(maxlen, right-left +1);




         }
         return maxlen;


    }
}
