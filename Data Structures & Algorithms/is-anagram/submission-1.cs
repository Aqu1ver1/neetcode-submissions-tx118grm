public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length) return false;
        Dictionary<char,int> isAnagram = new Dictionary<char,int>();
        foreach(char c in s){
            if(!isAnagram.ContainsKey(c)){
                isAnagram[c] = 0;
            }
            isAnagram[c]++;
        }

        foreach(char c in t){
            if(!isAnagram.ContainsKey(c) || isAnagram[c] == 0){
                return false;
            }
            isAnagram[c]--;
        }
        return true;
    }
}
