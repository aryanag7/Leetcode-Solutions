class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(0,len(nums2)):
            found=False
            for j in range(i+1,len(nums2)):
                if nums2[j]>nums2[i]:
                    ans.append(nums2[j])
                    found=True
                    break
            if found==False:
                ans.append(-1)
   
        dictionary=dict(zip(nums2,ans))
        final_ans=[]
        for i in nums1:
            final_ans.append(dictionary[i])
        return final_ans

#Another Solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n=len(nums2)
        stack=[]
        nge=[0]*len(nums2)
        nge[n-1]=-1
        stack.append(nums2[n-1])
        for i in range(len(nums2)-2,-1,-1):
            while len(stack)!=0 and  nums2[i]>=stack[-1]:
                stack.pop()
            if len(stack)==0:
                nge[i]=-1
            else:
                nge[i]=stack[-1]
            stack.append(nums2[i])
        for i in range(0,len(nums1)):
            index=nums2.index(nums1[i])
            nums1[i]=nge[index]

        return nums1
         

        
