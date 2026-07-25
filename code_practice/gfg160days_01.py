class Solution:
    def getSecondLargest(self, arr):
        # code here
        for i in range(len(arr)-1):
            # arr.sort()
            # large=arr[0]
            a= arr[i]
            b=arr[i+1]
            if a<b:
                large= b
                second_large=a
            else:
                return -1
            
        return large
        # return second_large
