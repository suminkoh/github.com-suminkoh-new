score1=(input())
score2=(input())
S=sum(map(int, score1.split()))
T=sum(map(int, score2.split()))
if S >= T:
  print(S)
else:
  print(T)