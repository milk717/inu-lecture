import time

N = int(input('2 이상의 자연수 입력 : '))
while N < 2:
    print(N, '은(는) 2 이상의 자연수가 아닙니다.')
    N = int(input('2 이상의 자연수 입력 : '))

a = list(range(N + 1))

start = time.time()

a[1] = 0
i = 2

while i <=N/2:
    j = 2
    while i*j <= N:
        a[i*j] = 0
        j = j + 1
    i = i + 1

end = time.time() - start
print('실행시간 : ', end)

cnt = 0
for i in range(1, N + 1):
    if a[i] != 0:
        cnt = cnt + 1
print(cnt, '개의 소수 발견')

        


