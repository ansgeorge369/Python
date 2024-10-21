# Assign multiple values
nums = [25,35,45,55]
print(nums)
print(nums[0])
print(nums[2:])
print(nums[-1])
print(nums[-4])

names = ['ans', 'dante', 'edmond']
print(names)

values = [2.5, 'Ans', 26]
print(values)

data = [nums , names]
print(data)

nums.append(99)  #add to the list
print(nums)

nums.insert(2, 82)
print(nums)

nums.remove(99)
print(nums)

nums.pop(0)  #remove value with index number
print(nums)

nums.pop()   #if no index number is not mentioned the last entered value will be removed
print(nums)

del nums[1:] #deletes the values mentioned after the index
print(nums)

nums.extend([1,2,3,4,5,6,7,8,9])
print(nums)

print(min(nums))
print(max(nums))
nums.reverse()
print(nums)
nums.sort()
print(nums)
nums.count(5)
print(nums)
nums.copy()
print(nums)
print(sum(nums))

nums.clear()
print(nums)