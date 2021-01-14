class Solution:
    def distributeCandies(self, candyType) -> int:
        set_of_list=set(candyType)
        if len(candyType)/2 >=len(set_of_list):
            return len(set_of_list)
        if len(set_of_list) > len(candyType)/2:
            return int(len(candyType)/2)

s=Solution()
arr=[1,1,2,2,3,3]
print(s.distributeCandies(arr))         