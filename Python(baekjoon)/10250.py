### 10250번: ACM 호텔

T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    h = 0
    w = 1
    for i in range(N):
        if h == H:
            h = 1
            w += 1
        else:
            h +=1
            
    if len(str(w)) == 1:
        print(str(h)+'0'+str(w))
    else:
        print(str(h)+str(w))
