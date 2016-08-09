from itertools import permutations
def pandigital(nums):
    lst = range(0,len(nums))
    for l in lst:
        if l not in nums:
            return False
    return True
def divprop(x):
    nums = [x for x in str(x)]
    return (int(''.join([nums[1],nums[2],nums[3]]))%2==0) and (int(''.join([nums[2],nums[3],nums[4]]))%3==0) and (int(''.join([nums[3],nums[4],nums[5]]))%5==0) and (int(''.join([nums[4],nums[5],nums[6]]))%7==0) and (int(''.join([nums[5],nums[6],nums[7]]))%11==0) and (int(''.join([nums[6],nums[7],nums[8]]))%13==0) and (int(''.join([nums[7],nums[8],nums[9]]))%17==0)
def main():
    perms = permutations([0,1,2,3,4,5,6,7,8,9], 10)
    n_power = len([0,1,2,3,4,5,6,7,8,9]) - 1
    candids = filter(lambda x: x[0] != 0, perms)
    candids = [sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in candids]
    candids = filter(lambda x: divprop(x)==True, candids)
    return sum(candids)
print main()