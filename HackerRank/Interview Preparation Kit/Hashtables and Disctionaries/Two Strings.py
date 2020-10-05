t = int(input())


def hashstring(first, second):
    flag = False
    hashwords = {}
    for i in first:
        if hashwords.get(i) != None:
            if hashwords[i] > 0:
                hashwords[i] += 1
        else:
            hashwords[i] = 1
    # print(hashwords)        
    for j in hashwords:
        for k in second:
            if k==j:
                return True
                break
            
   
while t != 0:
    m = input()
    n = input()
    first = list(m)
    second = list(n)
    # print(first,second)
    res = hashstring(first, second)
    if res:
        print("YES")
    else:
        print("NO")
    t -= 1
