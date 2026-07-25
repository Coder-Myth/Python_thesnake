#day 2 add two numbers 

class Solution:
    def getSecondLargest(self, arr):
        # code here
        for i in range(len(arr)):
            arr.sort()
            
            a= arr[i]
            b= arr[i+1]
            
            if a>b:
                return b
                
        return b