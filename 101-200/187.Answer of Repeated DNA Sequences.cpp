class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<int, int> m;
    vector<string> r;
    int t = 0, i = 0, ss = s.size();
    while (i < ss)
        if (m[t = (t << 3 | s[i++] & 7) & 0x3FFFFFFF]++ == 1)
            r.push_back(s.substr(i - 10, 10));
    return r;
}
};