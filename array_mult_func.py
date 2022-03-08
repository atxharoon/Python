def array_mult(A, B):
    num_rows_a = len(A)
    num_cols_a = len(A[0])
    num_cols_b = len(B[0])
    num_rows_b=len(B)
    rows =[]
    for i in range(num_rows_a):
        cols=[]
        for j in range(num_cols_b):
            entrysum=0
            for k in range(num_rows_b):
                entrysum +=(A[i][k])*(B[k][j])
            cols.append(entrysum)
        rows.append(cols)
    return rows


