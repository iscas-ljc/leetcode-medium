class Solution(object):
    def search(self, nums, target):
        return target in nums
'''
class Solution {
public:
    //二分查找
    bool search(int A[], int n, int target) {
        int start = 0,end = n-1;
        int mid;
        while(start <= end){
            mid = (start + end) / 2;
            if(A[mid] == target){
                return true;
            }
            //中间元素大于最左边元素则左部分为有序数组
            else if(A[mid] > A[start]){
                //目标位于左部分
                if(target >= A[start] && target <= A[mid]){
                    end = mid - 1;
                }
                //目标位于右部分
                else{
                    start = mid + 1;
                }
            }
            //中间元素小于最左边元素则右部分为有序数组
            else if(A[mid] < A[start]){
                //目标位于右部分
                if(target <= A[end] && target >= A[mid]){
                    start = mid + 1;
                }
                //目标位于左部分
                else{
                    end = mid - 1;
                }
            }
            //中间元素等于最左边元素则无法区分有序部分
            else{
                start++;
            }
        }
        return false;
    }
};
int main() {
    int result;
    Solution solution;
    int A[] = {4,5,1,2,3};
    result = solution.search(A,5,4);
    printf("Result:%d\n",result);
    return 0;
}
'''