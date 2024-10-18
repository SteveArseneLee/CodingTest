def proc_2(x):
    len_x = len(x)
    tmp = bin(len_x)
    return tmp[2:]
    

def solution(s):
    # print(type(s))
    # proc_1(list(s))
    answer = [0, 0]

    while len(s) > 1:
        prev_s = len(s)
        s = [x for x in s if x!='0']
        len_s = len(s)
        answer[1] += prev_s - len_s
        tmp = bin(len_s)
        s = tmp[2:]
        answer[0] += 1
    # answer.append(cnt)
    # answer.append(b)
    # print(s)
    
    return answer