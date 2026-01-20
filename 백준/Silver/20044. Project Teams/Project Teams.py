n = int(input())
w_str = input()
w = sorted(list(map(int, w_str.split())))
sums = []
for i in range(1, n+1):
 sums.append(w[i-1] + w[-i])
min_sum = min(sums) 
print(min_sum)