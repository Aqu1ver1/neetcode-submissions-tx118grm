public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        int[] counts = new int[26];
        var dict = new Dictionary<string, List<string>>();
        foreach(string s in strs){
            Array.Clear(counts, 0, counts.Length);
            foreach(char c in s){
                counts[c - 'a']++;
            }

            string key = string.Join(',', counts);

            if(!dict.ContainsKey(key)){
                dict[key] = new List<string>();
            }
            dict[key].Add(s);
            
        }
        var res = new List<List<string>>();
        foreach(var pair in dict){
            res.Add(pair.Value);
        }
        return res;
    }
}
