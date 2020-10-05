n, k = map(int, input().split())


a = list(map(int, input().rstrip().split()))
a.sort()
sum1 = 0
cout = 0
for i in range(len(a)):
    s = sum1+a[i]
    if (s<=k):
      sum1=sum1+a[i];
      cout=cout+1;
    else:
      break;

print(cout)
