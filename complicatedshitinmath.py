def euclidtree(p, n):
    return [1 if i==0 or i==n-1 else p[i-1]+p[i] for i in range(n)]

List=[]
n=1
arr=[1]
while n!=30:
    arr=euclidtree(arr,n)
    List.append(arr)
    n += 1

s_len = len(" ".join(map(str,List[-1])))
for el in List:
    s = " ".join(map(str,el))
    print(str.center(s,s_len))

input()