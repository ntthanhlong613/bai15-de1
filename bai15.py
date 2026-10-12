a,b,c=map(int,input().split())
tong=a+b+c
C = max(a,b,c)
B = tong-max(a,b,c)-min(a,b,c)
A = min(a,b,c)
print(max(C-B, B-A) -1)
