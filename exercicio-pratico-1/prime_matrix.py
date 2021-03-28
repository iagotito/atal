num_rows, num_columns = map(int, input().split())

limit=int(1e5+2)
diffs=[2,1,0,0]+[1,0]*((limit-2)//2)
for i in range(3,limit):
    if not diffs[i]:
        diffs[i*i::i]=[1]*((limit-i*i)//i+1)
for i in range(limit,4,-1):
    diffs[i]*=diffs[i+1]+1

matrix_diffs = [[diffs[j] for j in map(int,input().split())] for i in range(num_rows)]

min_moves_to_rows = min(sum(i) for i in matrix_diffs)
min_moves_to_cols = min(sum(i) for i in zip(*matrix_diffs))
print(min(min_moves_to_rows, min_moves_to_cols))
