s = list(map(str,input().split(" ")))
query = input()
for i in s:
    if(i.startswith(query) != True):
        s.remove(i)
print(s)
