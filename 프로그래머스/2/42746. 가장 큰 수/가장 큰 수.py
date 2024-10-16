import functools

def compare(a,b):
    t1 = str(a) + str(b)
    t2 = str(b) + str(a)
    return (int(t1) > int(t2)) - (int(t1) < int(t2))

def solution(nums):
    sorted_nums = sorted(
    nums, key=functools.cmp_to_key(lambda a,b: compare(a,b)), reverse=True)
    
    ans = "".join(str(x) for x in sorted_nums)
    return "0" if int(ans)==0 else ans