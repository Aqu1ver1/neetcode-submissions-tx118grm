public class Solution {
    public bool IsAnagram(string s, string t) {
        // if(s.Length != t.Length) return false;
        // HashTable chars = new HashTable();
        // for(int i = 0; i < s.Length;i++){

        // }
        char[] char1 = s.ToArray();
        char[] char2 = t.ToArray();
        Array.Sort(char1);
        Array.Sort(char2);
        string s2 = new string(char1);
        string t2 = new string(char2);
        return s2 == t2;
    }
}
