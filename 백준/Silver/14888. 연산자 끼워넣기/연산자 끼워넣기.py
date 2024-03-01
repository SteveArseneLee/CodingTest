import sys
si = sys.stdin.readline
# 수의 개수 N(2~N~11)
n = int(si())

# 수열 주어짐
nums = list(map(int, si().split()))
# 연산자 개수
# 덧셈, 뺄셈, 곱셈, 나눗셈
operators = list(map(int, si().split()))
min = 1e9
max = -1e9

def calculator(num1, operator, num2):
    if operator == 0:
        return num1 + num2
    if operator == 1:
        return num1 - num2
    if operator == 2:
        return num1 * num2
    if operator == 3:
        if num1 < 0:
            return -((-num1)//num2)
        else:
            return num1 // num2

def rec_func(k, value):
    # 종료조건 : n개 숫자 다 채움
    if k == n-1:
        global min, max
        min = min if min < value else value
        max = max if max > value else value
    else:
        global operators
        for cand in range(4):
            if operators[cand] >= 1:
                # 연산자 선택
                operators[cand] -= 1
                # 그 다음 칸으로 넘어가고 지금까지꺼 연산
                rec_func(k+1, calculator(value, cand, nums[k+1]))
                # 연산자 다시 선택 풀어주기
                operators[cand] += 1

# 처음부터 시작
rec_func(0, nums[0])
print(max)
print(min)