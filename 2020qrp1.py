from sys import * 
num = int(stdin.readline())
for j in range(1, num+1):
    n = int(stdin.readline())
    lst_matrix = []
    for f in range(n):
        lst_inp = list(map(int, stdin.readline().split()))
        lst_matrix.append(lst_inp)
    trace = 0
    for k in range(n):
        trace += lst_matrix[k][k]
    r, c = 0, 0
    lst_vert = []
    for x in range(n):
        lst_vert_local = []
        for i in range(1, n+1):
            if lst_matrix[x].count(i) != 1:
                r += 1
                break
        for m in range(n):
            lst_vert_local.append(lst_matrix[m][x])
        lst_vert.append(lst_vert_local)
    for p in range(n):
        for q in range(1, n+1):
            if lst_vert[p].count(q) != 1:
                c += 1 
                break
    print("Case #"+str(j)+":", trace, r, c)