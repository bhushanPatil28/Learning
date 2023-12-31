#include <stdio.h>

int find_loc(int arr[], int len, int find);

int main() {
    int a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int find = 8;
    int len = sizeof(a) / sizeof(a[0]);
    int result = find_loc(a, len, find);
    
    if (result != -1) {
        printf("Element %d found at index %d\n", find, result);
    } else {
        printf("Element %d not found in the array\n", find);
    }
    
    return 0;
}

int find_loc(int arr[], int len, int find) {
    int lo = 0;
    int hi = len - 1;
    
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2; // Calculate mid without potential overflow
        
        if (arr[mid] == find) {
            return mid;
        } else if (arr[mid] < find) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    
    return -1; // Element not found
}
