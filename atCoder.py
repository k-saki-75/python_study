
# ITP1_7_B - How Many Ways?
import itertools
#def LI(): return list(map(int,input().split()))
#while 1:
 # n,x = LI()
  #if n==x==0:
   # break;
  #ans = 0
  #for i,j,k in itertools.combinations(range(1,n+1),3):
   # if i+j+k==x:
    #  ans += 1
  #print(ans)

  # AtCoder Beginner Contest 106 B - 105
# def I(): return int(input())
# N = I()
# ans = 0
# if N>=105:
#     for i in range(105,N+1,2):
#         cout_yakusuu = 0
#         for j in  range(1,int(i**0.5)+1):
#             if i%j==0:
#                 cout_yakusuu += 2
#         if cout_yakusuu==8:
#             ans += 1
# print(ans)

# AtCoder Beginner Contest 122 B - ATCoder
# S = input()
# ans, temp = 0,0
# for x in S:
#     if x in 'ACGT':
#         temp += 1
#     else:
#         temp  = 0
#     ans = max(ans, temp)
# print(ans)
# import itertools
# S = input()
# ans = 0
# for i, j in itertools.combinations_with_replacement(range(len(S)), 2):
#     if all([x in 'ACGT' for x in S[i:j+1]]):
#         ans = max(ans, j+1-i)
# print(ans) 

# パ研杯 2019 c -カラオケ
# def LI(): return list((map(int,input().split())))
# N,M = LI()
# A = [LI() for _ in range(N)]
# ans = 0
# for i in range(M):
#     for j in range(i+1,M):
#         temp =0
#         for k in range(N):
#             temp+= max(A[k][i],A[k][j])
#         ans = max(ans,temp)
# print(ans)

#AtCoder Beginner Contest 095 C - Half and Half
# def LI(): return list(map(int,input().split()))
# A,B,C,X,Y = LI()
# ans = float('INF')
# for i in range(max(X,Y)+1):
#   price = A*max(X-i,0)+B*max(Y-i,0)+C*2*i
#   ans = min(ans,price)
# print(ans)

#三井住友信託銀行プログラミンコンテスト
# def I(): return int(input())
# N = I()
# S = input()
# ans = 0
# for i in range(1000):
#   num = str(i).zfill(3)
#   if S.find(num[0]) == -1:
#     continue
#   S1 = S[S.find(num[0])+1:]
#   if S1.find(num[1])==-1:
#     continue
#   S2 = S1[S1.find(num[1])+1:]
#   if S2.find(num[2])==-1:
#     continue
#   ans += 1
# print(ans)

# JOI 2007 本線 3 - 最古の遺跡
# def I(): return int(input())
# def TI(): return tuple(map(int,input().split()))
# n = I()
# xy = [TI() for _ in range(n)]
# set_xy = set(xy)
# ans = 0
# for i in range(n):
#   x1,y1 = xy[i]
#   for j in range(i+1,n):
#     x2,y2 = xy[i]
#     vectorx,vectory = x2-x1,y2-y1
#     if(x1-vectory,y1+vectorx) in set_xy and (x2-vectory,y2+vectorx) in set_xy:
#       ans =max(ans, vectorx**2+vectory**2)
# print(ans)

# Square869120Contest #6 B - AtCoder Markets
# def I(): return int(input())
# def LI(): return list(map(int,input().split()))
# N = I()
# A = [LI() for _ in range(N)]
# T_A = list(zip(*A))
# ans = float('INF')
# for x,y in itertools.product(T_A[0],T_A[1]):
#   temp = 0
#   for z in A:
#     temp += abs(z[0]-x)
#     temp += z[1]-z[0]
#     temp += abs(z[1]-y)
#   ans = min(ans,temp)
# print(ans)

#JOI 2008 予選 4 -星探し
# import numpy as np
# def I(): return int(input())
# def LI(): return list(map(int, input().split()))
# def solve():
#   M = I()
#   Mxy = np.array(sorted([LI() for _ in range(M)]))
#   N = I()
#   Nxy = np.array(sorted([LI() for _ in range(N)]))
#   Mvector = []
#   for i in range(1,M):
#     Mvector.append(Mxy[i]-Mxy[0])
#   if M==1:
#     return Nxy[0]-Mxy[0]
#   for i in range(N):
#     for j in range(i+1,N):
#       Nvector = Nxy[j]-Nxy[i]
#       if tuple(Nvector) != tuple(Mvector[0]):
#         continue
#       for x in Mvector[1:]:
#         if not (Nxy[i]+x==Nxy).all(axis=1).any():
#           break
#       else:
#         return Nxy[i]-Mxy[0]
# print(*solve()) 
# 15 AtCoder Beginner Contest 145 C - Average Length
# import itertools,math,numpy as np
# def I(): return int(input())
# def LI(): return list(map(int, input().split()))
# N = I()
# xy = np.array([LI() for _ in range(N)])
# sum_norm = 0
# dict_norm = {}
# for a in itertools.permutations(range(N)):
#   for i in  range(len(a)-1):
#     vector = tuple(xy[a[i+1]]-xy[a[i]])
#     if not vector in dict_norm:
#       dict_norm[vector] = np.linalg.norm(vector)
#       vector_inverse = tuple(xy[a[i]] - xy[a[i+1]])
#       dict_norm[vector_inverse] = dict_norm[vector]
#     sum_norm += dict_norm[vector]
# print(sum_norm/math.factorial(N))
#AtCoder Beginner Contest 150 C - Count Order
# import itertools
# def I(): return int(input())
# def LI(): return list(map(int, input().split()))
# N =I()
# P = LI()
# Q = LI()
# sequence = [list(x) for x in itertools.permutations(range(1,N+1))]
# print(abs(sequence.index(P)-sequence.index(Q)))
#ALDS_13_A - 8 クイーン問題
# import itertools
# def I(): return int(input())
# def LI(): return list(map(int, input().split()))
# k = I()
# rc = [LI() for _ in range(k)]
# for a in itertools.permutations(range(8)):
#   XY = [[x,y] for x,y in enumerate(a)]
#   if len(set([x+y for x,y in XY])) != 8 or len(set([x-y for x,y in XY])) != 8:
#     continue
#   count = 0
#   for r,c in rc:
#     if [r,c] in XY:
#       count += 1
#   if count != k:
#     continue
#   board = [['.' for _ in range(8)] for _ in range(8)]
#   for x,y in XY:
#     board[x][y] = 'Q'
#   break
# for b in board:
#   print(*b,sep=' ')
#ALDS_4_B - 二分探索
# import bisect
# def I(): return int(input())
# def LI(): return list(map(int,input().split()))
# n = I()
# S = LI()
# q = I()
# T = LI()
# ans = 0
# for x in T:
#   ok = bisect.bisect(S,x)-1
#   if S[max(ok,0)]==x:
#     ans += 1
# print(ans)
# JOI 2009 本選 ピザ
# import bisect
# def I(): return int(input())
# d = I()
# n = I()
# m = I()
# dn = [0]+sorted([I() for _ in range(n-1)])+[d]
# mn = sorted([I() for _ in range(m)])
# ans = 0
# for x in mn:
#   ok = bisect.bisect(dn,x)-1
#   ans += min(x-dn[ok],dn[ok+1]-x)
# print(ans)

# AtCorder Beginner Contest 077 C-Snuke Festival

# import bisect
# def I(): return int(input())
# def LI(): return list(map(int, input().split()))
# N = I()
# A = sorted(LI())
# B = sorted(LI())
# C = sorted(LI())
# ans = 0
# for b in B:
#   ok_a = bisect.bisect_left(A,b)
#   ok_c = bisect.bisect_right(C,b)
#   ans += ok_a*(N-ok_c)
# print(ans)

# AtCoder Beginner Contest 023 D -射撃王
# import numpy as np
# def I(): return int(input())
# def LI(): return list(map(int, input().split()))
# N = I()
# HS = np.array([LI() for _ in range(N)])
# H = HS[:,0]
# S = HS[:,1]
# rangeN = np.arange(N)
# ok,ng = 10**9+10**9*10**9+1,0
# def is_ok(i):
#   T = (i-H)//S
#   T.sort()
#   return (T>=rangeN).all()
# while abs(ok-ng)>1:
#   mid = (ok+ng)//2
#   if is_ok(mid):
#     ok = mid
#   else:
#     ng = mid
# print(ok)

# AtCoder Regular Contest 054 B - ムーアの法則
def F(): return float(input())
P = F()
high,low = P,0
def f(x):
  return x+P*2**(-x/1.5)
def is_high(i,j):
  return f(i)>=f(j)
while high-low>1*(10**-12):
  mid_right = (high*2+low)/3
  mid_left = (high+low*2)/3
  if is_high(mid_right,mid_left):
    high = mid_right
  else:
    low = mid_left
print(f(high))