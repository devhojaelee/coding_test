#https://www.acmicpc.net/problem/1065

def hansu_sol(num):
    res_cnt = 0
    hansu = 0
    cnt = 1
    x = num
    sav = []
    d = []
    tmp = x
    origin = x
    for _ in range(10):
        if tmp < 10:  # 숫자의 자릿수 갯수
            break
        tmp = int(tmp/10)
        cnt = cnt + 1

    for _ in range(cnt):
        sav.append(x % 10)  # sav 배열에 자리수 입력. sav[0]~sav[3]
        x = int(x/10)

    '''
    for j in range(cnt-1): # d list에 공차를 대입.
        d[j]=sav[j+1]-sav[j] -> 문제가 생김. 왜? -> d[]로 접근하는건 이미 존재하는 원소에 접근할 때!!!
    '''
    for j in range(cnt-1):
        d.append(sav[j+1]-sav[j])

    for p1, p2 in zip(d, d[1:]):
        if p1 ^ p2 == 0:  # p1, p2가 같으면
            # print("hansu")
            #print(p1, p2)
            hansu = hansu+1
        else:
            #print("no hansu")
            break
    if origin <= 99:
        res_cnt = res_cnt+1
    elif len(d)-1 == hansu:  # 비교.
        res_cnt = res_cnt+1
    
    return res_cnt

N = int(input())
sum = 0

for i in range(1,N+1):
    sum=sum+(hansu_sol(i))

print(sum)
