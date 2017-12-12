class Solution {
public:
    vector<int> grayCode(int n) 
    //格雷码，不知道啥意思
    {         
        vector<int> res(1, 0);
        for (int i = 0; i < n; ++i) {
            int size = res.size();
            while (size--) {
                int curNum = res[size];
                curNum += (1 << i);
                res.push_back(curNum);
            }
        }
        return res;
    }
};