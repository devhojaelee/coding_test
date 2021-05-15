from itertools import permutations

k = int(input())
ineq = list(map(str, input().split()))
#ineq = ['<', '>','<']
ans = []
tmp = []
max = 0
min = 9999999999

for x in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], k+1):

    cnt = 0
    for i in range(len(ineq)):

        if ineq[i] == '<':
            if x[i]-x[i+1] < 0:
                cnt = cnt+1
                continue
            else:
                break

        elif ineq[i] == '>':
            if x[i]-x[i+1] > 0:
                cnt = cnt+1
                continue
            else:
                break
    if cnt == k:
        x = list(map(str, x))  # list 안의 원소의 타입을 int <-> str 왔다갔다
        x = "".join(x)
        x = int(x)
        # print(x)
        if x < min:
            min = x
        if x > max:
            max = x

'''
Q. (1,2,3)를 123으로 만드는 방법?
각 원소 str화 -> 문자열 join() -> 다시 int화
'''
print(str(max))

max_len = len(str(max))
min_len = len(str(min))

if max_len != min_len:
    print('0'+str(min))
else:
    print(str(min))
