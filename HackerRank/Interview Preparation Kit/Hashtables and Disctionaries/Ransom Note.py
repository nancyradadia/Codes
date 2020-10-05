def ransom(magazine, note):
    hashword = {}
    for i in magazine:
        if hashword.get(i) != None:
            if hashword[i] > 0:
                hashword[i] += 1
        else:
            hashword[i] = 1

    for j in note:
        if hashword.get(j) is None or hashword[j] == 0:
            return False
        else:
            hashword[j] -= 1
    print(hashword)
    return True

m, n = input().split()
# print(m,n)

magazine = list(map(str, input().rstrip().split()))
note = list(map(str, input().rstrip().split()))
# print(magazine)
ans = ransom(magazine,note)

if ans:
    print("Yes")
else:
    print("No")