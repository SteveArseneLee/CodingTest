import sys
from itertools import combinations
input = sys.stdin.readline
vowels = ['a', 'e', 'i', 'o', 'u']

l,c = map(int, input().split())
arr = input().split()
arr.sort()

# arrjam = [i for i in arr if i in jam]

for password in combinations(arr,l):
    count = 0
    for i in password:
        if i in vowels:
            count += 1

    if count >= 1 and count <= l-2:
        print(''.join(password))