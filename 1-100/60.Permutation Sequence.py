class Solution(object):
'''
	def getPermutation(self, n, k):
		nums=[str(i) for i in range(1,n+1)]
		result=[]
		self.DFS(result,[],nums)
		return result[k-1]
	def DFS(self,result,L1,nums):
		if len(nums)==0:
			result.append(''.join(L1))
		for i in range(len(nums)):
			L1.append(nums[i])
			self.DFS(result,L1,nums[:i]+nums[i+1:])
			L1.pop()
超时
'''
	def getPermutation(self,n,k):
		result=''
		k-=1
		fac=1
		for i in range(1,n):
			fac*=i
		num=[str(i) for i in range(1,n+1)]
		for  i in reversed(range(n)):
			curr=num[k//fac]
			result+=str(curr)
			num.remove(curr)
			if i!=0:
				k%=fac
				fac=fac//i
		return result