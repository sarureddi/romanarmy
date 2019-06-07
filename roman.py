n1 = int(input())
a1= list(map(int,input().split()))
c1 = 0
for i in range(0,len(a1)-2):
  for j in range(i+1,len(a1)-1):
    for k in range(j+1,len(a1)):
      if i<j<k and a1[i]>a1[j]>a1[k]:
        c1 = c1+1
print(c1)
