class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        
        map<int, int>m;
        vector<int> op;
        
        for(int i=0;i<nums.size();i++)
        {
            m[nums[i]]++;
        }
        
        for(auto i:m)
        {
            if(i.second > int(nums.size()/3))
            {
                op.push_back(i.first);
            }
        }
        return op;
    }
};
