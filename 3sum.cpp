#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> triplet(int n, vector<int> &arr) {
    vector<vector<int>> ans;
    int len = arr.size();

    // Sort the array in ascending order.
    sort(arr.begin(), arr.end());

    for (int i = 0; i < len - 2; i++) {
        // To avoid duplicate triplets, skip duplicates of the current element.
        if (i > 0 && arr[i] == arr[i - 1])
            continue;

        int left = i + 1;
        int right = len - 1;

        while (left < right) {
            int currentSum = arr[i] + arr[left] + arr[right];

            if (currentSum < 0) {
                left++;
            } else if (currentSum > 0) {
                right--;
            } else {
                // Store the triplet in the result vector.
                ans.push_back({arr[i], arr[left], arr[right]});

                // To avoid duplicate triplets, skip duplicates of left and right elements.
                while (left < right && arr[left] == arr[left + 1])
                    left++;
                while (left < right && arr[right] == arr[right - 1])
                    right--;

                left++;
                right--;
            }
        }
    }

    return ans;
}
