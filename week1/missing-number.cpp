class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int arr[10000]={0};
        int i=0;
        std::vector<int>::iterator itr=nums.begin();
        while(itr!=nums.end())
        {
            arr[*itr]++;
            itr++;
            i++;
        }
        while(i>=0)
        {
            if(arr[i]==0)
                break;
            i--;
        }
        return i;
    }
};