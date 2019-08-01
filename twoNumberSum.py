def twoNumberSum(array, targetSum):
	a = {}
	for i in array:
		if targetSum-i in a:
			result = [i,targetSum-i]
			result.sort()
			return result
		else:
			a[i] = True
	return []
