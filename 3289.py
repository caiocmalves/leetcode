nums = [7,1,5,4,3,4,6,0,9,5,8,2]
repete = []

for i in range(len(nums)):
    x = nums[i]
    del [nums[i]]
    if x in nums:
        if x in repete:
            pass
        else:
            repete.append(x)
    nums.insert(i, x)

print(repete)