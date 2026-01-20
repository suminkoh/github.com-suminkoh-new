n=int(input())

group=0
already=[]

for j in range(n):
  a=input()
  already=[]
  for i in range(len(a)):
    if a[i] not in already:
     already.append(a[i])
    else:
      if a[i] != a[i-1]:
        break
  else:
    group += 1

print(group)