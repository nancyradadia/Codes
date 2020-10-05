# n = int(input())
# query = {}
# for i in range(n):
#     data = input()
#     temp = data.split(' ')
#     query[int(temp[0])] = int(temp[1])
#     # o, d = input().split()
#     # o = int(o)
#     # d = int(d)
#     # query[o] = d
# for key, value in query.items():
# 	print('Name: {}, Score: {}'.format(key, value))
q = int(input().strip())

queries = []

for _ in range(q):
    queries.append(list(map(int, input().rstrip().split())))

# print(queries)
arr = []
freq={}
count = 0
for i in range(q):
  
    if queries[i][0] == 1:
        arr.append(queries[i][1])
        for items in arr: 
            freq[items] = arr.count(items)
        
    if queries[i][0] == 2:
        if queries[i][1] in arr:
            for j in arr:
                if queries[i][1]==j:
                    count=count+1
        if count>0:
            arr.remove(queries[i][1])
            del freq[queries[i][1]]
        count = 0
        # print("i=2",arr) 
        
    if queries[i][0]==3:
        # print('hii')
        # print(freq)
        for j in freq:
            # print(j)
            if queries[i][1]==freq[j]:
                print('1')
                break
            else:
                print('0')
                break
        if len(freq)==0:
            print('0')     

# print(arr)
